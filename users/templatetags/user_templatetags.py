from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django import template

register = template.Library()


@register.simple_tag
def BizzFuzz(num):
    status = ''

    if num % 3 == 0:
        status += 'Bizz'
    if num % 5 == 0:
        status += 'Fuzz'
    if not status:
        status = str(num)

    return status


@register.simple_tag
def is_allowed(birthday):
    age = relativedelta(timezone.now().date(), birthday).years
    status = 'Allowed' if age > 13 else 'Blocked'

    return status



