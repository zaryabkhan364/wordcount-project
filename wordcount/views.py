from django.http import HttpResponse
from django.shortcuts import render
import operator
import json

def portfolio(request):
    return HttpResponse('<h1>I love programming.</h1>')

def homepage(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html') 

def count(request):

    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:    
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)        

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(word_list), 'sorted_words':sorted_words})


def count1(request):
    return render(request, 'count1.html')
