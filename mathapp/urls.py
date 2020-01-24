from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from mathapp import views
from mathapp.views import (MainList,
						   CategoryListView,
						   CategoryDetailView,
						   ElementaryDetailView,
						   BeginnerListView,
						   BeginnerDetailView,
						   LoginView,
						   UserAccountView,
						   BuyView,
						   UserReactionView,
						   ExamView
						)
from . import views

urlpatterns = [
	url(r'^$', MainList.as_view(), name = 'base_view'),
	url(r'^category/$', CategoryListView.as_view(), name='category'),
	url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
	url(r'^elementary-detail/(?P<slug>[-\w]+)/$', ElementaryDetailView.as_view(), name='elementary-detail'),
	url(r'^beginner/$', BeginnerListView.as_view(), name='beginner'),
	url(r'^beginner-detail/(?P<slug>[-\w]+)/$', BeginnerDetailView.as_view(), name='beginner-detail'),
	url(r'^login_view/$', LoginView.as_view(), name = 'login_view'),
	url(r'^user_account/(?P<user>[-\w]+)/$', UserAccountView.as_view(), name='account_view'),
	url(r'^user_reaction/$', UserReactionView.as_view(), name='user_reaction'),
	url(r'^buy/$',BuyView.as_view(), name='buy'),
	url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('base_view')), name='logout_view'),
	url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^exam/(?P<slug>[-\w]+)/$', ExamView.as_view(), name='exam'),
]
