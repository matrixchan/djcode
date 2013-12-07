from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from django.http import Http404
from django.core.urlresolvers import reverse

from polls.models import Poll,Choice


# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list':latest_poll_list}
    return render(request,'polls/index.html',context)

    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello,world.You're at the poll index.")

def detail(request,poll_id):
    '''try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request,'poll/detail.html',{'poll':poll})
    #return HttpResponse("You're looking at poll %s." % poll_id)'''
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})



def results(request,poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})

def vote(request,poll_id):
    p = get_object_or_404(Poll,pk = poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'poll':p,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args = (p.id,)))
    #return HttpResponse("You're voting on poll %s." % poll_id)

