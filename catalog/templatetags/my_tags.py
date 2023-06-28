from django import template

register = template.Library()


@register.filter()  # Создание фильтра
def mediapath(text):
    if text:
        return f"/media/{text}"
    else:
        return '#'