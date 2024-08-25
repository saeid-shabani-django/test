from django.shortcuts import render

def show_deb(request,id):
    a = 2
    b = 2 * 4
    return render(request,'deb/hello.html',{'name':id,'b':b})




