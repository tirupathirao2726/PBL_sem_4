from django.db import models
# Create your models here.
class CreatedDatabases(models.Model):
    program=models.CharField(max_length=10)
    regulation=models.CharField(max_length=5)
    semister=models.CharField(max_length=10)
    examtype=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True)
    no_of_branches_result_user_add=models.IntegerField(default=0)
    is_published=models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+"    "+self.program+"       "+self.regulation+"        "+self.semister+"        "+self.examtype+"       "+str(self.created_date)



class Adding_branch(models.Model):
    added_branch_file=models.FileField(upload_to='csv_files/')
    added_branch_name=models.CharField(max_length=30)
    table_name=models.CharField(max_length=10,null=True)
    CDid=models.IntegerField()

class Published_Databases(models.Model):
    CrData_id=models.IntegerField()
    is_published=models.CharField(max_length=5,default='NO')

