from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    fulltext=request.GET['fulltext']
    word=fulltext.split()
    a={}
    for i in word:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    l=[[k,v] for k,v in a.items()]
    l.sort(key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(word),'worddis':l})
