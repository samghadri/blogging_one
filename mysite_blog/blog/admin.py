from django.contrib import admin
from .models import Post, Comment, ContactRequest, UserProfileInfo


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ContactRequest)
admin.site.register(UserProfileInfo)
