from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Quiz,Question,Result
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from.forms import addQuestionform,addquizform
from django.contrib.auth.models import User
@login_required
def index(request):
        quiz_list=Quiz.objects.all()
        context={
            'quiz_list': quiz_list
        }
        return render(request,'quiz/index.html',context)
@login_required
def quiz(request,quiz_name1):
    quiz1=Quiz.objects.get(quiz_name=quiz_name1)
    question=Question.objects.filter(quiz=quiz1)
    if request.method=='POST':
        correct1=0
        wrong1=0
        for q in question:
            if q.answer!=request.POST.get(q.question_text):
                wrong1+=1
            else:
                correct1+=1 
        request.user.result_set.create(quiz=quiz1,correct=correct1,wrong=wrong1,total=len(question),quiz_given=True)
        
        context={
            'correct':correct1,
            'wrong':wrong1,
        }
        
        return render(request,'quiz/result.html',context)
    else:
        if request.user.result_set.filter(quiz=quiz1,user=request.user):
            result=Result
            result=request.user.result_set.get(quiz=quiz1,user=request.user)
            context={
                'correct':result.correct,
                'wrong':result.wrong
            }
            return  render(request,'quiz/result.html',context)
        else:
            context={
                'question_list':question,
                'quizz':quiz1
            }
            return render(request,'quiz/question.html',context)
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz/addQuestion.html',context)
    else: 
        return redirect('index') 
def addquiz(request):
    if request.user.is_staff:
        form=addquizform(request.POST)
        if(request.method=='POST'):
            if(form.is_valid()):
                form.save()
                return redirect('add_question')
        else:
            context={
                'form':form
            }
            return render(request,'quiz/addquiz.html',context)
    else:
        return redirect('index')
def editquizzes(request):
    if request.user.is_staff:
        form=addQuestionform(request.POST)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('index')

                           
        
        