from django.contrib import admin

from .models import Movie, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    readonly_fields = ('id',)


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    readonly_fields = ('id',)
    inlines = (CommentInLine,)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
