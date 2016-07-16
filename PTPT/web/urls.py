from django.conf.urls import url
from .import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^signup/thanks/$',views.signup_thanks),
    url(r'^accounts/login/$',login,{'template_name':'web/login.html'}, name='login'),
    url(r'^accounts/logout/$',logout, {'template_name':'web/logout.html'},name='logout'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
    url(r'^accounts/edit-profile/$',views.edit_profile,name='edit_profile'),
    url(r'^accounts/view-profile/$',views.view_profile,name='view_profile'),
    url(r'^accounts/verify-student/$',views.verify_student,name='verify_student'),
    url(r'^accounts/join-tutor/$',views.join_tutor_form,name='join-tutor'),
    url(r'^accounts/join-tutor/thanks/$',views.join_tutor_thanks),
    url(r'^advanced_search/$', views.adv_search, name='advanced_search'),
    url(r'^advanced_search/results/$', views.adv_search_results, name='adv_search_results'),
    url(r'^search_modules/$', views.search_modules, name='search_modules'),

    ]
