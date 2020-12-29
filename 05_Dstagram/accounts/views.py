# 이 뷰에서는 기존의 제네릭 뷰에서 어떤 식으로 처리를 하는지 알아볼 수 있는 힌트가 있다.

from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    # if request.method == 'POST'라는 부분은 회원 가입 정보가 서버로 전달됐다는 의미이다.
    # 입력을 받는 템플릿들을 보면 form 태그에 method가 post로 설정되어 있는 것을 자주 보았다.
    # post는 HTTP 메서드들 중 하나로 서버로 자료를 전달할 때 사용하는 메서드이다.
    # 따라서 post 방식으로 뷰를 호출했다는 것은 서버로 자료를 전달하는 상태라는 것을 알 수 있다.
    # 그래서 정보를 전달 받으면 RegisterForm을 이용해 유효성 검사를 수행하고 이상이 없으면 데이터베이스에 저장한다.
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # 저장하는 절차는 두 단계를 거친다.
            # 우선 user_form.save 메서드를 통해 폼 객체에 지정된 모델을 확인하고 이 모델의 객체를 만든다.
            # 이 때 옵션으로 commit=False를 지정했기 때문에 데이터베이스에 저장하는 것이 아니라 메모리 상에 객체만 만들어진다.
            new_user = user_form.save(commit=False)
            # 그리고 set_password 메서드를 사용해 비밀번호를 지정한다.
            # 이런 과정을 거쳐야 비밀번호가 암호화된 상태로 저장된다.
            new_user.set_password(user_form.cleaned_data['password'])
            # 비밀번호까지 지정했다면 new_user의 save 메서드를 호출해 실제로 데이터베이스에 저장한다.
            new_user.save()
            # 회원 가입이 완료되었으므로 register_done이라는 템플릿을 렌더링해 보여준다.
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    # 반대로 HTTP 메서드가 POST가 아니라면 자료를 전달받은 상태가 아니라 입력을 받는 화면을 보여줘야한다.
    # 그래서 이 때는 비어있는 RegisterForm 객체를 만들고 register 템플릿을 렌더링해 보여준다.
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form': user_form})

# 이 뷰를 사용하기 위해 URL을 연결하겠다.
# urls.py 파일을 열어 수정한다.