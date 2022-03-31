from django.shortcuts import render

# Create your views here.
def WordCount(request):
    return render(request, 'WordCount.html')

def result(request):
    text = request.POST['text']
    wordcount  = len(text.split())
    return render(request,'result.html', {'wordcount':wordcount})
