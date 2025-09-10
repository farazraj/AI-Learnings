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

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone'):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.phone = request.POST.get('phone')
            employee.save()
            return redirect("emplist")   # 👈 after saving go back to list
    return render(request, "index.html")


#to write he database setting ton the settings file
def update_settings_file(database_name, reg_code):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proj_folder = os.path.join(base_dir, 'employee')
    settings_file_path = os.path.join(proj_folder, 'settings.py')

    with open(settings_file_path, 'r') as f:
        lines = f.readlines()

    with open(settings_file_path, 'w') as f:
        database_exists = False  # Flag to check if the database name exists in the file
        for line in lines:
            if line.startswith('DATABASES = {'):
                f.write(line)
                if not database_exists:
                    # Write the database details only if the database name doesn't exist
                    if not any(line.startswith(f"    '{reg_code}'") for line in lines):
                        f.write(f"    '{reg_code}': {{\n")
                        f.write(f"        'ENGINE': 'mssql',\n")
                        f.write(f"        'NAME': '{database_name}',\n")
                        user = "os.environ.get('DB_USER_L')"
                        password = "os.environ.get('DB_PASS_L')"
                        host = "os.environ.get('DB_HOST_L')"
                        if not user:
                            user = "''"
                        if not password:
                            password = "''"
                        if host == '(LocalDB)\MSSQLLocalDB':
                            host = "'(LocalDB)\\MSSQLLocalDB'"
                        f.write(f"        'USER': {user},\n")
                        f.write(f"        'PASSWORD': {password},\n")
                        f.write(f"        'HOST': {host},\n")
                        f.write(f"        'PORT': '',\n")
                        f.write(f"        'OPTIONS': {{'driver': 'ODBC Driver 17 for SQL Server',}},\n")
                        f.write(f"    }},\n")
                        f.write(f"    }},\n")
                        database_exists = True
            else:
                f.write(line)



@login_required
def emplist(request):
    # update_settings_file("example_db", "2873")

    employee_list = Employee.objects.order_by("name")
    empdict= {'employees':employee_list}
    return render(request, 'emplist.html',context = empdict)



def delete_employee(request, pk):
    emp = get_object_or_404(Employee, id=pk)
    emp.delete()
    return redirect("emplist")


@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, id=pk)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.phone = request.POST.get("phone")
        employee.save()
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
