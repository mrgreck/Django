from django import template

register = template.Library()

# запрещённые слова
cens = [
    'алкоголь'
]


@register.filter(name='censor')
def censor(value, arg):
    if cens:
        for i in cens:
            value = value.replace(i, '*' * len(i))

    # слова запрешённые через шаблон
    if arg:
        arg = arg.split()
        for y in arg:
            value = value.replace(y, '*' * len(y))

    return value
