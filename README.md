# Music History API

##Description

This is a REST API created for the Music History Project. The API will be used to house information about Artist, Albums, Songs, and Genres. Clients can then pull this information down by making a simple URL call.

##Installation

1. Install Python 3.6.0. See instructions for download here:

    https://www.python.org/downloads/

3. Install pip

    `$ python -m pip install -U pip`

4. Install Django

    `$ pip install Django`
    
5. Install Django rest framework

    `$ pip install djangorestframework`

## How to Run

### From the Command Line in root project folder:

1. cd in to the main project folder:

`$ cd music_history/`

2. run migrate to setup database and install fixtures

`$ python manage.py migrate`

3. run the server

`$ python manage.py runserver`

4. Navigate to localhost in your browser `http://localhost:8000/`

## To login as admin

`username: admin`

`password: pass1234`

### Collections

```
* GET - http://127.0.0.1:8000/artist                returns all artists
* GET - http://127.0.0.1:8000/albums                returns all albums
* GET - http://127.0.0.1:8000/songs                 returns all songs
* GET - http://127.0.0.1:8000/genres                returns all genres
```

### Members
```
* GET - http://127.0.0.1:8000/artists/<id>          returns an artist by id
* GET - http://127.0.0.1:8000/albums/<id>           returns an album by id
* GET - http://127.0.0.1:8000/songs/<id>            returns a song by id
* GET - http://127.0.0.1:8000/genres/<id>           returns a genre by id
```

##Example
```
// http://localhost:8000/genres/1/?format=json

{
  "url": "http://localhost:8000/genres/1/?format=json",
  "title": "Rock"
}
```