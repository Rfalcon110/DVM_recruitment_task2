
from django.forms import ModelForm
from .models import *

class addQuestionform(ModelForm):
    class Meta:
        model=Question
        fields="__all__"
class addquizform(ModelForm):
    class Meta:
        model=Quiz
        fields='__all__'       
