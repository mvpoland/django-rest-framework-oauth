from __future__ import unicode_literals

from django.conf.urls import url, include
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework_oauth import permissions
from rest_framework_oauth.authentication import OAuthAuthentication, OAuth2Authentication
from rest_framework.views import APIView


class MockView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

    def post(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

    def put(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})


class OAuth2AuthenticationDebug(OAuth2Authentication):
    allow_query_params_token = True


urlpatterns = [
    url(r'^oauth/$', MockView.as_view(authentication_classes=[OAuthAuthentication])),
    url(
        r'^oauth-with-scope/$',
        MockView.as_view(
            authentication_classes=[OAuthAuthentication],
            permission_classes=[permissions.TokenHasReadWriteScope]
        )
    ),

    url(r'^oauth2/', include('provider.oauth2.urls')),
    url(r'^oauth2-test/$', MockView.as_view(authentication_classes=[OAuth2Authentication])),
    url(r'^oauth2-test-debug/$', MockView.as_view(authentication_classes=[OAuth2AuthenticationDebug])),
    url(
        r'^oauth2-with-scope-test/$',
        MockView.as_view(
            authentication_classes=[OAuth2Authentication],
            permission_classes=[permissions.TokenHasReadWriteScope]
        )
    ),
]
