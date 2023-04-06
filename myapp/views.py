from django.shortcuts import render
import datetime


# Create your views here.
# Request -> response (request handler)


def say_hello(request):
    maintenant = datetime.datetime.now()
    context = {'maintenant': maintenant}
    return render(request, 'hello.html', context)
