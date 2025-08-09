from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'marks/index.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password) # type: ignore
        if user is not None:
            login(request, user) # type: ignore
            return redirect('admin_dash')  # Redirect to the admin dashboard on successful login
        else:
            # Handle invalid login
            return render(request, 'marks/admin_login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'marks/admin_login.html')

def admin_dash(request):
    return render(request, 'marks/admin_dash.html')

def reviewer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password) # type: ignore
        if user is not None:
            login(request, user) # type: ignore
            return redirect('reviewer_dashboard')  # Redirect to the admin dashboard on successful login
        else:
            # Handle invalid login
            return render(request, 'marks/reviewer_login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'marks/reviewer_login.html')

def admin_access(request):
    return render(request, 'marks/admin_access.html')

def admin_dash(request):
    return render(request, 'marks/admin_dash.html')

def Admin_mark(request):
    return render(request, 'marks/Admin_mark.html')

def admin_view(request):
    return render(request, 'marks/admin_view.html')

def review_mark(request):
    return render(request, 'marks/review_mark.html')

def review_view(request):
    return render(request, 'marks/review_view.html')

def reviewer_dashboard(request):
    return render(request, 'marks/reviewer_dashboard.html')

def select(request):
    return render(request, 'marks/select.html')

def select1(request):
    return render(request, 'marks/select1.html')

def team(request):
    return render(request, 'marks/team.html')


from django.shortcuts import render
from .models import Student

def student_selection(request):
    students = Student.objects.all()  # Fetch all student records
    return render(request, 'marks/select.html', {'students': students})

from django.shortcuts import render
from .models import Student

def student_selection1(request):
    students = Student.objects.all()  # Fetch all student records
    return render(request, 'marks/select1.html', {'students': students})



from django.shortcuts import render, redirect
from .models import AdminMark, Student

def admin_mark_view(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        initial_mark = int(request.POST.get('initialMark'))
        final_mark = int(request.POST.get('finalMark'))
        plagiarism = int(request.POST.get('plagiarism'))
        work_log = int(request.POST.get('workLog'))

        student = Student.objects.get(id=student_id)
        AdminMark.objects.create(
            student=student,
            initial_mark=initial_mark,
            final_mark=final_mark,
            plagiarism=plagiarism,
            work_log=work_log
        )
        return redirect('admin_view')  
    
    students = Student.objects.all()
    return render(request, 'Admin_mark.html', {'students': students})

# marks/views.py
from django.shortcuts import render
from .models import AdminMark

def admin_view(request):
    marks = AdminMark.objects.all()  # Replace this with your actual query if needed
    return render(request, 'marks/admin_view.html', {'marks': marks})



from django.shortcuts import render, redirect
from .models import TeamFeedbackMark, Student

# Handling form submission from team.html
def team_mark_view(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        explanation = int(request.POST.get('explanation'))
        novelty = int(request.POST.get('novelty'))
        plagiarism = int(request.POST.get('plagiarism'))
        originality = int(request.POST.get('originality'))
        innovation = int(request.POST.get('innovation'))
        qna = int(request.POST.get('qna'))

        student = Student.objects.get(id=student_id)
        # Create a new TeamFeedbackMark object and save it
        TeamFeedbackMark.objects.create(
            student=student,
            explanation=explanation,
            novelty=novelty,
            plagiarism=plagiarism,
            originality=originality,
            innovation=innovation,
            qna=qna
        )
        return redirect('review_view')  

    students = Student.objects.all() 
    return render(request, 'team.html', {'students': students})


# Rendering review data on review_view.html
def review_view(request):
    marks = TeamFeedbackMark.objects.all()  # Fetch all marks
    return render(request, 'marks/review_view.html', {'marks': marks})



from django.shortcuts import render, redirect
from .models import ReviewerMark, Student

def review_mark_view(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        marks = {
            'explanation_objectives': int(request.POST.get('mark1')),
            'originality_novelty': int(request.POST.get('mark2')),
            'technical_complexity': int(request.POST.get('mark3')),
            'ethical_standards': int(request.POST.get('mark4')),
            'problem_effectiveness': int(request.POST.get('mark5')),
            'team_collaboration': int(request.POST.get('mark6')),
            'innovation_creativity': int(request.POST.get('mark7')),
            'impact_scalability': int(request.POST.get('mark8')),
            'technology_usage': int(request.POST.get('mark9')),
            'qna_quality': int(request.POST.get('mark10')),
        }

        student = Student.objects.get(id=student_id)
        ReviewerMark.objects.create(student=student, **marks)
        return redirect('review_view')  # Redirect to the review view page after submission

    students = Student.objects.all()
    return render(request, 'review_mark.html', {'students': students})

def review_view(request):
    reviewer_marks = ReviewerMark.objects.all()
    return render(request, 'marks/review_view.html', {'marks': reviewer_marks})



#reviewer_view
from django.shortcuts import render
from .models import TeamFeedbackMark, ReviewerMark

def review_view(request):
    # Fetch all team feedback marks
    team_feedback_marks = TeamFeedbackMark.objects.all()
    
    # Fetch all reviewer marks
    reviewer_marks = ReviewerMark.objects.all()
    
    # Combine the data into a dictionary for easier access in the template
    combined_data = []
    for team_mark in team_feedback_marks:
        reviewer_mark = reviewer_marks.filter(student=team_mark.student).first()  # Match student
        combined_data.append({
            'ptac_id': team_mark.student.ptac_id,  
            'student': team_mark.student.name,
            'team_total_mark': team_mark.total_mark,
            'reviewer_total_mark': reviewer_mark.total_mark if reviewer_mark else 'N/A',
        })

    return render(request, 'marks/review_view.html', {'combined_data': combined_data})


from django.shortcuts import render
from .models import TeamFeedbackMark, ReviewerMark, AdminMark

def admin_access_view(request):
    # Fetch all admin marks
    admin_marks = AdminMark.objects.all()
    
    # Fetch all team feedback marks and reviewer marks
    team_feedback_marks = TeamFeedbackMark.objects.all()
    reviewer_marks = ReviewerMark.objects.all()
    
    # Prepare combined data
    combined_data = []
    for admin_mark in admin_marks:
        student = admin_mark.student
        team_mark = team_feedback_marks.filter(student=student).first()
        reviewer_mark = reviewer_marks.filter(student=student).first()

        # Perform the conversions
        team_communication_mark_converted = (
            (team_mark.total_mark / 30) * 10 if team_mark else 0
        )
        reviewer_mark_converted = (
            (reviewer_mark.total_mark / 100) * 60 if reviewer_mark else 0
        )

        # Calculate the total marks
        total_calculated_marks = (
            admin_mark.total_mark + team_communication_mark_converted + reviewer_mark_converted
        )

        combined_data.append({
            'student': student.name,
            'ptac_id': student.ptac_id,  
            'admin_mark': admin_mark.total_mark,
            'reviewer_name': reviewer_mark.reviewer_name if reviewer_mark else 'N/A',  
            'mark_provided_date': reviewer_mark.mark_provided_date if reviewer_mark else 'N/A',  
            'team_mark_converted': round(team_communication_mark_converted, 2),
            'reviewer_mark_converted': round(reviewer_mark_converted, 2),
            'total_calculated_marks': round(total_calculated_marks, 2),
        })

    return render(request, 'marks/admin_access.html', {'combined_data': combined_data})


# views.py

from django.shortcuts import render, redirect
from .models import Student, AdminMark

def admin_mark_entry(request):
    students = Student.objects.all()  # to show in dropdown

    if request.method == "POST":
        # Collect data from form
        student_id = request.POST.get("student")
        ptac_id = request.POST.get("ptacId")
        initial = int(request.POST.get("initialMark"))
        final = int(request.POST.get("finalMark"))
        plagiarism = int(request.POST.get("plagiarism"))
        work_log = int(request.POST.get("workLog"))

        # Calculate total
        total = initial + final + plagiarism + work_log

        # Save to database
        AdminMark.objects.create(
            student_id=student_id,
            ptac_id=ptac_id,
            initialMark=initial,
            finalMark=final,
            plagiarism=plagiarism,
            workLog=work_log,
            total=total
        )

        return redirect('admin_view')  # After saving, go to view page

    return render(request, 'marks/Admin_mark.html', {'students': students})
