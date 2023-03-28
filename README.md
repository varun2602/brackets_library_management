# Library Management Project

## Overview

This is a library management project where a librarian can create a book entry, retrieve one or all books, update any entry info or delete a book entry. The project is based on RESTful APIs using Django rest framework, and consists of two independent applications - one for backend and one for frontend. These two applications interact with each other only through APIs created for the project. All CRUD operations are performed through these APIs.

## Distinctiveness and Complexity

The most distinctive feature of this project is that it's based on RESTful APIs using Django rest framework. In this project, the database and application are separate and can even be located in different servers miles apart, yet still interact perfectly well. This provides a lot of flexibility in terms of development and management.

Creating APIs using serializers from rest framework, extracting JSON data from the request, streaming it, converting it to Python data, and serializing it for appropriate use was a complex task. I also created a separate application with its own front end and back end, and connected it to the API to send requests gets pretty complex. Additionally, I implemented API related error checking, tested whether they work or not, and directed the responses to the user's front end. 

In the registration process, I created a JS code to check instantaneously whether the username is available or not. I also used JS to interact with the middle layer and backend in the add books page. In other cases, I interacted with the backend through HTML along with learning how to implement register and login routes.

## What's Contained in Each File Created

I created two applications, library and library_front, in the project called "lm". The "library" app contains an additional "serializers.py" apart from general Django files where I created a serializer function. The "library_front" app is a library management app where a librarian can create, retrieve one book, retrieve all books, update a book and delete a book. It contains a "templates" folder where all essential templates are stored and a "static" folder where JS code is stored along with general files that Django provides.

## How to Run the Application

To run the application, simply run the migrations and "python manage.py runserver". Open the link and the application will begin.

## Additional Information that staff should know

Staff will have to install Django Rest Framework since it does not come with Django. I have handled the remaining process of installing it and utilizing packages inside it.

