# 꼭 앱폴더 내에 위치하는게 아니더라도 동작은 한다.

# 뷰 : 기능을 담당(페이지 단위)
# 화면이 나타나는 뷰, 화면이 없는 뷰
# 화면이 나타나는 뷰 : 템플릿이 존재 O(사용자가 화면을 보거나)
# 화면이 없는 뷰 : 템플릿이 없기도 있기도 하는 것(사용자의 화면에 나타나지 않는)
# 화면이 있건 없건 주소 URL은 있어야 한다.

# 뷰 내용(함수 or 클래스), URL이 있으면 동작한다.

# 뷰의 코드 형식 : 함수형, 클래스형 두 가지
# 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수,
#         내가 원하는대로 동작들을 설계하고 만들고 싶을 때 사용

# 클래스형 : CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
#           상속받아서 사용한다.
# 장고의 제네릭 뷰를 많이 사용

from django.http import HttpResponse
from django.shortcuts import render # render는 템플릿을 렌더링해주는 것이다.

# 함수형 뷰
# request에는 사용자가 요청한 내용들이 다 들어있다. 세션이나 쿠키값 등, 필수 매개변수다.
# 매개변수가 추가되는 경우도 있다.
def index(request):
    # 어떤 계산이나, 데이터베이스 조회, 수정, 등록 등
    # 응답 메시지를 만들어서 반환한다.
    # 실전에서는 html 변수를 대신해서 템플릿을 사용한다. 여기서는 그냥 예시
    html = "<html><body>Hi Django.</body></html>"
    return HttpResponse(html)

# 문제
# 뷰의 이름은 : welcome
# 뷰의 접속 주소 : welcome/ (뒤에 꼭 슬래쉬가 들어가야한다.)
# 내용 : Welcome to Django.
# 출력하는 뷰 만들기
def welcome(request):
    html = "<html><body>Welcome to Django.</body></html>"
    return HttpResponse(html)


def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 여러분이 설정한 폴더
    return render(request, 'test.html')

# 연습해야할 것
# 함수형 뷰 만들기, 템플릿 만들기, URL 연결하기, 브라우저로 접속해보기
# 익숙해져야한다.
