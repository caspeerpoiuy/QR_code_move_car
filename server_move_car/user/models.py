from django.db import models
from hashlib import sha1


def get_hash(str):
    sha = sha1()
    sha.update(str.encode("utf8"))
    return sha.sh.hexdigest()


class UserManger(models.Manager):
    def add_one_user(self,username,password):
        user = self.create(username,get_hash(password))
        return user

    def get_one_user(self,username,password):
        try:
            user = self.get(username=username, password=get_hash(password))
        except self.model.DoesNotExist:
            user = None
        return user

    def check_username(self,username):
        try:
            userexist = self.get(username=username)
        except self.model.DoesNotExist:
            userexist = None
        return userexist



class User(models.Model):
    username = models.CharField(max_length=30,verbose_name="用户名")
    password = models.CharField(max_length=30,verbose_name="密码")

    object = UserManger()

    class Meta:
        db_table = "User"
    