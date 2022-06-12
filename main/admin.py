from django.contrib import admin
from main.models import Tag, Category, Post, Comments, Settings

admin.site.register(Comments)
admin.site.register(Settings)

admin.site.register(Post,
    prepopulated_fields={'slug': ('title',)}
)

admin.site.register(Category,
    prepopulated_fields={'slug': ('name',)}
)

admin.site.register(Tag,
    prepopulated_fields={'slug': ('name',)}
)

# Register your models here.

