from counter.models import Counter
from datetime import datetime, time

class CounterMiddleware(object):
    def process_request(self, request):
        now_time = datetime.now().time()
        online, create = Counter.objects.get_or_create(ip=request.META["REMOTE_ADDR"])
        if not create:
            online.visited_time = now_time
        online.save()
        request.online = self

    def total(self):
        total = Counter.objects.all().count()
        return total