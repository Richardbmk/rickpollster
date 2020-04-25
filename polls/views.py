from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse 
from django.http import JsonResponse 

from . models import Question, Choice


# This is the Landing pge
def main(request):
    return render(request, 'polls/pages/home.html')


# This display all the questions
def index(request):
    latest_question = Question.objects.order_by('-pub_date')
    context = {'latest_question' : latest_question}
    return render (request, 'polls/poll/index.html', context)

# This show the question and the choices
def detail(request, pk):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise  Http404("Question does not exist")

    context = {'question' : question }

    return render(request, 'polls/poll/detail.html', context)



# This display the results
def results(request, pk):
  question = get_object_or_404(Question, id=pk)
  context = { 'question' : question }
  return render(request, 'polls/poll/results.html', context)


# Vote for a question choice
def vote(request, pk):
    #print(request.POST['choice'])
    question = get_object_or_404(Question, id=pk)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/poll/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)