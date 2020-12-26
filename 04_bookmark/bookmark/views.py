from django.shortcuts import render
from django.views.generic.list import ListView
# 윈도우에서는 Ctrl, 맥에서는 cmd를 누르고 ListView를 클릭해보면 안의 소스코드를 볼 수 있다.
# 실력 향상을 하고 싶으면 안의 소스코드를 봐라

from bookmark.models import Bookmark

# Create your views here.
# CRUD : Create, Read, Update, Delete
# CRUD는 기본적으로 할 줄 알아야 개발을 할 수 있다.
# List

# 클래스형 뷰, 함수형 뷰 두 종류 존재

# 클래스형 뷰는 쉽게 만들 수 있다.
# 목록 뷰 만들기
# 관리자 페이지를 이용해 모델을 관리할 수 있지만 제대로 된 서비스를 만들기 위해서는 프론트에서 해당 기능을 사용할 수 있어야 한다.
# 이러한 기능들을 뷰(view)라고 부르는데 보통은 views.py에 만든다.
class BookmarkListView(ListView):
    model = Bookmark

# 이번 앱에서는 모든 뷰를 클래스형 뷰로 만들 것이다.
# 뷰에는 함수형 뷰와 클래스형 뷰가 있다.
# 클래스형 뷰는 웹 프로그래밍에서 자주 사용하는 기능을 장고가 미리 준비해뒀고 그걸 빌려다 쓰는 형태라고 했다.
# 북마크 앱은 전형적인 뷰들이 필요하기 때문에 클래스형 뷰가 적절하다.

# 목록 뷰는 BookmarkListView라는 이름으로 클래스형 뷰를 만드는데, ListView를 상속해 사용한다.
# 그리고 model을 설정해줘야하기 때문에 Bookmark 모델을 임포트하고 클래스 안에 model = Bookmark라는 구문을 이용해 모델을 설정한다.

# 웹 페이지에 접속한다. : 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답을 한다.
# config/urls.py로 이동
