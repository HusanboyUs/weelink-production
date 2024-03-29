from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from .models import Profile, ProfileLink,Projects
from .forms import ContactForm, userRegisterForm,updateProfileForm,addLinksForm,editProfileLinkForm
from django.contrib import messages
from django.views.generic import TemplateView
#imports
def registerView(request):
    form=userRegisterForm()
    if request.method=='POST':
        form=userRegisterForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('loginView')
    else:
        pass          
    context={'form':form}
    return render(request, 'main/signup.html', context)        

def loginView(request):
    form=userRegisterForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profileView')
        else:
            messages.error(request, 'Your credentials did not match ours', )    
    context={'form':form}        
    return render(request, 'account/login.html', context)

@login_required(login_url='loginView')
def profileView(request):
    user=request.user
    human=Profile.objects.filter(user=user).first()
    links=ProfileLink.objects.filter(user=human)
    context={'user':user, 'links':links}
    return render(request, 'main/profile.html',context)

@login_required(login_url='loginView')
def updateProfileView(request):
    owner=request.user
    profile=Profile.objects.get(user=owner)
    form=updateProfileForm(instance=profile)
    if request.method=='POST':
        form=updateProfileForm(request.POST,request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('profileView')
    context={'form':form}
    return render(request, 'main/updateProfile.html', context)


@login_required(login_url='loginView')
def addProfileLink(request):
    form=addLinksForm
    user=request.user
    if request.method=='POST':
        form=addLinksForm(request.POST)
        if form.is_valid():
            user=request.user
            user_user=Profile.objects.filter(user=user).first()
            instance=form.save(commit=False)
            instance.user=user_user
            instance.save()
            return redirect('profileView')
    context={'form':form}
    return render(request, 'main/addProfileLink.html', context)   
      
@login_required(login_url='loginView')
def deleteProfileLink(request, pk):
    link=ProfileLink.objects.get(id=pk)
    form=editProfileLinkForm
    if request.method=='POST':
        link.delete()
        return redirect('profileView')
    context={'link':link, 'form':form}
    return render(request, 'main/deleteLinks.html', context)        


def userView(request, user_slug):
    try:
        profile=get_object_or_404(Profile, slug=user_slug)
        links=ProfileLink.objects.filter(user=profile)
        projects=Projects.objects.filter(user=profile)
        context={'profile':profile, 'links':links, 'projects':projects}
    except:
        return render(request, 'main/not404.html')    
    return render(request, 'main/user2.html', context)

def homeView(request):
    users=Profile.objects.all()
    context={'users':users}
    return render(request, 'main/home.html', context)

def ContactView(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We have recieved your message successfully!')
            #return redirect('homeView')
            #return another value or head to home view
    context={'form':form}        
    return render(request, 'main/contact.html', context)

class ApiView(TemplateView):
    template_name='main/apiDoc.html'


api_view=ApiView.as_view()



