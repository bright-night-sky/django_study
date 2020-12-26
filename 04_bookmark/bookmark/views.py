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
class BookmarkListView(ListView):
    model = Bookmark

# 웹 페이지에 접속한다. : 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답을 한다.
