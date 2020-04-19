from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage



def index(request):
    # return HttpResponse("Hello world")
    webpage_list=AccessRecord.objects.order_by('date')
    date_dic={'access_record':webpage_list}
    return render(request,"index.html",context=date_dic)



# Create your views here.
