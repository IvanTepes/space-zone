from django.shortcuts import render
import requests
import json
# Create your views here.


def get_image():
    response = requests.get(
        'https://api.le-systeme-solaire.net/rest/planet')
    image = response.json()
    print(json.dumps(image, indent=4, sort_keys=True))
    return image






def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

