"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# 장고 3.0부터 추가된 파일이다.
# 비동기 관련 지원되도록 만들어진 것
# wsgi를 지원하는 웹서버와 asgi를 지원하는 웹서버가 조금 달라서 신경써서 세팅해야하는 부분이 있다.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
