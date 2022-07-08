from datetime import timedelta as td
from django.utils import timezone
from django.conf import settings
from django.db.models.expressions import F    
from .models import User

from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

class LastUserActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    KEY = "last-activity"

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            last_activity = request.session.get(self.KEY)
            if last_activity:
                last_activity = datetime.strptime(last_activity, "%Y-%m-%dT%H:%M:%S.%f%z")
            # If key is old enough, update database.
            too_old_time = timezone.now() - td(seconds=settings.LAST_ACTIVITY_INTERVAL_SECS)
            if last_activity and last_activity < too_old_time:
                User.objects.filter(id=request.user.pk).update(
                        last_login=timezone.now(),
                        login_count=F('login_count') + 1)

            request.session[self.KEY] = json_serial(timezone.now())

        return None