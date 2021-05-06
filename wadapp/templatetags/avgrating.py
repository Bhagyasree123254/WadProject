from django import template
register = template.Library()

@register.filter(name='avg_rating')
def avg_rating(reviewsn,bookname):
    sum = 0
    count = 0
    for i in reviewsn:
        if bookname == i.bookname:
            count = count+1
            sum = sum+i.rating
    if count:
        sum = sum/count
        sum=round(sum,2)
        return sum
    else:
        a = 'No ratings till now'
        return a
@register.filter(name='count')
def count(reviewsn,bookname):
    count = 0
    for i in reviewsn:
        if bookname == i.bookname:
            count = count+1
    if count:
        return count
    else:
        a='No reviews till now'
        return a