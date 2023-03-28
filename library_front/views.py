from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
@login_required(login_url="login")
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
@csrf_exempt
def get(request):
    if request.method == 'GET':
        return render(request, 'get.html')
    if request.method == 'POST':
        URL = 'http://127.0.0.1:8000/library_back/get_book'
        form_data = request.POST.get('book', None)
        data = {'book_name':form_data}
        json_data = json.dumps(data)
        r = requests.get(url = URL, data = json_data)
        response = r.json()
        context = {'response':response}
        return render(request, 'get.html', context)
    
@csrf_exempt
def get_all(request):
    if request.method == 'GET':
        URL = 'http://127.0.0.1:8000/library_back/get_book'
        form_data = request.POST.get('book', None)
        data = {'book_name':'all'}
        json_data = json.dumps(data)
        r = requests.get(url = URL, data = json_data)
        response = r.json()
        context = {'response':response}
        return render(request, 'get_all.html', context)
    
@csrf_exempt
def add_book(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    if request.method == 'POST':
        book_name = request.POST.get('book_name', None)
        book_author = request.POST.get('book_author', None)
        if book_name != '' and book_author != '':
            URL2 = 'http://127.0.0.1:8000/library_back/add_book'
            data = {
                'book_name':book_name,
                'book_author':book_author
            }
            json_data = json.dumps(data)
            r = requests.post(url = URL2, data = json_data)
            response = r.text
            return HttpResponse(response, content_type = 'application/json')
       
        data = {'message':'Invalid data'}
        # json_data = json.dumps(data)
        return JsonResponse(data)
    
@csrf_exempt
def put_data_complete(request):
    if request.method == 'GET':
        return render(request, 'put_complete.html')
    if request.method == 'POST':
        book_name = request.POST.get('book_name', None)
        book_author = request.POST.get('book_author', None)
        is_issued = request.POST.get('is_issued', None)

        if book_name == '':
            context = {'message':'Book Name Required!'}
            return render(request, 'put_complete.html', context)
        
        if book_author == '':
            context = {'message':'Book author name required!'}
            return render(request, 'put_complete.html', context)
        
        if is_issued == None:
            context = {'message': 'Please indicate whether the book is issued or not'}
            return render(request, 'put_complete.html', context)
        if is_issued == 'False':
            issued_to = None
        elif is_issued == 'True':
            issued_to = request.POST.get('issued_to')
        data = {
            'book_name':book_name,
            'book_author':book_author,
            'is_issued':is_issued,
            'issued_to':issued_to
        }
        json_data = json.dumps(data)
        URL3 = 'http://127.0.0.1:8000/library_back/put_data_complete'
        r = requests.put(url = URL3, data = json_data)
        response = r.json()
        context = {'response':response}

        return render(request, 'put_complete.html', context)

@csrf_exempt
def put_data_partial(request):
    if request.method == 'GET':
        return render(request, 'put_partial.html')
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        is_issued = request.POST.get('is_issued')
        # issued_to = request.POST.get('issued_to')
        if book_name == '' and book_author == '':
            context = {'message':'Book Name and Book Author cannot be blank'}
            return render(request, 'put_partial.html', context)
        if is_issued == False:
            issued_to =  None 
        elif is_issued == True:
            issued_to = request.POST.get('issued_to')
        elif is_issued == None:
            issued_to = request.POST.get('issued_to')
        
        if issued_to == '':
            issued_to = None 

        data = {
            'book_name':book_name,
            'book_author':book_author,
            'is_issued':is_issued,
            'issued_to':issued_to
        }
        json_data = json.dumps(data)
        URL4 =  'http://127.0.0.1:8000/library_back/put_data_partial'
        r = requests.put(url = URL4, data = json_data)
        response = r.text
        print(response)
        return HttpResponse(response, content_type = 'application/json')

@csrf_exempt
def delete_data(request):
    if request.method == 'GET':
        return render(request, 'delete.html')
    if request.method == 'POST':
        book_name = request.POST.get('book')
        print(book_name)
        data = {
        'book_name':book_name
        }
        URL5 = 'http://127.0.0.1:8000/library_back/delete_data'
        json_data = json.dumps(data)
        r = requests.delete(url = URL5, data = json_data)
        response = r.json()
        context = {'response':response}
        return render(request, 'delete.html', context)
    
@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword  = request.POST.get('cpassword')
        
        # Checking if passwords are confirmed properly 
        if password != cpassword:
            data = {'message':'Confirm password properly!'}
            return JsonResponse(data)
        
        # Check if user already exists 
        try:
            
            user_check = models.CustomUser.objects.get(username = username)
            data = {'message':'Username is taken'}
            
            return JsonResponse(data)
            
        except models.CustomUser.DoesNotExist:
            user_create = models.CustomUser.objects.create_user(username = username, name = name, email = email, password = password)
            user_create.save()
            data = {'message':'Registered successfully!'}
            return JsonResponse(data)
        
@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username = username, password = password)
        print(user)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            data = {'message':'Invalid Credentials'}
            return render(request, 'login.html', data)
@csrf_exempt
def validate_name(request):
    username = request.POST.get('username')

    try:
        user_check = models.CustomUser.objects.get(username = username)
        data = {'r':20}
        return JsonResponse(data)
    except models.CustomUser.DoesNotExist:
        data = {'r':200}
        return JsonResponse(data)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


    


