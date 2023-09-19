from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy

from .models import District,Details,Banks
from . forms import DetailsForm
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    district_details= District.objects.all()


    return render(request,"home.html",{'district':district_details})

def login(request):
    district_details = District.objects.all()

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("bank:details")
        else:
            messages.info(request,"Invalid username or password")
            return redirect('bank:login')

    return render(request,'login.html',{'district':district_details})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                messages.info(request, "Password Mismatch")
                return redirect('bank:login')
        else:
            messages.info(request, "Password Mismatch")
            return redirect("register")



    return render(request,'register.html')

def logout(requests):
    auth.logout(requests)
    return redirect("/")

def details(request):
    district_details=District.objects.all()
    return render(request, 'details.html', {'district': district_details})

def Add_Details(request):
    form = DetailsForm()
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:add')
    return render(request, 'add.html', {'form': form})

def Update_view(request, pk):
    person = get_object_or_404(Details, pk=pk)
    form = DetailsForm(instance=details)
    if request.method == 'POST':
        form = DetailsForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('details_change', pk=pk)
    return render(request, 'add.html', {'form': form})

# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = Banks.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


# class PreviewView(ListView):
#     model = Details
#     context_object_name = 'details'


# class AddDetailsView(CreateView):
#     model = Details
#     form_class = DetailsForm
#     template_name = 'add.html'
#     # success_url = reverse_lazy('add')

# def load_branches(request):
#     district_id = request.GET.get('district')
#     branch = Banks.objects.filter(district_id=district_id).order_by('branch')
#     return render(request, 'branch_dropdown.html', {'branch': branch})



