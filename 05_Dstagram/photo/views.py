# 5.3.6 뷰 만들기
# 사진 목록, 업로드, 확인, 수정, 삭제 기능을 위한 뷰를 만들어보자.

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# 5.5.3 권한 제한하기 위한 import
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# 댓글도 사용할 수 있게 됐으니 인스타그램처럼 로그인한 사용자만 이 서비스를 사용할 수 있도록 변경해보자.
# photo 앱의 views.py 파일을 수정하겠다.
# 권한 제한을 하는 방법은 다양하게 있지만 가장 쉽게 하는 방법은 두 가지이다.
# 데코레이터(decorator)와 믹스인(mixin)을 사용하는 방법이다.

from .models import Photo

# Create your views here.
# 첫 번째는 목록이다.
# 함수형 뷰로 만들기 위해 photo_list라는 함수를 만든다.
@login_required
def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all() # objects는 ORM 매니저이다. all()은 전부 다 달라는 쿼리이다.
    return render(request, 'photo/list.html', {'photos': photos})
# 주의사항 : 함수형 뷰는 기본 매개변수로 request를 설정한다.
# 클래스형 뷰와는 달리 모든 기능을 직접 처리해야 한다.
# 목록으로 출력할 사진 객체를 불러오기 위해 Photo 모델의 기본 매니저인 objects를 이용해 all 메서드를 호출한다.
# 그럼 데이터베이스에 저장된 모든 사진을 불러온다.
# 그리고 render 함수를 사용해서 list.html 템플릿을 렌더링한다.
# 'photo/list.html'에서 템플릿을 찾을 때는 앱 폴더로부터 찾는게 아니라 템플릿 폴더로부터 찾아내려간다.
# 이 때 photos 라는 템플릿 변수를 같이 전달한다.

# 다음은 사진 업로드 뷰를 만들자.
# 제네릭 뷰를 사용할텐데 다른 뷰에 사용할 제네릭 뷰들을 미리 임포트하겠다.
# CreateView, DeleteView, UpdateView를 임포트하고 CreateView를 상속받는 PhotoUploadView를 만든다.
class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    # 작성자(author), 작성시간(created)도 필요하지만
    # 일단 작성시간(created)는 add_auto_now로 자동으로 넣어지고,
    # 작성자(author)는 로그인한 사람이 작성자이므로 밑에서 따로 처리한다.
    fields = ['photo', 'text']
    # PhotoUploadView에는 template_name이라는 클래스 변수를 만들었다.
    # 이 변수에는 실제 사용할 템플릿을 설정한다.
    template_name = 'photo/upload.html'

    # 작성자 확인은 백엔드, 프론트엔드(자바스크립트)에서 모두 확인하는 것이 가장 보안에 좋다.
    # 누가 어디 부분의 취약점을 건드릴지 모르기 때문이다.
    # form_valid 메서드는 업로드를 끝낸 후 이동할 페이지를 호출하기 위해 사용하는 메서드이다.
    # 이 메서드를 오버라이드해서 작성자를 설정하는 기능을 추가했다.
    def form_valid(self, form):
        # 작성자는 필수 필드이다.
        # 작성자는 현재 로그인 한 사용자로 설정한다.
        # ForeignKey 같은 경우 _id로 값을 불러온다. 장고 매뉴얼에 있는 내용이다.
        # 로그인을 한 전제이므로 self.request.user.id가 있다.
        # 로그인을 하지 않은 전제는 나중에 코딩할 것이다.
        form.instance.author_id = self.request.user.id
        # 작성자를 설정하고 나면 is_valid 메서드를 이용해 입력된 값들을 검증한다.
        # 이상이 없다면
        if form.is_valid():
            # 데이터베이스에 저장하고
            form.instance.save() # 팩토리 패턴 검색해보기
            # redirect 메서드를 이용해 메인 페이지로 이동한다.
            return redirect('/')
        # 만약 이상이 있다면
        else:
            # 작성된 내용을 그대로 작성 페이지에 표시한다.
            return self.render_to_response({'form': form})
            # 잘못 만든 사이트 같은 경우 회원가입 정보를 잘못 입력하고 가입 버튼을 눌렀을 때, 정보 입력이 제대로 안됬다면서 다시 돌아오게 한 뒤 확인해보면 입력된 내용이 다 사라져있는 경우가 있다.
            # 그게 바로 위의 폼 설정을 제대로 안 한 경우이다.

# 나머지 뷰들도 제네릭 뷰를 사용해서 적절히 만들어준다.
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    # success_url의 값 '/'는 사이트 메인을 뜻한다.
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

# 뷰를 다 만들었는데 지금 Detail 뷰가 없다.
# 제네릭 뷰를 이용하면 쉽게 뷰를 만들 수 있는데 views.py에 작성하는 방법 말고 다른 방법이 있다.
# Detail 뷰는 그 방법을 이용해 만들 것이다.
# 5.3.7 URL 연결 -> urls.py로 이동

# 데코레이터는 함수형 뷰에서 사용하고
# 믹스인은 클래스형 뷰에서 사용한다.
# 데코레이터는 뷰의 바로 윗줄에 써주고
# 믹스인은 첫 번째로 상속하도록 한다.
# 이렇게 뷰를 수정한 뒤에 로그아웃하고 메인 페이지에 접속하면 바로 로그인 화면으로 이동하는 것을 확인할 수 있다.
# 현재 Detail 뷰는 views.py에 없기 때문에 상속을 할 수가 없어 권한 제한을 추가하지 못했다.
# 여러분이 직접 views.py에 PhotoDetailView를 구현하고 권한 제한도 추가해보자.