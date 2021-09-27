
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from api.views import StudentViewSet
from api.views import StudentModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating router object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('student_api', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/get_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
