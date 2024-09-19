from django.urls import path
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView,
    StaffProfileListView, StaffProfileDetailView, StaffProfileCreateView, StaffProfileUpdateView, StaffProfileDeleteView,
    StudentProfileListView, StudentProfileDetailView, StudentProfileCreateView, StudentProfileUpdateView, StudentProfileDeleteView,
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView,
    AttendanceListView, AttendanceDetailView, AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView,
    TimetableListView, TimetableDetailView, TimetableCreateView, TimetableUpdateView, TimetableDeleteView,DashboardView
)

urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
    # User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    # Department URLs
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),

    # StaffProfile URLs
    path('staff_profiles/', StaffProfileListView.as_view(), name='staffprofile_list'),
    path('staff_profiles/<int:pk>/', StaffProfileDetailView.as_view(), name='staffprofile_detail'),
    path('staff_profiles/create/', StaffProfileCreateView.as_view(), name='staffprofile_create'),
    path('staff_profiles/<int:pk>/update/', StaffProfileUpdateView.as_view(), name='staffprofile_update'),
    path('staff_profiles/<int:pk>/delete/', StaffProfileDeleteView.as_view(), name='staffprofile_delete'),

    # StudentProfile URLs
    path('student_profiles/', StudentProfileListView.as_view(), name='studentprofile_list'),
    path('student_profiles/<int:pk>/', StudentProfileDetailView.as_view(), name='studentprofile_detail'),
    path('student_profiles/create/', StudentProfileCreateView.as_view(), name='studentprofile_create'),
    path('student_profiles/<int:pk>/update/', StudentProfileUpdateView.as_view(), name='studentprofile_update'),
    path('student_profiles/<int:pk>/delete/', StudentProfileDeleteView.as_view(), name='studentprofile_delete'),

    # Course URLs
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    # Attendance URLs
    path('attendances/', AttendanceListView.as_view(), name='attendance_list'),
    path('attendances/<int:pk>/', AttendanceDetailView.as_view(), name='attendance_detail'),
    path('attendances/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendances/<int:pk>/update/', AttendanceUpdateView.as_view(), name='attendance_update'),
    path('attendances/<int:pk>/delete/', AttendanceDeleteView.as_view(), name='attendance_delete'),

    # Timetable URLs
    path('timetables/', TimetableListView.as_view(), name='timetable_list'),
    path('timetables/<int:pk>/', TimetableDetailView.as_view(), name='timetable_detail'),
    path('timetables/create/', TimetableCreateView.as_view(), name='timetable_create'),
    path('timetables/<int:pk>/update/', TimetableUpdateView.as_view(), name='timetable_update'),
    path('timetables/<int:pk>/delete/', TimetableDeleteView.as_view(), name='timetable_delete'),
]
