from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from django.utils.datastructures import MultiValueDictKeyError
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
    
    # username = request.GET['username']
    # password = request.GET['password']
    context = {
        'method': request.method,
        'is_valid': True
    }
    
    
    if (request.method == 'GET'):
        # 이하 주석 처리된 부분은 삭제해도 되는 부분
        # # username과 password에 대한 입력이 없다면
        # if username is None and password is None: # users/login
        #     # return HttpResponse('로그인 화면입니다.')
        #     return render(request, 'users/login.html')
        # # username과 password중 하나의 입력이 누락되었을 때
        # elif username is None or password is None:
        #     return HttpResponse('불가능한 접근입니다.')
        return render(request, 'users/login.html', context)
    
    if (request.method == 'POST'):
        # username, password = None, None
        # try:
            # username = request.GET['username'] # .GET['username']: key가 없을 경우 keyerror를 띄운다.
            # password = request.GET['password']
        # except MultiValueDictKeyError:
            # if username is None:
            #     return HttpResponse('유저 아이디를 입력해주세요')
            # if password is None:
            #     return HttpResponse('유저 비밀번호를 입력해주세요')
            
        username = request.POST.get('username') # .get('username'): key가 없으면 none을 반환한다.
        password = request.POST.get('password')
        # if username is None:
        #     return HttpResponse('유저 아이디를 입력해주세요')
        # if password is None:
        #     return HttpResponse('유저 비밀번호를 입력해주세요')
        
        #blank 상태일 때는 유저가 input을 입력하지 않고 제출했을 때(유저의 실수)
        if username == '':
            # return HttpResponse('유저 아이디를 입력해주세요')
            context['is_valid'] = False
        if password == '':
            # return HttpResponse('유저 비밀번호를 입력해주세요')
            context['is_valid'] = False
        
        if (username != user_data['username']):
            # return HttpResponse('유저 아이디가 올바르지 않습니다.')
            context['is_valid'] = False
        if (password != user_data['password']):
            # return HttpResponse('유저 비밀번호가 올바르지 않습니다.')
            context['is_valid'] = False
        # return render(request, 'users/login.html')
    
        if context['is_valid']:
            # return redirect('pages:index')
            response = redirect('pages:index')
            
            response.set_cookie('username', user_data['username'])
            response.set_cookie('password', user_data['password'])
            response.set_cookie('is_login', True)
            
            return response
        # return HttpResponse('로그인 성공!!')
        return render(request, 'users/login.html', context)
    return HttpResponse()

def login_detail(request, id):
    return HttpResponse('user id는 ' + str(id) + '입니다.')

def index(request,):
    return render(request, 'index.html')