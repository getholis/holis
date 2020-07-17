from apps.users.api import views
from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("list", views.UserViewSet)
router.register("notifications", views.NotificationViewSet)

urlpatterns = [
    path("check-company/<str:company_name>/", views.CheckCompanyAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("set-status/", views.SetStatusAPIView.as_view()),
    path(
        "suggest-company-code/",
        views.SuggestCompanyCodeAPIView.as_view(),
        name="suggest-company-code",
    ),
]


urlpatterns += router.urls
