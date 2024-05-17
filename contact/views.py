from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def contact_form(request):
    context = {'success': False,
                'message': 'Contact form sent successfuly.'
               }

    return JsonResponse(context)
def contact(request):
    return render(request, 'contact.html')
