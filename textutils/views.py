from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('''<h1>About Kids</h1> <a href="http://127.0.0.1:8000/"> Back</a>''')

def analyze(request):
    #for getting checkbox values
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    lineremover = request.GET.get('lineremover', 'off')


    #for checking checkbox values
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if lineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed+char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)
