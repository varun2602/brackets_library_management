from django.shortcuts import render,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from . import models
from . import serializers
import io
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_book(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        name = python_data.get('book_name', None)
        if name is not None and name != 'all':
            try:
                book_api = models.books.objects.get(book_name = name)
                serialized = serializers.bookSerializer(book_api)
                json_res = JSONRenderer().render(serialized.data)
                return HttpResponse(json_res, content_type = 'application/json')
            except models.books.DoesNotExist:
                data = {
                'message':'Invalid data'
                }
                json_response = json.dumps(data)
                return HttpResponse(json_response, content_type = 'application/json')
        elif name == 'all':
            books_all = models.books.objects.all()
            serialized = serializers.bookSerializer(books_all, many = True)
            json_response = JSONRenderer().render(serialized.data)
            return HttpResponse(json_response, content_type = 'application/json')
        else:
            data = {
                'message':'Invalid data'
            }
            json_response = json.dumps(data)
            return HttpResponse(json_response, content_type = 'application/json')
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        book_name = python_data.get('book_name', None)
        if book_name is not None:
            try:
                models.books.objects.get(book_name = book_name)
                data = {'message':'Name already taken'}
                json_response = json.dumps(data)
                return HttpResponse(json_response, content_type = 'application/json')
            except models.books.DoesNotExist:
                serialized = serializers.bookSerializer(data = python_data)
                if serialized.is_valid():
                    # print(serialized)
                    serialized.save()
                    data = {'message':'Data created successfully'}
                    json_res = json.dumps(data)
                    return HttpResponse(json_res, content_type = 'application/json')
                json_response = JSONRenderer().render(serialized.errors)
                return HttpResponse(json_response, content_type = 'application/json')
            
@csrf_exempt
def put_data_complete(request):
    if request.method == 'PUT':
        request_body = json.loads(request.body)
        book_name = request_body.get('book_name', None)
        book_author = request_body.get('book_author', None)
        is_issued = request_body.get('is_issued', None)
        issued_to = request_body.get('issued_to', None)
        
        data = {
            'book_name':book_name,
            'book_author':book_author,
            'is_issued':is_issued,
            'issued_to':issued_to
        }
        json_data = json.dumps(data)
        # stream = io.BytesIO(json_data)
        python_data = json.loads(json_data)
        try:
            book_obj = models.books.objects.get(book_name = book_name)
            serialized = serializers.bookSerializer(book_obj, data = python_data)
            if serialized.is_valid():
                serialized.save()
                data = {'message':'Data Updated successfully'}
                json_res = json.dumps(data)
                return HttpResponse(json_res, content_type = 'application/json')
            json_response = JSONRenderer().render(serialized.errors)
            return HttpResponse(json_response, content_type = 'application/json')
        except models.books.DoesNotExist:
            data = {'message':'Book does not exists'}
            json_response = json.dumps(data)
            return HttpResponse(json_response, content_type = 'application/json')


@csrf_exempt 
def put_data_partial(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        book_name = python_data.get('book_name', '')
        if book_name is not '':
            try:
                book_obj = models.books.objects.get(book_name = book_name)
                serialized = serializers.bookSerializer(book_obj, data = python_data, partial = True)
                if serialized.is_valid():
                    serialized.save()
                    data = {'messsage':'Data updated successfully'}
                    json_data = json.dumps(data)
                    return HttpResponse(json_data, content_type = 'application/json')
                json_response = JSONRenderer().render(serialized.errors)
                return HttpResponse(json_response, content_type = 'application/json')
            except models.books.DoesNotExist:
                data = {'message':'Book does not exists'}
                json_data = json.dumps(data)
                return HttpResponse(json_data, content_type = 'application/json')

        else:
            data = {'message':'book name required'}
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type = 'application/json')
@csrf_exempt
def delete_data(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        book_name = python_data.get('book_name', None)
        if book_name is not None or book_name != '':
            try:
                book_obj = models.books.objects.get(book_name = book_name)
                book_obj.delete()
                data = {'message': 'Book deleted successfully'}
                json_response = json.dumps(data)
                return HttpResponse(json_response, content_type = 'application/json')
            except models.books.DoesNotExist:
                data = {'message':'Book does not exists'}
                json_data = json.dumps(data)
                return HttpResponse(json_data, content_type = 'application/json')
        data = {'message':'Book name cannot be blank'}
        json_response = json.dumps(data)
        return HttpResponse(json_response, content_type = 'application/json')
        

    
        
        


