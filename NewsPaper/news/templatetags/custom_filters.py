from django import template


register = template.Library()

censored_words = ['насрала', 'выебет', 'хуйнуло', 'говном', 'блядь']

@register.filter()
def censor(value):
    if type(value) == str:
        for word in censored_words:
            if word in value:
                censor_words = f"{word[0]}{''.join(['*' for word in range(len(word)-1)])}"
                value = value.replace(word, censor_words)
            elif word.capitalize() in value:
                censor_words = f"{word.capitalize()[0]}{''.join(['*' for word in range(len(word)-1)])}"
                value = value.replace(word.capitalize(), censor_words)
        return value
