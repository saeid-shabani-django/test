from django.shortcuts import render

def show_deb(request,name):
    a = 3
    b = a * 2
    return render(request,'newdeb/hello.html',{'name':name,
                                               'b':b})