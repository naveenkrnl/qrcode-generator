from django.shortcuts import render
import pyqrcode
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):



    if request.method == 'GET': # If the form is submitted

        data = request.GET.get('search_box', None)
        if data:
            a = pyqrcode.create(data)
            a.png(os.path.join(BASE_DIR, 'qrcode/static_proj/img/qr.png'),scale=7)


            # print(a.terminal(quiet_zone=0))
            return render(request, 'qr/result.html')
    return render (request, 'qr/index.html')






