from django.conf.urls import patterns,  url


urlpatterns = patterns('',
            url(r'^$', 'my_blog.views.add_message'),
            #url(r'^add_new_message/$', 'my_blog.views.add_new_message'),
            #url(r'^add_new_message/save/$', 'my_blog.views.save_message'),

            url(r'^page/(\d+)/$', 'my_blog.views.add_message'),


            )
