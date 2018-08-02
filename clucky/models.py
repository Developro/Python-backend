# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnswerVotes(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    answer = models.ForeignKey('Answers', models.DO_NOTHING)
    vote = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_votes'
        unique_together = (('user', 'answer'),)


class Answers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    answer = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class Categories(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class QuestionVotes(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    vote = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_votes'
        unique_together = (('user', 'question'),)


class Questions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    subject = models.CharField(max_length=255)
    question = models.TextField()
    views = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class QuestionsCategories(models.Model):
    question = models.ForeignKey(Questions, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_categories'
        unique_together = (('question', 'category'),)


class QuestionsTags(models.Model):
    question = models.ForeignKey(Questions, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey('Tags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_tags'
        unique_together = (('question', 'tag'),)


class Tags(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tags'



