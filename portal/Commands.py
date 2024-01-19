# 1) Создать двух пользователей (с помощью метода User.objects.create_user('username')).
#
# u1 = User.objects.create_user('Василий')        'Тестовая команда'
# u2 = User.objects.create_user('Константин')     'тестовая команда'
# u3 = User.objects.create_user('Михаил')
# u4 = User.objects.create_user('Данил')
#
#
#
# 2) Создать два объекта модели Author, связанные с пользователями.
#
# a1 = Author.objects.create(user=u1)
# a2 = a1 = Author.objects.create(user=u2)
#
#
# 3) Добавить 4 категории в модель Category.
#
# cat1 = Category.objects.create(name='Спорт')
# cat2 = Category.objects.create(name='Политика')
# cat3 = Category.objects.create(name='Погода')
# cat4 = Category.objects.create(name='Форум')
#
#
#
#
# 4) Добавить 2 статьи и 1 новость.
#
# Post.objects.create(author_id=1,post_news='AR', category=2, post='Пост имя', text='Тут текст статьи')    'Тестовая команда, не сразу понял как сделать'
# Post.objects.create(author_id=2,post_news='AR',post='Факты о погоде', text='На планете Земля самая высокая температура, когда-либо зарегистрированная, составила 56,7 градуса Цельсия. Это произошло 10 июля 1913 года в Долине Смерти, Калифорния, США.')
# Post.objects.create(author_id=1,post_news='NE',post='Валюта', text='Аналитик считает, что в первом квартале российская валюта способна укрепиться до 85 за доллар, 93 за евро и 11,7 за юань.')
#
#
# 5) Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
#
#
# PostCategory.objects.create(category_ct_id=2, post_ps_id=2)
# PostCategory.objects.create(category_ct_id=1, post_ps_id=3)
#
#
#
#
# 6) Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
#
#
# Comment.objects.create(text_comment='Отличная новость',user_id=1,comment_post_id=2)
# Comment.objects.create(text_comment='Тут ничего интересного,расходимся',user_id=1,comment_post_id=1)
# Comment.objects.create(text_comment='Где-то жара, а у нас -35!!!',user_id=2,comment_post_id=2)
# Comment.objects.create(text_comment='Мои финансы, поют романсы',user_id=4,comment_post_id=3)
#
#
#
#
# 7) Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
#
# post = Post.objects.all()
# post[0].like()
# post[1].like()
# post[1].dislike()
# post[2].dislike()
#
#
# comments = Comment.objects.all()
# comments[0].like()
# comments[1].like()
# comments[1].like()
# comments[1].like()
# comments[1].dislike()
#
#
#
# 8)Обновить рейтинги пользователей.
#
#
#
# authors=Author.objects.all()
# authors[0].uptade_rating()
# authors[1].uptade_rating()



# 9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта)
#
# Author.objects.all().order_by('-rating').values('user_id__username','rating')[0]




# 10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
#
# b=Post.objects.all().order_by('-rating_post').values('post_time','author_id__user_id__username','rating_post','text')[0]
# b['preview'] = Post.objects.all().order_by('-rating_post').first().preview()
#
# 11) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
#
# Comment.objects.filter(comment_post__rating_post=Post.objects.all().order_by('-rating_post')[0].rating_post).values('time_comment','user__userna
# me','rating_comment','text_comment')