import challenges
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    'january': 'Eat healthy food for entire month.',
    'february': 'Walk 20 minutes twice a day.',
    'march': 'Learn Django for 2 hours a day.',
    'april': 'Eat healthy food for entire month.',
    'may': 'Walk 20 minutes twice a day.',
    'june': 'Learn Django for 2 hours a day.',
    'july': 'Eat healthy food for entire month.',
    'august': 'Walk 20 minutes twice a day.',
    'september': 'Learn Django for 2 hours a day.',
    'october': 'Eat healthy food for entire month.',
    'november': 'Walk 20 minutes twice a day.',
    'december': None,

}


def index(request):
    # list_items = ''
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitlized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitlized_month}</a></li>'

    # response_data = f'<ul>{list_items}</ul>'
    # return HttpResponse(response_data)
    return render(request, 'challenges/index.html', {
        'months': months,
    })


def january(request):
    return HttpResponse('Eat healthy food for entire month.')


def february(request):
    return HttpResponse('Walk 20 minutes twice a day.')


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month_name': month
        })
        # response_data = f'<h1>{challenge_text}</h1>'
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('This month is not supported.')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
