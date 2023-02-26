from django.db import models

# Create your models here.

class Admin_panel(models.Model):
    username = models.CharField('UserName',max_length=20)
    password = models.CharField('Password',max_length=8)
    email = models.EmailField()

    @staticmethod
    def get_Login_byusername(username):
        try:
            return Admin_panel.objects.get(username=username)
        except:
            return False


class UserRegistration(models.Model):

    QUALIFICATION_CHOICES = (
        ('10th', 'Matic pass or Below'),
        ('12th', '12th pass'),
        ('UG', 'Under graduate'),
        ('PG', 'Post graduate'),
        ('PHD', 'Doctor of Philosophy'),
    )

    name = models.CharField('NAME',max_length=50,default=" ",blank=True,null=True)
    email_id  = models.EmailField('EMAIL_ID',default=" ",blank=True,null=True)
    qualification = models.CharField('QUALIFICATION',max_length=10,choices=QUALIFICATION_CHOICES)
    address = models.CharField('ADDRESS',max_length=200)

    def __str__(self):
        return self.name