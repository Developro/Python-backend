from django.db import models
from clusers.models import User

# Create your models here.


class AnswerVote(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    answer = models.ForeignKey('Answer', models.DO_NOTHING)
    vote = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_votes'
        unique_together = (('user', 'answer'),)


class Answer(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    question = models.ForeignKey('Question', models.DO_NOTHING)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'categories'
        verbose_name_plural = 'categories'


class QuestionVote(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    question = models.ForeignKey('Question', models.DO_NOTHING)
    vote = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_votes'
        unique_together = (('user', 'question'),)


class Question(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    tags = models.ManyToManyField('Tag', through='QuestionsTags')
    categories = models.ManyToManyField(Category, through='QuestionsCategories')
    subject = models.CharField(max_length=255)
    question = models.TextField()
    views = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class QuestionsCategories(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_categories'


class QuestionsTags(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    tag = models.ForeignKey('Tag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questions_tags'


class Tag(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'tags'
