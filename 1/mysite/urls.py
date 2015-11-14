from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from library.views import book_list,update,add_book,show,add_author,begin,search,back_search
urlpatterns = patterns('',
    #(r'^hello/$',hello),
    #(r'^time1/$',time1),
    #(r'^time2/$',time3),
    (r'^add_author/$',add_author),
    (r'^book_list/$',book_list),
    (r'^update/(.+)/$',update),
    (r'^add_book/$',add_book),
    (r'^show/(.+)/$',show),
    (r'^begin/$',begin),
    (r'^search/$',search),
    (r'^back_search/$',back_search),
    #(r'^wrong_answer/$',wrong_answer),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
