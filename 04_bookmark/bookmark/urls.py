from django.urls import path
from .views import BookmarkListView

urlpatterns = [
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
]