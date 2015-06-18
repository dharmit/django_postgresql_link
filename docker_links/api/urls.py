from django.conf.urls import url, patterns


urlpatterns = patterns(
    'api.views',

    url(r'^users/(?P<pk>[0-9]+)',
        'user_detail', name='user_detail'),

    url(r'^users/new/$', 'user_create', name='user_create'),
)
