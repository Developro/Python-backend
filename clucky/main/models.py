from django.db import models
from clucky.clusers.models import Users

# Create your models here.

# Эти модели сгенерированы автоматически, необходимо всё перепроверить


class Answer(models.Model):
    answer = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey('Questions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class Question(models.Model):
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
    question = models.ForeignKey(Question, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_categories'
        unique_together = (('question', 'category'),)


class QuestionsTags(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    question = models.ForeignKey(Question, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey('Tags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_tags'
        unique_together = (('question', 'tag'),)


class Tag(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tags'


class Vote(models.Model):
    vote = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    answer = models.ForeignKey(Answer, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votes'
