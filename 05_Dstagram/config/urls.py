"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# include를 임포트하고
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path를 하나 추가해 photo.urls를 연결해준다.
    # 이 때 URL 패턴을 ''로 설정하면 photo 앱이 메인 페이지로 동작한다.
    path('', include('photo.urls')),
    # 로그인, 로그아웃용 url
    path('accounts/', include('accounts.urls')),
    # 이제 로그인, 로그아웃 기능은 동작할 것이다. 템플릿을 만들고 마무리하겠다.
    # accounts/templates/registration/login.html로 이동
]
# 5.3.8 템플릿 분리와 확장 -> base.html로 이동

# 5.3.9 사진 표시하기
# 기본 뷰는 다 완성했다. 하지만 사진이 제대로 출력되지 않는다.
# 사진을 출력하기 위해서는 몇 줄의 코드를 더 입력해야 한다.
# config 폴더의 루트 urls.py를 수정하자.
# static을 사용해서 MEDIA_URL에 해당하는 주소를 가진 요청에 대해서는 MEDIA_ROOT에서 찾아서 응답하도록 urlpatterns에 추가하는 구문이다.
# 이 구문은 디버그 모드가 True일 때만 동작한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)