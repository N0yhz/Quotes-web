# templatetags/quote_tags.py
from django import template
from django.db.models import Count
from quotes.models import Tag

register = template.Library()

@register.inclusion_tag('quotes/top_tags.html')
def top_ten_tags():
    tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    return {'tags': tags}