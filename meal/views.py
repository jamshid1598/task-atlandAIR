from django.shortcuts import render
from django.views import View

import requests

from .models import Meal


# Create your views here.

class HomeView(View):
    template_name='meal/index.html'
    def get(self, request, *args, **kwargs):
        object_list = Meal.objects.all().order_by('-id')
        context={'object_list': object_list, }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        query = None
        if 'q' in request.POST:
            query = request.POST.get('q')
            endpoint='https://www.themealdb.com/api/json/v1/1/search.php?s=%s' % query
            response = requests.get(endpoint)

        if 'json' in response.headers.get('Content-Type'):
            data=response.json()
            obj_list = data['meals']
            if obj_list != None:
                print(obj_list)
                for obj in obj_list:
                    if Meal.objects.filter(slug=obj['idMeal']).exists():
                        new_instance = Meal(
                            name        = obj['strMeal'],
                            category    = obj['strCategory'],
                            instruction = obj['strInstructions'],
                            region      = obj['strArea'],
                            slug        = obj['idMeal'],
                            image       = obj['strMealThumb']
                        )
                        new_instance.save()
        object_list = Meal.objects.all().order_by('-id')

        context={'object_list': object_list, }
        return render(request, self.template_name, context)


class DetailView(View):
    template_name=''
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, self.template_name, context)