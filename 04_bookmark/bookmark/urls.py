from django.urls import path
from .views import *

urlpatterns = [
    # path의 첫 번째 인수는 ''를 보면 bookmark/ 이하 부분이 없다라고 해석할 수 있다.
    # 그럼 북마크 앱의 루트 페이지 같은 역할을 한다고 생각하면 된다.
    # 이런 주소로 접속했을 때 BookmarkListView라는 뷰를 호출하겠다라는 의미이다.
    # 함수형 뷰라면 이름만 써주면 되지만 클래스형 뷰일 경우 .as_view()라고 꼭 붙여줘야 정상적으로 동작한다.
    # 마지막 인자인 name은 설정한 이름을 가지고 해당 URL 패턴을 찾을 수 있도록 하는 역할을 한다.

    # http://127.0.0.1/bookmark/???
    # 앞의 bookmark까지는 1차에서 다 인식하고 왔다.
    # 밑의 주소는 http://127.0.0.1/bookmark/이다.
    # .as_view()는 클래스형 뷰를 함수형 뷰로 내부적으로 바꿔주는 처리를 하는 것이다.
    # 클래스형 뷰를 사용할 경우 꼭 붙여야한다.
    # name= 은 템플릿에서 이 URL을 어떻게 불러다가 쓸 것인지 정하는 이름이다.
    # 즉 URL 패턴의 이름이다.
    # 파일을 새로 만들어서 수정한 경우 서버 자체를 껐다가 다시 켜줘야한다.
    path('', BookmarkListView.as_view(), name='list'),
    # 오류 페이지에 나오는 오류 메시지들은 꼭 확인하고 공부하자.

    # urlpatterns 변수에 path를 하나 더 추가해 BookmarkCreateView를 연결한다.
    # 이 뷰를 사용하기 위해서 당연히 임포트를 미리 해야한다.
    path('add/', BookmarkCreateView.as_view(), name='add'),
    # URL을 연결했으니 템플릿도 만들자.
    # bookmark/templates/bookmark에 bookmark_create.html 파일 생성하기

    # urls.py에 path를 추가하고 BookmarkDetailView를 연결한다.
    # URL 패턴은 다른 뷰들과 차이를 보인다. 바로 [<int:pk>]가 들어간 부분이다.
    # 이 부분은 두 개의 값이 의미하는 바바 각각 있다.
    # 앞쪽인 int는 타입이라고 여기면 된다.
    # 정확히는 컨버터라고 부르는 기능이며 클래스 형태이다.
    # 뒤쪽은 컨버터를 통해 반환받은 값 혹은 패턴에 일치하는 값의 변수명이다.
    # 컨버터는 생략하거나 커스텀 컨버터를 만들어 넣을 수 있다.
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    # <pk>와 같이 그냥 비워두면 문자열로 인식한다.
    # 기본으로 제공되는 컨버터는 다음과 같다.
    #   1. str : 비어있지 않은 모든 문자와 매칭. 단 '/'는 제외. 컨버터를 설정하지 않을 경우 기본 컨버터
    #   2. int : 0을 포함한 양의 정수와 매칭
    #   3. slug : 아스키 문자나 숫자, 하이픈, 언더스코어를 포함한 슬러그 문자열과 매칭. 쇼핑몰에서 많이 쓴다.
    #   4. uuid : UUID와 매칭. 같은 페이지에 여러 URL이 연결되는 것을 막으려고 사용
    #   5. path : 기본적으로 str과 같은 기능이나 '/'도 포함. URL의 부분이 아닌 전체에 대한 매칭을 하고 싶을 때 사용

    # URL 연결이 끝았으면 템플릿도 작성하자. bookmark_detail.html 파일을 만들고 코드를 작성하자.

    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    # 마지막은 템플릿이다. bookmark_update.html을 bookmark_create.html의 내용과 똑같이 만들고 버튼의 값만 Update로 변경하자.

    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]