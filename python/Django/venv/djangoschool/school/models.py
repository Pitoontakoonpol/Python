from django.db import models

class ExamScore(models.Model):

    allsubject = (('math', 'คณิตศาสตร์'),
                    ('sci', 'วิทยาศาสตร์'),
                    ('eng', 'ภาษาอังกฤษ'),
                    ('art', 'ศิลป์'),
                    ('physics', 'ฟิสิกส์'),
                    ('bio', 'ชีววิทยา')
                    )

    subject = models.CharField(max_length=100, choices=allsubject, default='math')
    studentName = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.studentName + ', ' + self.subject + ', ' + str(self.score)



