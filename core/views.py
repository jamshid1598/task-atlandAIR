from django.shortcuts import render
from django.views import View



# Create your views here.


class HomeView(View):
    template_name='index.html'
    def get(self,request, *args, **kwargs):
        context={'agent': 'agent', 'price': 'price', 'feedback': 'feedback' }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            agent    = request.POST.get('agent')
            feedback = request.POST.get('feedback')
            price    = request.POST.get('proce')
            print(agent, feedback, price)
        context={'agent': agent, 'price': price, 'feedback': feedback }
        return render(request, self.template_name, context)


