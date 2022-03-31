from django.shortcuts import render

# Create your views here.
def WordCount(request):
    return render(request, 'WordCount.html')

def result(request):
    text = request.POST['text']
    wordcount  = len(text.split())
    total_len = len(text)
    no_blank_len = len(text.replace(' ',''))
    return render(request,'result.html', {
        'wordcount':wordcount,
        'total_len':total_len,
        'no_blank_len': no_blank_len})
