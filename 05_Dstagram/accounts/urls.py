# 5.4.2 로그인, 로그아웃 기능 추가
# 로그인, 로그아웃 기능은 장고에 이미 만들어져있는 기능이다.
# 이 기능을 그대로 불러다 쓰기 위해서 accounts 앱 폴더에 urls.py를 만들고 기존에 있는 뷰를 불러다가 사용하자.

from django.urls import path
from django.contrib.auth import views as auth_view

from .views import register

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # register 뷰를 임포트하고 path를 새로 추가하여 register 뷰를 연결한다.
    path('register/', register, name='register'),
    # 그리고 회원가입 페이지를 위한 템플릿을 작성한다.
    # accounts/templates/registration/register.html로
]

# 이 urls.py를 사용하기 위해 루트 urls.py에 연결한다.
# config/urls.py로 이동