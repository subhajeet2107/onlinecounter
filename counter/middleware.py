from counter.models import Counter
from datetime import datetime, time

class CounterMiddleware(object):
    def process_request(self, request):
        now_time = datetime.now().time()
        visitor_ip = self.get_client_ip(request)
        online, create = Counter.objects.get_or_create(ip=visitor_ip)
        online.visited_time = now_time
        online.save()
        request.online = self

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip