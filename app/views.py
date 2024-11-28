from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

# Topics Table
 
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics': topics}
    return render(request,'display_topics.html',d)


def insert_topics(request):
    to=input('Enter the Topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=to)
    if TO[1]:
        topics=Topic.objects.all()
        d={'topics': topics}
        return render(request,'display_topics.html',d)
    else:
        return HttpResponse('Topic_name already present TOPIC in table')


# Webpages:


def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages': webpages}
    return render(request,'display_webpages.html',d)


def insert_webpages(request):
    to=input('Enter the Topic_name: ')
    n=input('Enter the name: ')
    u=input('Enter the url: ')
    e=input('Enter the email: ')

    TO=Topic.objects.filter(topic_name=to)
    if TO:
        WO=Webpage.objects.get_or_create(topic_name=TO[0], name=n, url=u, email=e)
    if WO[1]:
        webpages=Webpage.objects.all()
        d={'webpages': webpages}
        return render(request,'display_webpages.html',d)
    else:
        return HttpResponse('WEbpage_data entered already present in WEBPAGE table')
    

# Access Record:

def display_access(request):
    access=Accessrecord.objects.all()
    d={'access': access}
    return render(request,'display_access.html',d)


def insert_access(request):
    to=input('Enter the Topic_name: ')
    n=input('Enter the name: ')
    u=input('Enter the url: ')
    e=input('Enter the email: ')
    a=input('Enter the author name: ')
    da=input('Enter the date: ')

    TO=Topic.objects.filter(topic_name=to)
    if TO:
        WO=Webpage.objects.filter(name=n)
    if WO:
        AO=Accessrecord.objects.get_or_create(name=WO[0], author=a, date=da)
        if AO[1]:
            access=Accessrecord.objects.all()
            d={'access': access}
            return render(request,'display_access.html',d)
        else:
            return HttpResponse('Access_data entered already present in ACCESS table')
    else:
        return HttpResponse('Webpage_data entered already present in WEBPAGE table')
    


def topicweb(request):
    PWTO=Topic.objects.prefetch_related('webpage_set').all()
    d={'PWTO': PWTO}
    return render(request, 'topicweb.html', context=d)


def webaccess(request):
    PWAO=Webpage.objects.prefetch_related('accessrecord_set').all()
    PWAO=Webpage.objects.prefetch_related('accessrecord_set').filter(name__startswith='L')
    d={'PWAO': PWAO}
    return render(request, 'webaccess.html', context=d)


def update_webpage(request):

    # update():

    # single data condition
    # Webpage.objects.filter(name='Daniel').update(name='Daniel Ricciardo')

    # multiple conditions
    # Webpage.objects.filter(topic_name='Formula 1').update(url='https://driversF1.com')

    #Zero conditions 
    # Webpage.objects.filter(name='Cristiano').update(name='Cristiano Ronaldo')

    # Parent table value updation ie: update(topic_name='Karate')
    # Karate is not present in parent table 'Topic'. Hence error is thrown.
    # Webpage.objects.filter(name='Conor Mcgregor').update(topic_name='Karate')

    # Parent table value updation ie: update(topic_name='FootBall') no error
    # Webpage.objects.filter(name='Conor Mcgregor').update(topic_name='FootBall')




    # update_or_create():

    # single condition
    # Webpage.objects.update_or_create(name='Mahindra Singj', defaults={'name': 'Mahi Dhoni'})

    # Multiple conditions give error in update_or_create() method because it internally uses get() method
    # for filtering of where conditions and we must also provide Parent table object for Foreign key column
    # TO=Topic.objects.filter(topic_name='Boxing')
    # Webpage.objects.update_or_create(topic_name=TO, defaults={'email': 'weluvbox@gmail.com'})


    # zero columns condition satisfied. Hence creates a new row
    TO=Topic.objects.filter(topic_name='FootBall')
    Webpage.objects.update_or_create(name='Cristiano Ronaldo', defaults={'topic_name': TO[0], 'url': 'https://cr7siuu.com', 'email': 'cristi7protu@gmail.com'})
    webpages=Webpage.objects.all()

    d={'webpages': webpages}
    return render(request, 'update_webpage.html', context=d)



def insert_webpage(request):
    TO=Topic.objects.all()
    if request.method=='POST':
        pass
    return render(request, 'insert_webpage.html', {'TO': TO})