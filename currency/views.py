from django.shortcuts import render
import requests
from django.views.generic.base import TemplateView
from django.http import JsonResponse ,HttpResponse

class CurrencyConverter(TemplateView):

    rates = {} 
    template_name = 'currency.html'

    def __init__(self,**kwargs):
        
        req = requests.get('http://data.fixer.io/api/latest?access_key=731d6a196c79112c3c971c183c4d804d')
        data = req.json()
        #print("@@@@@@@@@@@@@2",data)
        self.rates = data['rates']
        print('######################',self.rates)


    def post(self, request,*args,**kwargs):
        currency_1 = request.POST['from_currency']
        currency_2 = request.POST['to_currency']
        amount = float(request.POST['amount'])
        to_amount = self.convert(amount,currency_1,currency_2)
        return render(request,'currency.html',{'amount':to_amount})

        
    def convert(self,amount,from_currency,to_currency):

        initial_amount = amount

        if from_currency != 'EUR':
            print("amount before",amount)
            print("fromcurrency rate",self.rates[from_currency])
            amount = amount/self.rates[from_currency]
            print("AMOUNT AFTER",amount)

        if to_currency == 'EUR':
            return amount*self.rates[from_currency]
        else:
            return amount*self.rates[to_currency]


