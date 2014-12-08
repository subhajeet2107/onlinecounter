from django.shortcuts import render
from django.http import HttpResponse

from counter.models import Counter

# Create your views here.
def index(request):
	total = Counter.objects.all().count()
	visitors = Counter.objects.all()
	context = {'total_online_users': total,'visitors_online':visitors}
	return render(request, 'counter/index.html',context)

def get_visitor_count(request):
	total = Counter.objects.all().count()
	return HttpResponse(total)
