from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^update/profile$', views.updateprofile, name='update'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^vote/(?P<post_id>\d+)?$', views.vote, name='vote'), 
     url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/post/$', views.PostList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)