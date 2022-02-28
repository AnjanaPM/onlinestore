from django.shortcuts import redirect


def sign_in(func):
    def wrapper(req, *args, **kwargs):
        if req.user.is_authenticated:
            # func(req, *args, **kwargs)
            return func(req, *args, **kwargs)

        else:
            return redirect('signin')
            # return redirect('signin')

    return wrapper


def sign_in_authentication(req, *args, **kwargs):
    return kwargs




def owner_permission_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return func(request,*args,**kwargs)
        else:
            return redirect('signin')
    return wrapper
