from django.contrib import admin

from .models import Bookmark

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
admin.site.register(Bookmark)
# 등록했으니 서버를 키고 관리자 페이지에서 확인해보자.
# 어노테이션을 이용해서 등록하는 방법도 있다.