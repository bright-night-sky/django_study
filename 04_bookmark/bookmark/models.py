# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다는 목적(이게 더 큰 목적이다.)
# 모델 = 데이터베이스 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값들) = 레코드의 컬럼 데이터값

# 내가 만약 어떤 정보를 데이터베이스에 저장해야겠다라는 것이 필요하면 모델을 만들면 된다.
# 잘 만드는 방법은 뒤에서 설명하겠다.

from django.db import models

# Create your models here.
# 모델은 클래스로 만들어지기 때문에 첫 글자를 대문자로 만들어야한다.
class Bookmark(models.Model):
    # 모델에는 필드를 추가할 때 종류를 명시해줘야한다.
    # 데이터가 들어갈 수 있는 공간이 한정되있기 때문에 종류와 제한을 지정하는 것이 좋다.
    # 그래야 메모리와 용량을 아끼면서 데이터를 담을 수 있다.
    site_name = models.CharField(max_length=100) # 글자를 입력
    url = models.URLField('Site URL') # URLField로 만들면 장고 자체에서 링크 기능을 제공한다.
    # 안에 'Site URL'은 레이블을 지정해주는 것이다.
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항(몇 글자까지 등등)
    # 3. Form의 종류를 결정
    # 4. Form에서의 제약 사항도 결정

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

# 모델을 만들었다 => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정했다는 말!
# 모델을 만들었으면
# makemigrations => 모델의 변경사항을 추적해서 기록하는 것
# 하고 나면 migrations 폴더에 0001_inital.py 파일이 생성된다.
# 마이그레이션(migration) 하기 => 데이터베이스에 모델의 내용을 반영(테이블 생성)
# 모델을 수정하고 나서도 migration을 해야한다.

