from django.urls import include, path
from rest_framework import routers
from myapp.views import Insertdata
from django.contrib import admin
from django.urls import include
from myapp import urls
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    # path('', include('myapp.urls'))
]


# urlpatterns += router.urls
