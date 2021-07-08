from django.shortcuts import render
from django.views import View
from django.conf import settings 
import requests
import json


# Create your views here.


class HomeView(View):
    template_name='index.html'

    def get(self,request, *args, **kwargs):
        endpoint = 'https://hub.aatgroup.uz/api/login'
        params = {
            "username": settings.AATGROUP_HOST_USERNAME,
            "password": settings.AATGROUP_HOST_PASSWORD,
            "currency": "USD"
        }
        response = requests.post(endpoint, params=params)

        if 'json' in response.headers.get('Content-Type'):
            r_json = response.json()
        else:
            print('Response content is not in JSON format.')
            print("Status Code: ", response.status_code)
            r_json = None
    
        print(r_json)

        context={'agent': None, 'price': None, 'feedback': None }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            agent    = request.POST.get('agent')
            feedback = request.POST.get('feedback')
            price    = request.POST.get('price')
            print(agent, feedback, price)
        context={'agent': agent, 'price': price, 'feedback': feedback }
        return render(request, self.template_name, context)


