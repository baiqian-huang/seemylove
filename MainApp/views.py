from django.shortcuts import render,HttpResponse
from .models import Datas
import json

# Create your views here.

def index(request):
    return render(request, "index.html", {"href":"http://www.baidu.com"})


def getdata(request):

    if request.method == "GET":
        flag = request.GET.get("get")
        print(flag)
        datas = Datas.objects.all()
        data = {}
        for objs in datas:
            data[objs.id] = [objs.url, objs.poster,objs.zhujue]
        print(data)
        return HttpResponse(json.dumps({
            "status":"success",
            "lenth":len(data.keys()),
            "data":data,
        }))
