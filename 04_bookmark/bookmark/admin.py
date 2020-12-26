# 관리자 페이지에 모델 등록
# 모델을 이용한 데이터 작업을 하려면 뷰를 만들어야 한다.
# 하지만 뷰를 만들기 위해서는 시간이 걸린다.
# 또 뷰를 만들면서 확인하는 작업을 할 때 미리 입력된 데이터가 필요하기도 하다.
# 그래서 관리자 페이지에 미리 모델을 관리할 수 있도록 등록해두면 편리하다.

# admin.py는 모델을 관리자 페이지에 등록해 관리할 수 있도록 하는 역할과 관리자 페이지에서 보이는 내용의 변경, 기능 추가 등을 할 수 있도록 코드를 입력하는 파일이다.

from django.contrib import admin

# from .models import Bookmark 구문은 현재 폴더에 있는 models.py 파일에서 Bookmark라는 모델을 불러오겠다라는 의미이다.
# 이렇게 불러온 모델을 admin.site.register 구문을 이용해 등록하면 관리자 페이지에서 해당 모델을 관리할 수 있다.
from .models import Bookmark

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
admin.site.register(Bookmark)
# 등록했으니 서버를 키고 관리자 페이지에서 확인해보자.
# 어노테이션을 이용해서 등록하는 방법도 있다.