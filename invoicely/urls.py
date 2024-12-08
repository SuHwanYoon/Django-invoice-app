from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 기본인증관련 엔트포인트 제공, 회원가입, 사용자관리 등의 기능 제공
    #     /users/ (사용자 생성)
    # /users/me/ (현재 사용자 정보)
    # /users/confirm/ (이메일 확인)
    path('api/v1/', include('djoser.urls')),
    # 토큰 기반 인증 관련 엔드포인트 제공 - 로그인, 로그아웃
    # /token/login/ (로그인)
    # /token/logout/ (로그아웃)
    path('api/v1/', include('djoser.urls.authtoken'))
]
