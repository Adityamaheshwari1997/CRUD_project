from django.db import models


# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=50)
    mail = models.EmailField()
    emobile = models.CharField(max_length=10)


    def __str__(self):
        return "%s %s %s %s" % (self.eid, self.ename, self.mail, self.emobile)
