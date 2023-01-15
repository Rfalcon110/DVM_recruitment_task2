from django.shortcuts import render,redirect
from.models import Quiz,Question,Result
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from.forms import addQuestionform,addquizform


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
        total=len(question)
        for q in question:
            if q.answer!=request.POST.get(q.question_text):
                wrong1+=1
            else:
                correct1+=1 
        request.user.result_set.create(quiz=quiz1,correct=correct1,wrong=wrong1,total=len(question),quiz_given=True)
        result=Result.objects.get(user=request.user,quiz=quiz1)
        context={
            'correct':correct1,
            'wrong':wrong1,
            'total':result.total
        }
        
        return render(request,'quiz/result.html',context)
    else:
        if request.user.result_set.filter(quiz=quiz1,user=request.user):
            result=Result
            result=request.user.result_set.get(quiz=quiz1,user=request.user)
            context={
                'correct':result.correct,
                'wrong':result.wrong,
                'total':result.total
            }
            return  render(request,'quiz/result.html',context)
        else:
            context={
                'question_list':question,
                'quizz':quiz1
            }
            return render(request,'quiz/question.html',context)


def addQuestion(request):    
    if request.user.has_perm('quizapp.add_question'):
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
    if request.user.has_perm('quizapp.add_quiz'):
        form=addquizform(request.POST)
        if(request.method=='POST'):
            if(form.is_valid()):
                form.save()
                return redirect('addquestion')
        else:
            context={
                'form':form
            }
            return render(request,'quiz/addquiz.html',context)
    else:
        return redirect('index')


def editquestion(request,quiz_name1,id):
    if request.user.has_perm('quizapp.change_question'):
        
        form=addQuestionform(request.POST)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            question=Question.objects.get(id=id)
            form=addQuestionform(instance=question)
            question.delete()
            return render(request,'quiz/addQuestion.html',{'form':form})


def edit_index(request):
    if request.user.has_perm('quizapp.change_quiz'):
        quiz_list=Quiz.objects.all()
        context={
            'quiz_list': quiz_list
        }
        return render(request,'quiz/index_edit.html',context)
    else:
        return redirect('index')


def edit_quiz(request,quiz_name1):
    if request.user.has_perm('quizapp.change_question'):
        quiz1=Quiz.objects.get(quiz_name=quiz_name1)
        question=Question.objects.filter(quiz=quiz1)
        context={
                    'question_list':question,
                    'quizz':quiz1
                }
        return render(request,'quiz/quiz_edit.html',context)
    else:
        return redirect('index')