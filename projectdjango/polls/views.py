from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def divbyzero(func):
#     def inner(x, y):
#         if y == 0:
#             return 'qty is zero'
#         return func(x, y)
#     return inner


# @divbyzero
# def unitprice(amount, qty):
#     return amount / qty

# print(unitprice(500, 0))
# print(unitprice(500, 10))


def index(request):
    return HttpResponse("message: Hello, world. You're at the polls index.")
