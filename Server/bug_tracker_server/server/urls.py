from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.home, name = 'server-home'),
    path('create-tables/', views.create_tables, name = 'create-tables'),
    path('drop-tables/', views.drop_tables, name = 'drop-tables'),
    path('get-bug-records/', views.get_bug_records, name = 'get-bug-records'),
    path('get-admin-records/', views.get_admin_records, name = 'get-admin-records'),
    path('get-listener-records/', views.get_listener_records, name = 'get-listener-records'),
    path('get-backup-records/', views.get_backup_records, name = 'get-backup-records'),
    path('insert-bug-record/', views.insert_bug_record, name = 'insert-bug-record'),
    path('insert-admin-record/', views.insert_admin_record, name = 'insert-admin-record'),
    path('insert-listener-record/', views.insert_listener_record, name = 'insert-listener-record'),
    path('insert-backup-record/', views.insert_backup_record, name = 'insert-backup-record'),
    path('update-bug-record/', views.update_bug_record, name = 'update-bug-record'),
    path('update-admin-record/', views.update_admin_record, name = 'update-admin-record'),
    path('update-listener-record/', views.update_listener_record, name = 'update-listener-record'),
    path('update-backup-record/', views.update_backup_record, name = 'update-backup-record'),
    path('delete-bug-record/', views.delete_bug_record, name = 'delete-bug-record'),
    path('delete-dev-record/', views.delete_dev_record, name = 'delete-dev-record'),
    path('delete-listener-record/', views.delete_listener_record, name = 'delete-listener-record'),
    path('delete-backup-record/', views.delete_backup_record, name = 'delete-backup-record'),
    path('get-distinct-admins/', views.get_distinct_admins, name = 'get_distinct-admins'),
    path('get-distinct-bug-sources/', views.get_distinct_bug_sources, name = 'get-distinct-bug-sources'),
    path('check-user-login/', views.check_user_login, name = 'check-user-login'),
]