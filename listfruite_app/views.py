from django.shortcuts import render
 #Create a new view function that will handle the request and render the date and time:
from django.shortcuts import render
def home(request):
 fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Pineapple']
 students = ['John', 'Jane', 'Mike', 'Sarah', 'Tom']
 context = {
 'fruits': fruits,
 'students': students,
 }
 return render(request, 'home.html', context)

