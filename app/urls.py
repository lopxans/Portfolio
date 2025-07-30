from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    
    # Contact URLs
    path('contact/', contact, name='contact'),
    path('contact_view/', contact_view, name='contact_view'),
    path('recycle_contact/', recycle_contact, name='recycle_contact'),
    path('soft_delete_contact/<int:id>', soft_delete_contact, name='soft_delete_contact'),
    path('hard_delete_contact/<int:id>', hard_delete_contact, name='hard_delete_contact'),
    path('restore_contact/<int:id>', restore_contact, name='restore_contact'),
    path('restore_all_contact/', restore_all_contact, name='restore_all_contact'),
    path('clear_all_contact/', clear_all_contact, name='clear_all_contact'),
    
    # Certificate URLS
    path('certificate/', certificate, name='certificate'),
    path('certificate_form/', certificate_form, name='certificate_form'),
    path('recycle_certificate/', recycle_certificate, name='recycle_certificate'),
    path('delete/<int:id>', certificate_soft_delete, name='certificate_soft_delete'),
    path('hard_delete_cert/<int:id>', hard_delete_cert, name='hard_delete_cert'),
    path('clear_all_cert', clear_all_cert, name='clear_all_cert'),
    path('restore_cert/<int:id>', restore_cert, name='restore_cert'),
    path('restore_all_cert', restore_all_cert, name='restore_all_cert'),
    path('edit_certificate/<int:id>', edit_certificate, name='edit_certificate'),
    
    # Project URLS
    path('project/', project, name='project'),
    path('project_form/', project_form, name='project_form'),
    path('recycle_project/', recycle_project, name='recycle_project'),
    path('project_soft_delete/<int:id>', project_soft_delete, name='project_soft_delete'),
    path('project_hard_delete/<int:id>', project_hard_delete, name='project_hard_delete'),
    path('project_clear_all/', project_clear_all, name='project_clear_all'),
    path('project_restore/<int:id>', project_restore, name='project_restore'),
    path('project_restore_all/', project_restore_all, name='project_restore_all'),
    path('edit_project/<int:id>', edit_project, name='edit_project'),
]
