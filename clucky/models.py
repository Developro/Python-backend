# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answers(models.Model):
    answer = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey('Questions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class Categories(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class Questions(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length=255)
    views = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class QuestionsCategories(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    question = models.ForeignKey(Questions, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_categories'
        unique_together = (('question', 'category'),)


class QuestionsTags(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    question = models.ForeignKey(Questions, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey('Tags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_tags'
        unique_together = (('question', 'tag'),)


class Tags(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tags'


class Users(models.Model):
    login = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=64)
    access_token_hash = models.CharField(max_length=64, blank=True, null=True)
    acc_action_token_hash = models.CharField(max_length=64, blank=True, null=True)
    refresh_token_hash = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class Votes(models.Model):
    vote = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    answer = models.ForeignKey(Answers, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votes'
