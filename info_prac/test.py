def require_admin(func):
    def wrapper(*args, **kwargs):
        if args or kwargs != 'admin':
            print("Access denied")
        else:
            return func(*args, **kwargs)
    return wrapper

@require_admin
def delete_user(user):
    print(f"{user} deleted a record")


delete_user("guest")   # Access denied
delete_user("admin")   # admin deleted a record

