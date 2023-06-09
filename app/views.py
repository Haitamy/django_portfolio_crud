from django.shortcuts import render, redirect
from .models import About, Services, Testi, Skills, Cont, Filtre, Porto
from .forms import About_form, Services_form, Testi_form, Skills_form, Cont_form, Filtre_form, Porto_form

# Create your views here.
def home(request):
    about=About.objects.all()[0]
    skills=Skills.objects.all()
    services=Services.objects.all()
    porto=Porto.objects.all()
    filtre=Filtre.objects.all()
    testi=Testi.objects.all()
    cont=Cont.objects.all()[0]
    return render(request,'perso/home.html',{'about':about,'skills':skills,'services':services,'porto':porto,'filtre':filtre,'testi':testi,'cont':cont})
def admin(request):
    return render(request,'perso/admin.html')
def editSkills(request,id):
    edit = Skills.objects.get(id=id)
    skills=Skills.objects.all()
    if request.method == 'POST':
        form = Skills_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('showSkills')
    else:
        form = Skills_form(instance=edit)
    return render(request,'perso/editSkills.html', {'form': form,'skills':skills})
def editServices(request,id):
    edit = Services.objects.get(id=id)
    services=Services.objects.all()
    if request.method == 'POST':
        form = Services_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('showServices')
    else:
        form = Services_form(instance=edit)
    return render(request,'perso/editServices.html',{'form':form})
def editTesti(request,id):
    edit = Testi.objects.get(id=id)
    testi=Testi.objects.all()
    if request.method == 'POST':
        form = Testi_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('showTesti')
    else:
        form = Testi_form(instance=edit)
    return render(request,'perso/editTesti.html',{'form':form})
def editPortfolio(request,id):
    edit = Porto.objects.get(id=id)
    porto=Porto.objects.all()
    if request.method == 'POST':
        form = Porto_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('showPorto')
    else:
        form = Porto_form(instance=edit)
    return render(request,'perso/editPortfolio.html',{'form':form,'porto':porto})
def editContact(request,id):
    edit = Cont.objects.get(id=id)
    cont=Cont.objects.all()
    if request.method == 'POST':
        form = Cont_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('showContact')
    else:
        form = Cont_form(instance=edit)
    return render(request,'perso/editContact.html',{'form':form,'cont':cont})
def editAbout(request, id):
    edit = About.objects.get(id=id)
    about=About.objects.all()[0]
    if request.method == 'POST':
        form = About_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = About_form(instance=edit)
    return render(request, 'perso/editAbout.html', {'form': form,'about':about})
def destroySkills(request, id):
    destroy = Skills(id)
    destroy.delete()
    return redirect('showSkills')
def destroyServices(request, id):
    destroy = Services(id)
    destroy.delete()
    return redirect('showServices')
def destroyTesti(request, id):
    destroy = Testi(id)
    destroy.delete()
    return redirect('showTesti')
def destroyPorto(request, id):
    destroy = Porto(id)
    destroy.delete()
    return redirect('showPorto')
def showSkills(request):
    skills=Skills.objects.all()
    return render(request,'perso/showSkills.html',{'skills':skills})
def addSkills(request):
    if request.method=='POST':
        form=Skills_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showSkills')
    else:
        form=Skills_form()
    return render(request,'perso/addSkills.html',{'form':form})
def addServices(request):
    if request.method=='POST':
        form=Services_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showServices')
    else:
        form=Services_form()
    return render(request,'perso/addServices.html',{'form':form})
def addTesti(request):
    if request.method=='POST':
        form=Testi_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showTesti')
    else:
        form=Testi_form()
    return render(request,'perso/addTesti.html',{'form':form})
def addFiltre(request):
    if request.method=='POST':
        form=Filtre_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showPorto')
    else:
        form=Filtre_form()
    return render(request,'perso/addFiltre.html',{'form':form})
def addPorto(request):
    if request.method=='POST':
        form=Porto_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showPorto')
    else:
        form=Porto_form()
    return render(request,'perso/addPorto.html',{'form':form})
def showServices(request):
    services=Services.objects.all()
    return render(request,'perso/showServices.html',{'services':services})
def showTesti(request):
    testi=Testi.objects.all()
    return render(request,'perso/showTesti.html',{'testi':testi})
def showContact(request):
    cont=Cont.objects.all()[0]
    return render(request,'perso/showContact.html',{'cont':cont})
def showPorto(request):
    porto=Porto.objects.all()
    filtre=Filtre.objects.all()
    return render(request,'perso/showPorto.html',{'porto':porto,'filtre':filtre})