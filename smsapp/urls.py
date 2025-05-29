from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('students/<int:id>/', views.student_details, name='student_details'),
    path('coarses/', views.coarses, name='coarses'),
    path('enroll_coarse/', views.enroll_coarse, name='enroll_coarse'),
    path('coarses/<int:student_id>/delete', views.deleteCourse, name='deleteCourse'),
    #path('coarse/<int:coarsecode>/update', views.updateCourse, name='updateCourse'),

    ]

