import csv
from django.core.management.base import BaseCommand
from marks.models import Student  # Adjust the import according to your model

class Command(BaseCommand):
    help = 'Import student projects from CSV'

    def handle(self, *args, **kwargs):
        file_path = "C:/Users/Administrator/Downloads/student_projects.csv"


        # Open and read the CSV file
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            # Debug: Print the column names
            print(f"CSV Headers: {reader.fieldnames}")

            for row in reader:
                print(f"Row: {row}")  # Debug: print each row to verify content

                # Check if PTAC_ID exists in the row (update the name to match CSV)
                if 'PTAC-ID' in row:
                    Student.objects.update_or_create(
                        ptac_id=row['PTAC-ID'],  # Use 'PTAC-ID' here
                        defaults={
                            'name': row['Student Name'],
                            'academic_year': row['Academic Year'],
                            'semester': row['Semester'],
                            'project_category': row['Project Category'],
                            'project_title': row['Project Title'],
                        }
                    )
                    self.stdout.write(self.style.SUCCESS(f"Successfully imported student {row['PTAC-ID']}"))
                else:
                    self.stdout.write(self.style.ERROR("Missing PTAC_ID in row"))

