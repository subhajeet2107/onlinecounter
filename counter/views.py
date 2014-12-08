from django.shortcuts import render
from django.http import HttpResponse

from counter.models import Counter

# Create your views here.
def index(request):
	context = {'online_users': request.online.total}
	return render(request, 'counter/index.html',context)
