from django.http.response import JsonResponse
from django.shortcuts import HttpResponse, redirect, render

def root(request):
  return redirect("/blogs")

def index(request):
  return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
  return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
  return redirect("/")

def show(request, number):
  print(f'========> /blogs/{number}')
  return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
  print(f'========> /blogs/{number}/edit')
  return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request, number):
  print(f'========> /blogs/{number}/delete')
  return HttpResponse(f'will delete blog {number}')

def json_method(request):
  print(f'========> /json')
  return JsonResponse({"title": "some title", "keys" : "some content keys?"})


