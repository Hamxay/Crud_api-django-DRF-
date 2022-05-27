from django.urls import path

from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="CRUD API",
        default_version='v1',
        description="Test description",
        # terms_of_service="https://www.text.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path("get_all_data", views.list_data),
    path("get_single_detail/<str:pk>", views.list_Detail),
    path("create_task", views.list_created),
    path("list_update/<str:pk>", views.list_update),
    path("list_delete/<str:pk>", views.list_Delete),
]
