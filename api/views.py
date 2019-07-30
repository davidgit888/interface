from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy
from datetime import datetime
import json
import requests
from pyzbar import pyzbar
# from PIL import Image

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
@api_view(http_method_names=['post'])        #只允许post
@permission_classes((permissions.AllowAny,))
def inventory(request):
    parameter = request.data
    data = parameter['image']
  
    return Response({'data':data})

@csrf_exempt
def images(request):
    # return HttpResponse("oh my god")
    with open("api/log.txt","a+") as f:
        f.write('\r\nbegin time %s \r' % datetime.now())
        key = 'AXLBZ-O5IL3-GTM3T-3FBKS-CXSVZ-FVF4X'
        try:
            lat = request.POST.get('lat')
            log = request.POST.get('log')
            url = 'https://apis.map.qq.com/ws/geocoder/v1/?location='+lat+','+log+'&key='+key+'&get_poi=1'
            a = requests.get(url)
            results = json.loads(a.text)
            location = results['result']['address']
        except Exception as ex:
            location = '无法获取位置信息'
        try:
            # pic = request.FILES['file']
            im_pic = cv2.imdecode(numpy.fromstring(request.FILES['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
            # im_bar = cv2.imread(request.FILES['file'],0)
            try:
                barcode = pyzbar.decode(im_pic)
                url = barcode[0].data.decode('utf-8')
            except:
                pass
            # image = cv2.imread(file)
            # im_pic = Image.open(pic)
            img2gray = cv2.cvtColor(im_pic, cv2.COLOR_BGR2GRAY)
            # w, h = im_pic.size
            imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
            # return Response({'data':'image found'})
            # abc = type(file)
            # abc = str(abc)
            if imageVar > 300:
                f.write("clear"+location + ',url is: '+url)
                return HttpResponse('图片清晰'+str(imageVar) + "位置是：" +location)
            else:
                f.write("unclear"+location + ',url is: '+url)
                return HttpResponse('图片不清晰，请再上传一次'+str(imageVar) + "位置是：" + location)
        except KeyError:
            # return Response({'data':'not found'})
            f.write("no image")
            return HttpResponse('没有上传图片')
    
        
