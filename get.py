import requests
import time

def get_image(url):
    exists = 'media/get'
    if not os.path.exists(exists):
        os.mkdir(exists)

    response = requests.get(url)
    if response.status_code == 200:
        filename = response.headers['Content-length'] + '.png'
        with open(exists + '/' + filename , 'wb') as file:
            file.write(response.content)

def main():
    image = input('enter image url --> ')
    get_image(image)
   


if __name__=='__main__':

    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    application = get_wsgi_application()

    main()