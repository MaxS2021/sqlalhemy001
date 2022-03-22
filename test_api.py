from requests import get, post, delete

print(get('http://localhost:5000/api/v2/news').json())

#print(get('http://localhost:5000/api/v2/news/1').json())
#
# print(get('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(get('http://localhost:5000/api/news/q').json())

# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
print(post('http://localhost:5000/api/v2/news',
           json={'title': 'Новость 4',
                 'content': 'Новость добавленная черес API V2',
                 'user_id': 2,
                 'is_private': False}).json())

# print(delete('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/news/4').json())

print(get('http://localhost:5000/api/news').json())