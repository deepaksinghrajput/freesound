# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
import django.contrib.auth.views as authviews
import messages.views as messages
import views as accounts

urlpatterns = patterns('accounts.views',
    url(r'^login/$', authviews.login, {'template_name': 'accounts/login.html'}, name="accounts-login"),
    url(r'^logout/$', authviews.logout, {'template_name': 'accounts/logout.html'}, name="accounts-logout"),
    url(r'^activate/(?P<activation_key>[^//]+)/$', accounts.activate_user, name="accounts-activate-user"),
    url(r'^signup/$', accounts.signup, name="accounts-signup"),
    
    url(r'^$', accounts.home, name="accounts-home"),
    url(r'^edit/$', accounts.edit, name="accounts-edit"),

    url(r'^upload/$', accounts.upload, name="accounts-upload"),
    url(r'^upload/(?P<unique_id>\d{10})/$', accounts.upload, name="accounts-upload-unique"),
    url(r'^upload/progress/(?P<unique_id>\d{10})/$', accounts.upload_progress, name="accounts-upload-progress"),
    url(r'^describe/$', accounts.describe, name="accounts-describe"),
    url(r'^attribution/$', accounts.attribution, name="accounts-attribution"),

    url(r'^messages/$', messages.inbox, name='messages'),
    url(r'^messages/sent/$', messages.sent_messages, name='messages-sent'),
    url(r'^messages/archived/$', messages.archived_messages, name='messages-archived'),
    url(r'^messages/changestate/$', messages.messages_change_state, name='messages-change-state'),
    url(r'^messages/(?P<message_id>\d+)/$', messages.message, name='message'),
    url(r'^messages/new/$', messages.new_message, name='messages-new'),
    url(r'^messages/new/(?P<username>[^//]+)/$', messages.new_message, name='messages-new'),
)