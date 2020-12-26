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
from django.urls import path, include

urlpatterns = [
    # URL 연결하기
    # 뷰를 만들었으면 어떤 주소를 사용해 이 뷰를 호출할 수 있도록 연결해야 한다.
    # 다시 말하면 어떤 주소를 입력했을 때 해당 페이지를 보여주고 싶은가를 설정하는 것이다.
    # 이 설정은 urls.py 파일에 한다.

    # urls.py 파일은 config 폴더에 있는 루트 파일과 각 앱 폴더에 만들어 두는 서브 파일들이 있다.
    # 루트 urls.py 파일만 있어도 무방하지만 한번 만든 앱은 다른 프로젝트에도 재사용할 수 있기 때문에 앱에 관한 URL 연결은 앱 폴더에 있는 urls.py에 설정한다.

    # 그리고 앱에 관한 urls.py의 내용은 루트 파일에서 연결해줘야만 동작을 한다.
    # 루트 urls.py 파일을 열고 include 함수를 임포트하고 urlpatterns에 bookmark.urls를 연결하는 path를 추가한다.

    # 대학병원에서 외과에 문진을 가야하는 경우, 바로 외과에 가는게 아니라 접수 중앙 로비에 접수하고 거기서 간호사와 직원분이 안내를 1차로 해준다.
    # 그리고 외과에 가면 2차로 간호사 접수를 또 해준다.
    # 위의 예처럼 url 동작방식도 같다.
    # 1차 -> 2차 -> 3차
    # http://127.0.0.1/bookmark/?
    # http://127.0.0.1/중앙창구/외과
    # http://127.0.0.1/중앙창구/내과
    # 주소 설계가 필요하다.
    # 여기서 1차 URL을 설계해준것이다.
    path('bookmark/', include('bookmark.urls')), # 슬래쉬 꼭 붙여야한다.
    # 이렇게 연결을 하면 http://127.0.0.1:8000/bookmark/[이하 URL] 같은 주소로 접속하면 bookmark/까지의 URL을 잘라내고 나머지 부분을 bookmark.urls로 전달해 찾아본다.
    # 나머지 부분을 가지고 어떤 뷰를 연결할지를 bookmark 앱 폴더에 있는 urls.py에 작성하도록 하자.
    # 아직까지는 bookmark 앱 폴더에 urls.py가 없으므로 새로 파일을 만들어 주자.
    # http://127.0.0.1/admin/
    path('admin/', admin.site.urls),
]
