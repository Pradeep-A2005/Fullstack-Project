from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

# Student Model
class Student(models.Model):
    ptac_id = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)  
    academic_year = models.CharField(max_length=20)  
    semester = models.CharField(max_length=10)  
    project_category = models.CharField(max_length=100)  
    project_title = models.TextField()  
    abstract_file = models.FileField(upload_to='abstracts/', blank=True, null=True)

    def __str__(self):
        return f"{self.ptac_id} - {self.name}"


# AdminMark Model
class AdminMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    initial_mark = models.IntegerField(default=5)  
    final_mark = models.IntegerField(default=10)  
    plagiarism = models.IntegerField(choices=[(5, "5"), (3, "3"), (0, "0")], default=5)  
    work_log = models.IntegerField(choices=[(2, "2"), (4, "4"), (8, "8"), (10, "10")], default=2)   
    total_mark = models.IntegerField(blank=True, null=True)  

    def save(self, *args, **kwargs):
        self.total_mark = self.initial_mark + self.final_mark + self.plagiarism + self.work_log
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - Total: {self.total_mark}"


# TeamFeedbackMark Model (Min 0, Max 5)
class TeamFeedbackMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    explanation = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # Min-0, Max-5  
    novelty = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # Min-0, Max-5  
    plagiarism = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # Min-0, Max-5  
    originality = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # Min-0, Max-5  
    innovation = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # Min-0, Max-5  
    qna = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # Min-0, Max-5  
    total_mark = models.IntegerField(blank=True, null=True)  

    def save(self, *args, **kwargs):
        self.total_mark = self.explanation + self.novelty + self.plagiarism + self.originality + self.innovation + self.qna
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - Total: {self.total_mark}"


# ReviewerMark Model (Min 0, Max 10)
class ReviewerMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    reviewer_name = models.CharField(max_length=255, default="default")  
    explanation_objectives = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])   
    originality_novelty = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])   
    technical_complexity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])   
    ethical_standards = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])   
    problem_effectiveness = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])  
    team_collaboration = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])    
    innovation_creativity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)]) 
    impact_scalability = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])  
    technology_usage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])  
    qna_quality = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])  
    total_mark = models.IntegerField(blank=True, null=True)  
    mark_provided_date = models.DateTimeField(default=now)  

    def save(self, *args, **kwargs):
        self.total_mark = (
            self.explanation_objectives
            + self.originality_novelty
            + self.technical_complexity
            + self.ethical_standards
            + self.problem_effectiveness
            + self.team_collaboration
            + self.innovation_creativity
            + self.impact_scalability
            + self.technology_usage
            + self.qna_quality
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - Total: {self.total_mark}"
