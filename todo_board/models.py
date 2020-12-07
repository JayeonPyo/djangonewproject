from django.db import models
from django.db.models import Max
# Create your models here.
class ProjectCode(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=4)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_code'


class TodoList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=4)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=1000, blank=True, null=True)  # Field name madelowercase.
    is_complete = models.IntegerField(db_column='IS_COMPLETE', blank=True, null=True)  # Field name made lowerase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.

    def todo_save(self):
        self.save()

#저장버튼을 누르면 바로 저장하지 않고 todo_save 함수를 호출하면 그제서야 저장하도록 함
#default로 db값을 넣어주기 위함
    class Meta:
        managed = False
        db_table = 'todo_list'
