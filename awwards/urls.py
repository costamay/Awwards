
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('projects.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'} ),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]
