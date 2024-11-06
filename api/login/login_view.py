from django.shortcuts import render

# Create your views here.
def login_views(request):
    template_name="authentication-login.html"
    return render(request,template_name)

# View for register
def register_view(request):
    template_name="authentication-register.html"
    return render(request,template_name)

# View for forgot
def forgot_view(request):
    template_name="authentication-password.html"
    return render(request,template_name)