from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department, StaffProfile, StudentProfile, Course, Enrollment, Attendance, Exam, ExamResult, Timetable, User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'admin'

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'staff'
    
class UserCreateView(AdminRequiredMixin,CreateView):
    model = User
    template_name = 'user_form.html'
    fields = ['username', 'email', 'role', 'password']
    success_url = reverse_lazy('user_list')
    
class UserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserUpdateView(AdminRequiredMixin, UpdateView):
    model = User
    template_name = 'user_form.html'
    fields = ['username', 'email', 'role']
    success_url = reverse_lazy('user_list')

class UserDeleteView(AdminRequiredMixin, DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'

class DepartmentCreateView(AdminRequiredMixin,CreateView):
    model = Department
    template_name = 'department_form.html'
    fields = ['name', 'head_of_department']
    success_url = reverse_lazy('department_list')

class DepartmentUpdateView(AdminRequiredMixin,UpdateView):
    model = Department
    template_name = 'department_form.html'
    fields = ['name', 'head_of_department']
    success_url = reverse_lazy('department_list')

class DepartmentDeleteView(AdminRequiredMixin,DeleteView):
    model = Department
    template_name = 'department_confirm_delete.html'
    success_url = reverse_lazy('department_list')

# StaffProfile Views
class StaffProfileListView(ListView):
    model = StaffProfile
    template_name = 'staffprofile_list.html'
    context_object_name = 'staff_profiles'

class StaffProfileDetailView(DetailView):
    model = StaffProfile
    template_name = 'staffprofile_detail.html'
    context_object_name = 'staff_profile'

class StaffProfileCreateView(AdminRequiredMixin,CreateView):
    model = StaffProfile
    template_name = 'staffprofile_form.html'
    fields = ['user', 'department', 'designation', 'date_of_joining']
    success_url = reverse_lazy('staffprofile_list')

class StaffProfileUpdateView(AdminRequiredMixin,UpdateView):
    model = StaffProfile
    template_name = 'staffprofile_form.html'
    fields = ['user', 'department', 'designation', 'date_of_joining']
    success_url = reverse_lazy('staffprofile_list')

class StaffProfileDeleteView(AdminRequiredMixin,DeleteView):
    model = StaffProfile
    template_name = 'staffprofile_confirm_delete.html'
    success_url = reverse_lazy('staffprofile_list')

# StudentProfile Views
class StudentProfileListView(ListView):
    model = StudentProfile
    template_name = 'studentprofile_list.html'
    context_object_name = 'student_profiles'

class StudentProfileDetailView(DetailView):
    model = StudentProfile
    template_name = 'studentprofile_detail.html'
    context_object_name = 'student_profile'

class StudentProfileCreateView(AdminRequiredMixin,StaffRequiredMixin,CreateView):
    model = StudentProfile
    template_name = 'studentprofile_form.html'
    fields = ['user', 'department', 'roll_number', 'admission_date']
    success_url = reverse_lazy('studentprofile_list')

class StudentProfileUpdateView(AdminRequiredMixin,StaffRequiredMixin,UpdateView):
    model = StudentProfile
    template_name = 'studentprofile_form.html'
    fields = ['user', 'department', 'roll_number', 'admission_date']
    success_url = reverse_lazy('studentprofile_list')

class StudentProfileDeleteView(AdminRequiredMixin,StaffRequiredMixin,DeleteView):
    model = StudentProfile
    template_name = 'studentprofile_confirm_delete.html'
    success_url = reverse_lazy('studentprofile_list')

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class CourseCreateView(AdminRequiredMixin,CreateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['name', 'department', 'credits']
    success_url = reverse_lazy('course_list')

class CourseUpdateView(AdminRequiredMixin,UpdateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['name', 'department', 'credits']
    success_url = reverse_lazy('course_list')

class CourseDeleteView(AdminRequiredMixin,DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course_list')


class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list.html'
    context_object_name = 'attendances'

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'
    context_object_name = 'attendance'

class AttendanceCreateView(AdminRequiredMixin,StaffRequiredMixin,CreateView):
    model = Attendance
    template_name = 'attendance_form.html'
    fields = ['student', 'course', 'date', 'status']
    success_url = reverse_lazy('attendance_list')

class AttendanceUpdateView(AdminRequiredMixin,StaffRequiredMixin,UpdateView):
    model = Attendance
    template_name = 'attendance_form.html'
    fields = ['student', 'course', 'date', 'status']
    success_url = reverse_lazy('attendance_list')

class AttendanceDeleteView(AdminRequiredMixin,DeleteView):
    model = Attendance
    template_name = 'attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance_list')

class TimetableListView(ListView):
    model = Timetable
    template_name = 'timetable_list.html'
    context_object_name = 'timetables'

class TimetableDetailView(DetailView):
    model = Timetable
    template_name = 'timetable_detail.html'
    context_object_name = 'timetable'

class TimetableCreateView(AdminRequiredMixin,StaffRequiredMixin,CreateView):
    model = Timetable
    template_name = 'timetable_form.html'
    fields = ['course', 'staff', 'day_of_week', 'start_time', 'end_time']
    success_url = reverse_lazy('timetable_list')

class TimetableUpdateView(AdminRequiredMixin,StaffRequiredMixin,UpdateView):
    model = Timetable
    template_name = 'timetable_form.html'
    fields = ['course', 'staff', 'day_of_week', 'start_time', 'end_time']
    success_url = reverse_lazy('timetable_list')

class TimetableDeleteView(AdminRequiredMixin,StaffRequiredMixin,DeleteView):
    model = Timetable
    template_name = 'timetable_confirm_delete.html'
    success_url = reverse_lazy('timetable_list')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Basic statistics
        context['department_count'] = Department.objects.count()
        context['staff_count'] = StaffProfile.objects.count()
        context['student_count'] = StudentProfile.objects.count()
        context['course_count'] = Course.objects.count()
        context['attendance_count'] = Attendance.objects.count()

        # Exams & Results
        context['exam_count'] = Exam.objects.count()
        context['exam_result_count'] = ExamResult.objects.count()

        # Timetable
        context['upcoming_timetable'] = Timetable.objects.all().order_by('day_of_week', 'start_time')[:5]

        # Recent activities (optional)
        context['recent_attendance'] = Attendance.objects.all().order_by('-date')[:5]
        context['recent_exams'] = Exam.objects.all().order_by('-date')[:5]

        # You can add more context as per your needs
        return context
