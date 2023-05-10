from django.shortcuts import render,redirect
from django.contrib import messages
from fitness.models import Contact, Enrollment,Gallery

# Create your views here.
def home(request):
    return render(request,'index.html')
def gallery(request):
    posts = Gallery.objects.all()
    context = { 'posts':posts}
    return render(request,'gallery.html',context )



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        fullemail = request.POST.get('email')
        desc = request.POST.get('message')

        query = Contact(name=name, email=fullemail, message = desc)

        query.save()

        messages.info(request, 'thanks for contacting us')
        return redirect('/')
    
    return render(request, '/')

def enroll(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        fullemail = request.POST.get('email')
        number = request.POST.get('phone')
        desc = request.POST.get('message')

        myquery = Enrollment (name=name, email=fullemail, phonenumber = number, message = desc)

        myquery.save()

        messages.info(request, 'Enrollment Successful')
        return redirect('/')
    
    return render(request, '/')
