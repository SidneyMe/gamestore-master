from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from ajax_select import urls as ajax_select_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.logout_then_login, name='logout'),
    path('accounts/reset-password', auth_views.PasswordResetView.as_view(), name="password-reset"),
    path('accounts/reset-password-done', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('accounts/reset-password-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset-password-complete', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('', include('gamestore.urls')),
    path('api/', include('api.urls')),
    path("select2/", include("django_select2.urls")),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
