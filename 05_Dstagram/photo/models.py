# 1. 모델 : 데이터베이스에 저장될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰(기능) : 계산, 처리 - 실제 기능, 화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록하는 것 - 주소를 지정
# 4. 화면에 보여줄 것이 있다. : 템플릿 작성(html)

# 5.3.2 모델 만들기
# models.py에 Photo 모델을 만들도록 하겠다.

from django.db import models
# 장고의 기본 유저 모델
from django.contrib.auth.models import User
# 장고 고급에서는 유저 모델을 커스터마이징해서 쓸 수도 있다.
from django.urls import reverse

# Create your models here.
# 모델은 항상 클래스 형태로 만들고 models.Model을 상속받는다.
# Photo 모델에는 총 5개의 필드를 만든다.
# 외래키(ForeignKey) - User 테이블에서 해당 유저를 찾을 수 있는 주키
# 주키(PrimaryKey) - User 테이블에 1 admin x x x x
class Photo(models.Model):
    # author : ForeignKey를 사용하여 User 테이블과 관계를 만든다.
    #          여기서 User 모델은 장고에서 기본적으로 사용하는 사용자 모델이다.
    #          on_delete 인수는 연결된 모델이 삭제될 경우 현재 모델의 값은 어떻게 할 것이냐이다.
    #          삭제될 때의 동작은 다음과 같은 옵션을 선택한다.
    #               CASCADE : 연결된 객체가 지워지면 해당 하위 객체도 같이 삭제
    #               PROTECT : 하위 객체가 남아 있다면 연결된 객체가 지워지지 않음
    #               SET_NULL : 연결된 객체만 삭제하고 필드 값을 null로 설정
    #               SET_DEFAULT : 연결된 객체만 삭제하고 필드 값을 설정된 기본 값으로 변경
    #               SET() : 연결된 객체만 삭제하고 지정한 값으로 변경
    #               DO_NOTHING : 아무 일도 하지 않음
    #          세 번째 인수인 related_name은 연결된 객체에서 하위 객체의 목록을 부를 때 사용할 이름이다.
    #          Photo 모델을 예로 들면 어떤 유저가 작성한 글을 불러올 때는 유저 객체에 user_photos 속성을 참조하면 된다.
    #          User 테이블 입장에서 Photo를 찾을수 있게 하는 것
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    # photo : 사진 필드이다. 여기서는 한 장만 올리는 기능이다.
    # 원래 FileField만 있었는데 ImageField가 추가되었다.
    # 나중에 더 배워서 진짜 인스타그램처럼 여러 장을 한 번에 올리는 기능도 구현해보길
    # upload_to는 사진이 업로드 될 경로를 설정한다.
    # upload_to에 함수도 지정할 수 있다.
    # 만약 업로드가 되지 않을 경우 default 값으로 대체한다.
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    # text : 사진에 대한 설명을 저장할 텍스트 필드이다.
    # 문자열 길이에 제한을 두지 않았다.
    text = models.TextField()
    # created : 글 작성일을 저장하기 위한 날짜시간 필드이다.
    # auto_now_add 옵션을 설정하면 객체가 추가될 때 자동으로 값을 설정한다.
    # auto_now_add는 데이터베이스에 데이터가 한 번 새로 등록될 때
    created = models.DateTimeField(auto_now_add=True)
    # updated : 글 수정일을 저장하기 위한 날짜시간 필드이다.
    # auto_now 옵션을 설정하면 객체가 수정될 때마다 자동으로 값을 설정한다.
    # auto_now는 매번 등록되거나 수정될 때마다 설정되는 것
    updated = models.DateTimeField(auto_now=True)

    # 필드는 나중에 더 추가할 것이다.
    # 우선 필요한 필드는 모두 작성했으니 옵션 클래스인 Meta 클래스를 추가하겠다.
    # Photo 모델에 Meta 클래스를 추가하고 ordering 값을 설정한다.
    class Meta:
        # 밑과 같이 따로 기준을 만들지 않은 경우, 기본적인 정렬은 자동으로 만들어지는 id 필드를 기준으로 정렬이 된다.
        # ordering 클래스 변수는 해당 모델의 객체들을 어떤 기준으로 정렬할 것인지 설정하는 옵션이다.
        # -updated로 설정했으니 글 수정 시간의 내림차순으로 정렬한 것이다.
        # 그래서 제일 최신 게시물이 제일 위에 올라온다.
        ordering = ['-updated']
    # Meta 클래스 다음으로는 지난 장에서 배운 __str__ 메서드를 추가하겠다.

    # __str__ 메서드는 작성자의 이름과 글 작성일을 합친 문자열을 반환한다.
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
    # 마지막으로 get_absolute_url 메서드를 추가한다.

    # get_absolute_url은 객체의 상세 페이지의 주소를 반환하는 메서드이다.
    # 객체를 추가하거나 수정했을 때 이동할 주소를 위해 호출되기도 하고 템플릿에서 상세 화면으로 이동하는 링크를 만들 때 호출하기도 한다.
    # 이런 주소를 만들기 위해서는 reverse 메서드를 사용하는데 reverse 메서드는 URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어주는 함수이다.
    # 여기서는 상세 화면의 패턴이름을 photo:photo_detail로 설정했는데 아직 만들지 않은 뷰이지만 get_absolute_url을 호출하기 전까지는 오류가 발생하지 않기 때문에 미리 만들어도 된다.
    # 마지막 인수인 args는 여러 값들을 리스트로 전달하는데 사용되는데 여기서는 URL을 만드는데 필요한 pk 값을 전달하는데 사용되었다.
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

    # 모델을 만들었으니 데이터베이스에 적용해보자.
    # makemigrations 명령어를 이용해 모델의 변경사항을 기록한다.
    # 이 명령을 실행하면 이전과 다르게 오류 메시지가 출력된다.
    # 메시지를 읽어보면 ImageField를 사용하려면 Pillow라는 모듈이 필요하다고 한다.
    # Pillow 모듈은 파이썬에서 이미지를 다룰 때 필요한 필수 모듈이다. 설치하자.
    # 설치하고 나면 다시 python manage.py makemigrations photo 명령을 실행하자.

    # makemigrations를 이용해 기록한 변경사항을 데이터베이스에 적용하려면 migrate 명령을 사용한다.
    # python manage.py migrate photo 0001
    # 모델을 만들었으니 관리자 페이지에 등록하고 업로드를 해보자.
    # admin.py로 이동