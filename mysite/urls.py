from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.views.generic import TemplateView
from collection import views
from collection.backends import MyRegistrationView
from django.contrib.sitemaps.views import sitemap 
from collection.sitemap import (ThingSitemap,StaticSitemap,HomepageSitemap,)
sitemaps = {'things':ThingSitemap,
			'static':StaticSitemap,
			'homepage':HomepageSitemap,}


urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^sitemap\.xml$',sitemap, {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    #url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^things/(?P<slug>[-\w]+)/$', 'collection.views.thing_detail', name='thing_detail'),
    # new line we're adding!
    url(r'^things/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_thing', name='edit_thing'),
    url(r'^things/(?P<slug>[-\w]+)/edit/images/$',views.edit_thing_uploads,name='edit_thing_uploads'),
    url(r'^delete/(?P<id>[-\w]+)/$',views.delete_upload,name='delete_upload'),
    
    url(r'^accounts/password/reset/$', password_reset, 
        {'template_name': 'registration/password_reset_form.html'}, 
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', 
        password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'}, 
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_thing/$', 'collection.views.create_thing', name='registration_create_thing'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^admin/', include(admin.site.urls)),


)
if settings.DEBUG:
		urlpatterns += [
		url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
		]


