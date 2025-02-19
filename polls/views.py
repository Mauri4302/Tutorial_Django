from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import  loader
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ' , '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    '''
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]
        # return Question.objects.filter(pub_date = timezone.now())

'''
def detail(request, question_id):
    return HttpResponse("Your're looking at question %s." % question_id)
'''
'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''
'''
def detail(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question': question}
'''
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

'''
def results(request, question_id):
    response = "Your're looking at the results of question %s."
    return HttpResponse(response % question_id)
'''
'''
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'q': question})
'''
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

'''
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))