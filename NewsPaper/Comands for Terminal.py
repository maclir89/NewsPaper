"""
1.	Создать двух пользователей (с помощью метода User.objects.create_user('username')).

user1 = User.objects.create_user('Username1')
user2 = User.objects.create_user('Username2')

2.	Создать два объекта модели Author, связанные с пользователями.

author1 = Author.objects.create(user_id=1)
author2 = Author.objects.create(user_id=2)

3.	Добавить 4 категории в модель Category.

cat1 = Category.objects.create(category_name='Category1')
cat2 = Category.objects.create(category_name='Category2')
cat3 = Category.objects.create(category_name='Category3')
cat4 = Category.objects.create(category_name='Category4')

4.	Добавить 2 статьи и 1 новость.

article1 = Post.objects.create(author_id=1, post_type=Post.article, title='Title1', text='Text1')
article2 = Post.objects.create(author_id=2, post_type=Post.article, title='Title2', text='Text2')
news1 = Post.objects.create(author_id=1, post_type=Post.news, title='Title3', text='Text3')

5.	Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

article1.category.add(cat1,cat2)
article1.category.add(cat2,cat3,cat4)
news1.category.add(cat1,cat3,cat4)

6.	Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

com1 = Comment.objects.create(text='Comment_text1',post_id=1,user_id=1)
com2 = Comment.objects.create(text='Comment_text2',post_id=2,user_id=1)
com3 = Comment.objects.create(text='Comment_text3',post_id=3,user_id=1)
com4 = Comment.objects.create(text='Comment_text4',post_id=1,user_id=2)
com5 = Comment.objects.create(text='Comment_text5',post_id=2,user_id=2)
com6 = Comment.objects.create(text='Comment_text6',post_id=3,user_id=2)

7.	Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

article1.like()      * 6 (+6)
article2.dislike()   * 12 (-12)
news1.like()         * 21 (+21)
com1.like()          * 5 (+5)
com2.like()          * 7 (+7)
com3.like()          * 9 (+9)
com4.dislike()       * 12 (-12)
com5.like()          * 3 (+3)
com6.dislike()       * 3 (-3)

8.	Обновить рейтинги пользователей.

author1.update_rating()
author2.update_rating()

9.	Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

Author.objects.all().order_by('rating').values('user__username','rating').last()
Author.objects.all().order_by('-rating').values('user__username','rating').first()

10.	Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках
 к этой статье.

Post.objects.order_by('-rating').values('time_create', 'author__user__username','rating', 'title').first()
Post.objects.order_by('-rating').first().preview()

11.	Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

Cоздаем переменную
best_post = Post.objects.order_by('-rating').first()
Выводим нужные поля
best_post.comment_set.all().values('time_create', 'user__username', 'rating', 'text')

"""