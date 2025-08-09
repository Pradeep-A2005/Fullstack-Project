from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  
    path('admin_login/', views.admin_login, name='admin_login'),
    path('reviewer_login/', views.reviewer_login, name='reviewer_login'),
    path('admin_access/', views.admin_access, name='admin_access'),
    path('admin_dash/', views.admin_dash, name='admin_dash'),
    path('Admin_mark/', views.Admin_mark, name='Admin_mark'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('review_mark/', views.review_mark, name='review_mark'),
    path('review_view/', views.review_view, name='review_view'),
    path('reviewer_dashboard/', views.reviewer_dashboard, name='reviewer_dashboard'),
    path('select/', views.select, name='select'),
    path('select1/', views.select1, name='select1'),
    path('team/', views.team, name='team'),
    path('student-selection/', views.student_selection, name='select'),
    path('student-selection1/', views.student_selection1, name='select1'),
    # path('admin_mark/', views.admin_mark_view, name='admin_mark'),
    # path('admin_view/', views.admin_view, name='admin_view'),
    path('team_mark/', views.team_mark_view, name='team_mark'),  
    path('review_view/', views.review_view, name='review_view'),
    path('review_mark/', views.review_mark_view, name='review_mark'),
    path('review_view/', views.review_view, name='review_view'),
    path('admin-access/', views.admin_access_view, name='admin_access'),
    
    
    path('Admin_mark/', views.admin_mark_entry, name='admin_mark_entry'),
    path('admin_view/', views.admin_view, name='admin_view'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)