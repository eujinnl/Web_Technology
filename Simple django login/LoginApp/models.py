from django.db import models


class Users(models.Model):
    userid = models.CharField('userid', max_length=50,primary_key=True)
    username = models.CharField('username', max_length=50)
    department = models.CharField('department', max_length=50)

    @property
    def userinfo(self):
        return '{} {}'.format(self.username, self.department)

