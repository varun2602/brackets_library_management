import requests 
import json 

URL = 'http://127.0.0.1:8000/library_back/get_book'
def get_book():
    data = {
        'book_name':'all'
    }
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    response = r.json()
    for r in response:
        print(r['book_name'])

URL2 = 'http://127.0.0.1:8000/library_back/add_book'
def add_book():
    data = {
        'book_name':'David Copperfield',
        'book_author':'Charles Dickens'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL2, data = json_data)
    response = r.json()
    print(response)
# add_book()
URL3 = 'http://127.0.0.1:8000/library_back/put_data_complete'
def put_data_complete():
    data = {
        'book_name':'David Copperfield',
        'book_author':'Charles Dickens',
        'is_issued':False,
        'issued_to':None
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL3, data = json_data)
    response = r.json()
    print(response)
# put_data_complete()

URL4 = 'http://127.0.0.1:8000/library_back/put_data_partial'
def put_data_partial():
    data = {
        'book_name':'test3',
        'book_author':'test_author',
        'is_issued':True,
        'issued_to':None,
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL4, data = json_data)
    response = r.json()
    print(response)
URL5 = 'http://127.0.0.1:8000/library_back/delete_data'
def delete_data():
    data = {
        'book_name':'ifeuvbdiouiefh'
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL5, data = json_data)
    response = r.json()
    print(response)
delete_data()
    




