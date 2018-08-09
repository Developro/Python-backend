from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question

        fields = ('user', 'tags', 'categories', 'subject', 'question', 'views')




