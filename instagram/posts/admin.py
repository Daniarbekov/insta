from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', )
    fields = ('id', 'image', 'description')
    readonly_fields = ('id',)


admin.site.register(Post, PostAdmin)