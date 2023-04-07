from django.shortcuts import render
import datetime


# Create your views here.
# Request -> response (request handler)


def show_time(request):
    maintenant = datetime.datetime.now()
    context = {'maintenant': maintenant}
    return render(request, 'showtime.html', context)
