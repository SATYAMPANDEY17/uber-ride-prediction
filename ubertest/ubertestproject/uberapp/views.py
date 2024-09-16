from django.shortcuts import render
import os
import pickle

# Create your views here.
def index(request):
    if request.method=="POST":
        ppw=int(request.POST['ppw'])
        pn=int(request.POST['pn'])
        mi=int(request.POST['mi'])
        appm=int(request.POST['appm'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'taxi.pkl'),'rb'))
        res=str(model.predict([[ppw,pn,mi,appm]])[0].round(2))
        context={'res':res}
    return render(request,"index.html",locals())