# apps.py는 각 앱에 대한 설명들이 있다.
# 나중에 커스텀 시그널을 만들게 되면 추가 코딩하는 부분이 있다.

from django.apps import AppConfig


class BookmarkConfig(AppConfig):
    name = 'bookmark'
