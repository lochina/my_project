# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Wordauthors(models.Model):
    wordid = models.IntegerField()
    wordsource = models.TextField()

    class Meta:
        #managed = False
        db_table = 'wordAuthors'


class Words(models.Model):
    wordid = models.AutoField(primary_key=True)
    word = models.TextField()
    translation = models.TextField()

    class Meta:
        #managed = False
        db_table = 'words'
