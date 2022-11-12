from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# import json
# Create your views here.

# def login(request: HttpRequest):
#     data = json.dumps(request.GET) # dictionary를 문자열로 바꿔주는 처리가 필요함
#     return HttpResponse(data)

def login(request):
    user_data = {
        'username': 'python',
        'password': 'django' 
    }
    
    if (request.method == 'GET'):
        username = request.GET['username']
        password = request.GET['password']
        
        if (username != user_data['username']):
            return HttpResponse('유저 아이디가 올바르지 않습니다.')
        
        if (password != user_data['password']):
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')
        
        return HttpResponse('로그인 성공!!')

def login_detail(request, id):
    return HttpResponse('user id는 ' + str(id) + '입니다.')