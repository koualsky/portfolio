from django.shortcuts import render


def work(request):
    text = 'One day, there will be so many pages...'
    return render(request, 'sites/work.html', {'text': text})


def about(request):
    return render(request, 'sites/about.html')






# now add animate to logo...