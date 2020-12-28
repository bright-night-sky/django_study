# 5.3.7 URL 연결
# 뷰를 동작시키기 위해서는 URL 연결을 해야한다.
# photo 앱 폴더에 urls.py 파일을 만들고 뷰에 URL을 연결해보자.

# 다른 뷰를 연결하는 방법은 지난 장에서 다른 뷰를 연결하는 방법을 사용했다.
# 함수형 뷰는 이름만 써주고 클래스형 뷰는 뒤에 .as_view()를 붙인다.
# 이번 장에서 작성한 urls.py에서는 챙겨봐야할 부분이 두 가지이다.
# 바로 app_name이라는 변수와 제네릭 뷰를 그대로 사용하는 인라인 뷰이다.

from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

# 우선 app_name은 네임스페이스(namespace)로 사용되는 값이다.
# 템플릿에서 url 템플릿 태그를 사용할 때 app_name 값이 설정되어 있다면 [app_name:URL패턴이름] 형태로 사용한다.
app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    # 제네릭 뷰인 DetailView는 views.py가 아닌 urls.py에서 인라인 코드로 작성할 수 있다.
    # path 함수에 인수로 전달할 때는 as_view 안에 클래스 변수들을 설정해 사용한다.
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]

# 뷰의 URL들은 다 설정했으니 이제 루트 urls.py에 앱의 urls.py를 연결해주겠다.
# config/urls.py로 이동