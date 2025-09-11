import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from emp.models import Employee, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import UserForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from emp.tasks import process_bulk_employee

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone'):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.phone = request.POST.get('phone')
            employee.save()
            messages.success(request, "Employee added successfully..!!")
            return redirect("emplist")   # 👈 after saving go back to list
    return render(request, "index.html")

@login_required
def bulk_add(request):

    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Please upload a CSV file.")
            return redirect("bulk_add")

        # Read CSV with pandas
        df = pd.read_csv(csv_file)

        # Ensure required columns exist
        required_cols = {"name", "phone"}
        if not required_cols.issubset(df.columns):
            messages.error(request, "CSV must contain name, phone columns.")
            return redirect("bulk_add")

        # Convert to list of dicts
        emp_data = df.to_dict(orient="records")

       # async processing + real-time WebSocket updates
        process_bulk_employee.delay(emp_data)
        
        messages.success(request, f"{len(emp_data)} contacts are being processed.")
        return redirect("bulk_add")

    return render(request, "bulk_add.html")



@login_required
def emplist(request):
    # update_settings_file("example_db", "2873")

    employee_list = Employee.objects.order_by("name")
    empdict= {'employees':employee_list}
    return render(request, 'emplist.html',context = empdict)


@login_required
def delete_employee(request, pk):
    emp = get_object_or_404(Employee, id=pk)
    emp.delete()
    messages.warning(request, "Employee deleted successfully..!!")
    return redirect("emplist")

@login_required
def delete_multiple(request):
    """
    Deletes multiple employees by IDs passed in GET param `ids`.
    Example: /delete-multiple/?ids=1,2,3
    """
    ids = request.GET.get("ids", "")
    if ids:
        id_list = [int(x) for x in ids.split(",") if x.isdigit()]
        deleted_count, _ = Employee.objects.filter(id__in=id_list).delete()
        messages.success(request, f"✅ Successfully deleted {deleted_count} employee(s).")
        return redirect("emplist")
    else:
        messages.warning(request, "⚠️ No employees selected for deletion.")
        

    return redirect("emplist")  # redirect back to records page



@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, id=pk)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.phone = request.POST.get("phone")
        employee.save()
        messages.success(request, "Employee Updated successfully..!!")
        return redirect("emplist")

    # reusing the same index.html template
    return render(request, "index.html", {"employee": employee})




@login_required
def search(request):
    if request.method=='POST':
        searched = request.POST.get('searched')
        empl = Employee.objects.filter(name__icontains = searched)
        return render(request, "search.html",{'searched':searched, 'empl':empl})
    else:
        return render(request, "search.html")


@login_required
def nav(request):
    return render(request, 'nav.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)


        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            UserProfile.objects.create(user = user, reg_code = 255)


            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'register.html',
                                        {'user_form':user_form,
                                            'registered':registered})




@csrf_exempt
def login_user(request):

    if request.method == "POST":
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")

        user = authenticate(request, username=username, password=password)
        if user:
            request.session['reg_code'] = username

            if user.is_active:
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse('Account Not Active')
        else:
             return HttpResponse("Invalid Login Details!")


    else:
        return render (request, 'login_user.html')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def autocomplete_search(request):
    query = request.GET.get('name', '')
    queryset = Employee.objects.filter(name__icontains=query)[:10]
    results = [m.name for m in queryset]
    return JsonResponse(results, safe=False)
