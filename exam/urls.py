"""url configuration for exam app"""

from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       (r'^login/$',
                        'django.contrib.auth.views.login',
                        {'template_name': 'login.html'}
                       ),

                       (r'^profile/$', 'exam.views.profile',
                        {'template_name': 'profile.html'}
                       ),

                       (r'^home/$', 'exam.views.home',
                        {'template_name': 'home.html'}
                       ),

                       (r'^questions/$', 'exam.views.topics',
                        {'template_name': 'topics.html'}
                       ),

                       (r'questions/(?P<sub_code>[^/]+)/view_questions/$',
                        'exam.views.view_questions',
                        {'template_name': 'view_questions.html'}
                       ),

                       (r'^sub_report/$', 'exam.views.sub_rep',
                        {'template_name': 'sub_res.html'}
                       ),

                       (r'questions/(?P<sub_code>[^/]+)/reports/$',
                        'exam.views.reports',
                        {'template_name': 'reports.html'}
                       ),

                       (r'^logout/$',
                        'django.contrib.auth.views.logout',
                        {'template_name': 'logged_out.html'}
                       ),

                       (r'^exam/$', 'exam.views.select_topic',
                        {'template_name': 'select_topic.html'}
                       ),

                       (r'^exam/(?P<sub_code>[^/]+)/start_exam/$',
                        'exam.views.start_exam',
                        {'template_name': 'start_exam.html'}
                       ),

                       (r'^password_change/$',
                        'django.contrib.auth.views.password_change',
                        {'template_name': 'password_change_form.html'}
                       ),

                       (r'^password_change/done/$',
                        'django.contrib.auth.views.password_change_done',
                        {'template_name': 'password_change_done.html'}
                       ),

)
