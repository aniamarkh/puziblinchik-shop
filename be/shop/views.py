from django.shortcuts import render
from django.http import JsonResponse
from .models import Merch, Category


def merch(request):
    return JsonResponse({
        'response': [{
            'name': m.name,
            'description': m.description,
            'date': m.date,
            'stock': m.stock,
            'category': {
                'id': m.category.id,
                'name': m.category.name
            },
        } for m in Merch.objects.all()]
    })


def categories(request):
    return JsonResponse({
        'response': [{
            'name': c.name,
            'description': c.description
        } for c in Category.objects.all()]
    })
