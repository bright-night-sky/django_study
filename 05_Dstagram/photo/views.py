# 5.3.6 뷰 만들기
# 사진 목록, 업로드, 확인, 수정, 삭제 기능을 위한 뷰를 만들어보자.

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Photo

# Create your views here.
# 첫 번째는 목록이다.
# 함수형 뷰로 만들기 위해 photo_list라는 함수를 만든다.
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})
# 함수형 뷰는 기본 매개변수로 request를 설정한다.
# 클래스형 뷰와는 달리 모든 기능을 직접 처리해야 한다.
# 목록으로 출력할 사진 객체를 불러오기 위해 Photo 모델의 기본 매니저인 objects를 이용해 all 메서드를 호출한다.
# 그럼 데이터베이스에 저장된 모든 사진을 불러온다.
# 그리고 render 함수를 사용해서 list.html 템플릿을 렌더링한다.
# 이 때 photos 라는 템플릿 변수를 같이 전달한다.

# 다음은 사진 업로드 뷰를 만들자.
# 제네릭 뷰를 사용할텐데 다른 뷰에 사용할 제네릭 뷰들을 미리 임포트하겠다.
# CreateView, DeleteView, UpdateView를 임포트하고 CreateView를 상속받는 PhotoUploadView를 만든다.
class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    # PhotoUploadView에는 template_name이라는 클래스 변수를 만들었다.
    # 이 변수에는 실제 사용할 템플릿을 설정한다.
    template_name = 'photo/upload.html'

    # form_valid 메서드는 업로드를 끝낸 후 이동할 페이지를 호출하기 위해 사용하는 메서드이다.
    # 이 메서드를 오버라이드해서 작성자를 설정하는 기능을 추가했다.
    def form_valid(self, form):
        # 작성자는 현재 로그인 한 사용자로 설정한다.
        form.instance.author_id = self.request.user.id
        # 작성자를 설정하고 나면 is_valid 메서드를 이용해 입력된 값들을 검증한다.
        # 이상이 없다면
        if form.is_valid():
            # 데이터베이스에 저장하고
            form.instance.save()
            # redirect 메서드를 이용해 메인 페이지로 이동한다.
            return redirect('/')
        # 만약 이상이 있다면
        else:
            # 작성된 내용을 그대로 작성 페이지에 표시한다.
            return self.render_to_response({'form': form})

# 나머지 뷰들도 제네릭 뷰를 사용해서 적절히 만들어준다.
class PhotoDeleteView(DeleteView):
    model = Photo
    # success_url의 값 '/'는 사이트 메인을 뜻한다.
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

# 뷰를 다 만들었는데 지금 Detail 뷰가 없다.
# 제네릭 뷰를 이용하면 쉽게 뷰를 만들 수 있는데 views.py에 작성하는 방법 말고 다른 방법이 있다.
# Detail 뷰는 그 방법을 이용해 만들 것이다.
# 5.3.7 URL 연결 -> urls.py로 이동