from django.shortcuts import render, redirect


def work(request):
    """
    text = ''
    return render(request, 'sites/work.html', {'text': text})
    """
    return redirect('about')


def about(request):
    return render(request, 'sites/about.html')


# now add animate to logo...
