from django.shortcuts import  render, redirect
from .forms import NewUserForm, NewProfileForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def home(request):
    return render(request, template_name="base.html")

def register_request(request):
	user_form = NewUserForm(request.POST or None)
	profile_form = NewProfileForm(request.POST or None)
	if request.method == "POST":

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			messages.success(request, "Registration successful." )
			return redirect("show_users")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":user_form , "profile_form":profile_form})


def showUsers(request):
	user = User.objects.all()
	return render(request, "show_users.html" , {'user' : user})

