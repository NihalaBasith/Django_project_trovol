from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Tuscany'
    dest1.desc = 'Tuscany is known for its landscapes, history, artistic legacy, and its influence on high culture. It is regarded as the birthplace of the Italian Renaissance and of the foundations of the Italian language.'
    dest1.img = 'packag1.jpg'
    dest1.name2 = 'Italy'
    dest1.price = '$ 1000.0'

    dest2 = Destination()
    dest2.name = 'Paris'
    dest2.desc = 'Paris is one of the most beautiful cities in the world. It is known worldwide for the Louvre Museum, Notre-Dame cathedral, and the Eiffel tower.'
    dest2.img = 'packag2.jpg'
    dest2.name2 = 'Italy'
    dest2.price = '$ 1000.0'

    dest3 = Destination()
    dest3.name = 'San Francisco'
    dest3.desc = 'San Francisco is famous for its Golden Gate Bridge, steep streets, Alcatraz, and full House. The thirteenth largest city in the United States also has some pretty interesting historical facts.'
    dest3.img = 'packag3.jpg'
    dest3.name2 = 'United States'
    dest3.price = '$ 2000.0'

    dest4 = Destination()
    dest4.name = 'Phuket'
    dest4.desc = 'Apart from the beautiful beaches, delicious foods, amazing nightlife, and adventure activities, Phuket is also known for its culture and amazing temples.'
    dest4.img = 'packag4.jpg'
    dest4.name2 = 'United States'
    dest4.price = '$ 2500.0'


    # dest1= Destination.objects.all()
    # dest2= Destination.objects.all()
    # dest3= Destination.objects.all()
    # dest4= Destination.objects.all()
    


    return render (request,'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3':dest3,'dest4':dest4})

def register(request):
    return render( 'register.html')