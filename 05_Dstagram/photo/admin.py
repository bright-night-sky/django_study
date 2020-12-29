# 5.3.3 관리자 사이트에 모델 등록
# 관리자 사이트에 모델을 등록하면 모델을 관리하는 뷰를 만들기 전에도 모델을 테스트해볼 수 있다.
# admin.py 파일을 수정해 Photo 모델을 등록한다.

# 5.3.5 관리자 페이지 커스터마이징
# 업로드 후에 관리자 사이트에서 사진 목록을 확인해보자.
# 보기 편한 형태는 아니다.
# admin.py 파일을 수정해서 목록을 보기 좋게 바꾸자.

from django.contrib import admin

from .models import Photo

# Register your models here.
# admin.py에 PhotoAdmin이라는 옵션 클래스를 만든다.
# 이름은 마음대로 해도 되지만 보통 [모델명Admin]으로 한다.
# 이 클래스는 admin.ModelAdmin 클래스를 상속받는다.
# PhotoAdmin 클래스에는 관리자 사이트에서 보이는 목록 화면을 커스터마이징할 수 있는 옵션을 설정한다.
#   1. list_display : 목록에 보일 필드를 설정한다.
#                     모델의 필드를 선택하거나 별도 함수를 만들어 필드처럼 등록할 수 있다.
#   2. raw_id_fields : ForeignKey 필드의 경우 연결된 모델의 객체 목록을 출력하고 선택해야 하는데 목록이 너무 길 경우 불편해진다.
#                      이런 경우 raw_id_fields로 설정하면 값을 써넣는 형태로 바뀌고 검색 기능을 사용해 선택할 수 있게 된다.
#                      raw_id_fields로 하지 않으면 사진 등록 시 author에 회원들이 리스트 박스로 쭉 나열되게 되는데 회원이 수만명 되면 찾기가 매우 어려워진다.
#                      그래서 raw_id_fields를 사용하는 것이다.
#                      ForeignKey 필드 같은 경우 보통 raw_id_fields로 해놓는 것이 좋다.
#   3. list_filter : 필터 기능을 사용할 필드를 선택한다.
#                    장고가 적절하게 필터 범위를 출력해준다.
#                    실무에서 필터는 보통 기간, 시간에 많이 걸게 된다.
#   4. search_fields : 검색 기능을 통해 검색할 필드를 선택한다.
#                      ForeignKey 필드는 설정할 수 없다.
#                      search_fields는 ORM 클래스의 icontains 메서드를 이용해 검색하는데 이는 문자열만 된다.
#                      그런데 ForeignKey는 객체라서 설정할 수 없다.
#                      author는 ForeignKey라서 설정할 수 없는데 작성자로도 검색하고 싶으면 'author__username'을 넣으면 된다.
#                      ORM 공부를 깊게 하면 알 수 있게 된다.
#   5. ordering : 모델의 기본 정렬값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값을 설정한다.
class PhotoAdmin(admin.ModelAdmin):
    # id는 자동으로 만들어지는 필드이다.
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created', 'author__username']
    ordering = ['-updated', '-created']

# 밑의 코드 한 줄 추가
# 관리자 사이트를 커스터마이징하는 클래스를 작성했으면 register 안에 넣어줘야한다.
admin.site.register(Photo, PhotoAdmin)

# admin.site.register() 말고도 어노테이션(데코레이터)로도 관리자 사이트에 모델을 등록할 수 있다.

# 모델을 등록했으니 사진을 업로드 해보자.
# python manage.py runserver 로 서버를 실행하고 관리자 페이지에 접속한다.

# 관리자 페이지에는 이미 Photo 모델이 등록되어 있다.
# [Add] 버튼을 클릭해 추가 화면으로 이동해 원하는 사진을 업로드한다.
# Author는 작성자인데 현 시점에는 관리자 계정만 있으므로 관리자 계정을 선택한다.
# 필드 값들을 다 채우고 [SAVE] 버튼을 누르고 업로드가 된다.
# 파이참으로 돌아와서 업로드 된 파일을 확인해보자.

# 업로드된 파일은 photos 폴더 밑에 업로드 년/월/일 순으로 폴더를 만들고 그 안에 저장되어 있다.
# 업로드는 잘 된 것 같지만 생각해볼 내용이 있다.
# 만약 사진을 업로드 하는 앱이 하나가 아니라 여러 개라고 생각보자.
# 블로그, 게시판, 사진 등등 여러 앱이 각각의 폴더를 만들어서 사진이나 파일을 업로드 할텐데 그러면 프로젝트 루트에 수많은 폴더가 생기게 된다.
# 그러면 매우 지저분해진다.
# 그래서 이를 해결하기 위해 파일들이 모이는 폴더를 따로 하나 만들어 관리하도록 하자.
# settings.py 맨 밑으로 이동

# 5.3.6 뷰 만들기 : views.py로 이동