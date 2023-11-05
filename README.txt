1. Создать двух пользователей (с помощью метода User.objects.create_user('username')).
user1 = User.objects.create.user(username='Tom')
user2 = User.objects.create.user(username='Bob')

2. Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=user1)
Author.objects.create(authorUser=user2)

3. Добавить 4 категории в модель Category.
Category.objects.create("IT")
Category.objects.get(id=1)
Category.objects.create("Politics")
Category.objects.get(id=2)
Category.objects.create("Education")
Category.objects.get(id=3)
Category.objects.create("Wars")
Category.objects.get(id=4)

4. Добавить 2 статьи и 1 новость.
Post.objects.create(author=author, categoryType='AR', title='title1', text='text1')
Post.objects.get(id=1)
Post.objects.create(author=author, categoryType='AR', title='title2', text='text2')
Post.objects.get(id=2)
Post.objects.create(author=author, categoryType='NW', title='title3', text='text3')
Post.objects.get(id=3)

5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentPost=Post.object.get(id=1), commentUser=Author.objects.get(id=1), text='text1')
Comment.objects.create(commentPost=Post.object.get(id=2), commentUser=Author.objects.get(id=2), text='text2')
Comment.objects.create(commentPost=Post.object.get(id=3), commentUser=Author.objects.get(id=1), text='text3')
Comment.objects.create(commentPost=Post.object.get(id=1), commentUser=Author.objects.get(id=2), text='text4')
Comment.objects.create(commentPost=Post.object.get(id=2), commentUser=Author.objects.get(id=1), text='text3')


7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).dislike()

Comment.objects.get(id=1).rating
Comment.objects.get(id=2).rating
Comment.objects.get(id=3).rating

8. Обновить рейтинги пользователей.
a1 = Author.objects.get(id=1)
a1.update.rating()
a2 = Author.objects.get(id=2)
a2.update.rating()
a3 = Author.objects.get(id=3)
a4.update.rating()

9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
a = Author.objects.order_by('-ratingAuthor')[:1]

for i in a:
	i.ratingAuthor
	i.authorUser.username

10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
a = Post.objects.order_by('-rating')[:1]

for i in a:
	i.Post.rating
	i.authorUser.username
	i.Post.title
	i.preview()

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
a = Post.objects.get(id=1)

for i in a:
	i.dateCreation
	i.author
	i.rating
	i.text
