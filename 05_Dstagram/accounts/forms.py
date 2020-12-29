# 5.4.3 회원 가입 기능 만들기
# 로그인 로그아웃 기능은 회원 가입 기능이 없다면 쓸모 없는 기능이다.
# 회원 가입 기능을 만들기 위해서는 뷰를 만들어야 하고 폼도 만들어야 한다.
# 회원 가입 양식인 폼을 만들기 위해서 forms.py 파일에 코드를 입력하자.

from django.contrib.auth.models import User
from django import forms

# 회원 가입 양식을 출력하기 위해 RegisterForm이라는 클래스를 만들었다.
# 이 클래스는 forms.ModelForm을 상속받는데 모델이 있고 그에 대한 자료를 입력받고 싶을 때 사용한다.
class RegisterForm(forms.ModelForm):
    # password의 경우에는 fields에 설정할 수 있지만 종류가 CharField이기 때문에 별도의 widget 옵션을 사용해 password 속성의 input 태그를 사용하려고 클래스 변수로 지정했다.
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # 또 password2 필드도 만들어서 회원 가입시 비밀번호 재입력 기능을 구현하도록 했다.
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    # 폼 클래스 내부에 있는 Meta 클래스를 이용하면 기존에 있는 모델의 입력 폼을 쉽게 만들 수 있다.
    class Meta:
        # model을 설정하고 fields를 이용해서 입력받을 필드들을 지정하면 된다.
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # clean_password2는 clean_필드명 형태의 메서드이다.
    # 이런 형태의 메서드들은 각 필드의 clean 메서드가 호출된 후에 호출되는 메서드이다.
    # 특별한 유효성 검사나 조작을 하고 싶을 때 만들어서 사용한다.
    # 이번 경우에는 password와 password2가 같은지 비교하는 코드를 실행하기 위해서 사용했다.
    # clean_필드명 형태의 메서드에서 해당 필드의 값을 사용할 때는 꼭 cleaned_data에서 필드 값을 찾아서 사용해야 한다.
    # 이 값이 이전 단계까지 기본 유효성 검사같은 처리를 마친 값이기 때문이다.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']

# 완성한 폼을 사용해서 뷰를 만들어보자.
# views.py를 열고 register라는 함수형 뷰를 만든다.
