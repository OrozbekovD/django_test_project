from django.contrib import admin
from blog.models import Post, Author, Category, User, Comments

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(User)