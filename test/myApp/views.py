from django.shortcuts import render,reverse , get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect,HttpResponseNotFound
from django.contrib.auth import authenticate
from . import models
from . import forms

def add_USER1(request):
    user_list=models.User.objects.all()
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('login'))
            except:
                form.add_error("user_phoneNumber", "this phone number is already registered")
                return render(request, "signup.html", {'form': form,"user_list":user_list})
        else:
            return render(request , "signup.html", {'form': form,"user_list":user_list})
    else:
        form = forms.UserForm()
        return render(request ,"signup.html", {'form': form,"user_list":user_list})

def login_user(request):
    form = forms.UserLogin()
    if request.method == "POST":
        user_phoneNumber = request.POST['user_phoneNumber']
        user_password = request.POST['user_password']
        try:
            user = models.User.objects.get(user_phoneNumber=int(user_phoneNumber))
            if user.user_password == user_password:
                print("User phone number and password match.")
                return render(request , "menu.html")
            else:
                print("User phone number and password do not match.")
                return render(request, "login.html", {"error": "User phone number and password do not match.",'form': form})

        except models.User.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid login data",'form': form})
    else:

        return render(request, "login.html", {'form': form})

def menu(request):
    return render(request, "menu.html")

def displayView(request):
    book_list=models.book.objects.all()
    return render(request, "display.html", {
        "books": book_list
    })


def update(request, book_id):
    book = get_object_or_404(models.book, id = book_id)

    if request.method == 'POST':
        form = forms.AddBook(request.POST, instance=book)  # Pass existing data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('display'))  # Redirect after update
    else:
        form = forms.AddBook(instance=book)  # Pre-populate the form

    context = {'form': form, 'book': book}
    return render(request, 'update.html', context)


def delete(request, book_id):
    book = models.book.objects.get( id = book_id)
    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect(reverse('display'))
   
    context = {'book': book}
    return render(request, 'delete.html', context)

def add(request):
    authors=models.User.objects.all()
    if request.method == "POST":
        forma= forms.AddBook(request.POST)
        if forma.is_valid():
            forma.save()
            return HttpResponseRedirect(reverse('display'))
    else:
        return render(request, "add.html", {'form': forms.AddBook(),"author_list":authors})    


