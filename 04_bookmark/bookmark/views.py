from django.shortcuts import render
from django.views.generic.list import ListView
# 윈도우에서는 Ctrl, 맥에서는 cmd를 누르고 ListView를 클릭해보면 안의 소스코드를 볼 수 있다.
# 실력 향상을 하고 싶으면 안의 소스코드를 봐라

# 북마크 추가 기능 구현시 필요한 import문
# views.py 파일에서 CreateView 옆에 UpdateView를 임포트한다.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# 북마크 확인 기능 구현시 필요한 import문
from django.views.generic.detail import DetailView

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

    # 페이징 기능 만들기
    # 페이징 기능은 게시판 같은 서비스에서는 필수이다.
    # 함수형 뷰에서는 페이징 기능을 만들기 위해서 여러가지 일을 해야하지만 클래스형 뷰에서는 간단하게 구현할 수 있다.
    # views.py에 있는 BookmarkListview에 paginate_by = 6이라는 코드를 추가하자.
    # 한 페이지에 몇 개씩 출력할 것인지 결정하는 값이다.
    # 그리고 북마크가 6개가 넘도록 몇 개 더 추가해보자.
    paginate_by = 6
    # 이제 목록 아래쪽에 페이지 목록을 출력해서 페이징 기능을 사용할 수 있도록 만들어보자.
    # bookmark_list.html을 수정하자.

# 이번 앱에서는 모든 뷰를 클래스형 뷰로 만들 것이다.
# 뷰에는 함수형 뷰와 클래스형 뷰가 있다.
# 클래스형 뷰는 웹 프로그래밍에서 자주 사용하는 기능을 장고가 미리 준비해뒀고 그걸 빌려다 쓰는 형태라고 했다.
# 북마크 앱은 전형적인 뷰들이 필요하기 때문에 클래스형 뷰가 적절하다.

# 목록 뷰는 BookmarkListView라는 이름으로 클래스형 뷰를 만드는데, ListView를 상속해 사용한다.
# 그리고 model을 설정해줘야하기 때문에 Bookmark 모델을 임포트하고 클래스 안에 model = Bookmark라는 구문을 이용해 모델을 설정한다.

# 웹 페이지에 접속한다. : 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답을 한다.
# config/urls.py로 이동

# 북마크 추가 기능 구현
# 북마크 추가를 위한 뷰를 BookmarkCreateView라는 이름을 가진 클래스 뷰로 만든다.
# 클래스형 뷰가 만들기 훨씬 더 간편하다. 미리 준비되어 있기 때문에
# 제네릭 뷰인 CreateView를 상속받으면 쉽게 만들 수 있다.
class BookmarkCreateView(CreateView):
    # 어떤 모델의 입력을 받을 것인지 결정해야 하기 때문에 ListView와 마찬가지로 model 변수를 만들고 Bookmark로 설정한다.
    model = Bookmark
    # fields 변수는 어떤 필드들을 입력받을 것인지 설정하는 부분이다.
    # CreateView와 UpdateView는 fields를 설정하지 않으면 오류가 뜬다. 무조건 필요하다.
    fields = ['site_name', 'url']
    # success_url은 글쓰기를 완료하고 이동할 페이지이다.
    # 보통은 상세 페이지로 이동하지만 success_url의 사용법을 알기 위해 상세 페이지로 설정해봤다.
    success_url = reverse_lazy('list')
    # template_name_suffix는 사용할 템플릿의 접미사만 변경하는 설정값이다.
    # 기본으로 설정되어 있는 템플릿 이름들은 모델명_xxx 형태이다.
    # CreateView와 UpdateView는 form이 접미사인데(bookmark_form), 이걸 변경해서 bookmark_create라는 이름의 템플릿 파일을 사용하도록 설정한 것이다.
    template_name_suffix = '_create'
    # 뷰를 완성했으니 URL을 연결하자.
    # bookmark/urls.py로 이동


# 북마크 확인 기능 구현
# 추가 기능을 구현했으니 북마크의 확인 기능을 구현해보자.
# 상세 페이지라고도 할 수 있는 이 기능도 클래스형 뷰를 사용해 간단히 만들겠다.
# views.py에 BookmarkDetailView를 만든다.
# 다른 뷰들과 마찬가지로 제네릭 뷰인 DetailView를 상속받도록 한다.
# model까지 Bookmark로 설정하면 확인 뷰 작성은 끝이다.
# URL만 연결해주면 뷰는 제대로 동작한다.
class BookmarkDetailView(DetailView):
    model = Bookmark


# 북마크 수정 기능 구현
# 수정 기능은 추가 기능과 거의 동일하다.
# 제네릭 뷰를 사용해서 수정 뷰를 추가하겠다.
# 임포트한 UpdateView를 상속받도록 BookmarkUpdateView를 만든다.
class BookmarkUpdateView(UpdateView):
    # 모델을 설정하고
    model = Bookmark
    # 추가 뷰처럼 입력받을 필드 목록을 설정한다.
    fields = ['site_name', 'url']
    # 그리고 이번에는 템플릿 접미사를 _update로 했다.
    # 그럼 bookmark_update.html이 템플릿이 된다는 뜻이다.
    template_name_suffix = '_update'
    # 수정이 완료된 이동할 페이지는 뷰에 success_url이 설정되어 있거나 모델에 get_absolute_url이라는 메서드를 통해 결정한다.
    # 그런데 우리는 두 가지 모두 없기 때문에 오류를 만난 것이다.
# 뷰 다음은 URL 연결이다.
# urls.py 파일에 새로운 path를 추가해 update라는 이름으로 뷰를 연결한다.
# bookmark/urls.py로 이동

# 북마크 삭제 기능 구현
# 북마크 삭제 기능도 제네릭 뷰를 상속받아 구현하겠다.
# views.py에 DeleteView를 임포트하고 BookmarkDeleteView를 만든다.
class BookmarkDeleteView(DeleteView):
    # 모델은 Bookmark로 하고,
    model = Bookmark
    # success_url은 목록 페이지로 가도록 reverse_lazy를 사용해 설정한다.
    # 삭제하면 어디론가 가야되므로
    # 다만 get_abolute_url은 사용할 수 없다.
    # 클래스형 뷰에서는 reverse가 아닌 무조건 reverse_lazy를 사용해야한다.
    # 왜냐하면 라우팅 테이블이 다 불러지지 않은 상태에서 클래스형 뷰를 먼저 점검하므로 그때 오류가 발생할 수 있기 때문이다.
    success_url = reverse_lazy('list')
# 뷰를 만들고 나면 urls.py에 새로 path를 추가해 BookmarkDeleteView를 연결한다.

