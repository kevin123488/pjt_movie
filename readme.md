# 실행하기에 앞서



### final_back

```django
$ python -m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py loaddata movies/movies_data.json
$ python manage.py runserver
```



### final_front

.env.local 생성 후

```vue
VUE_APP_TMDB_API_KEY=
```

```vue
$ npm install
$ npm run serve
```