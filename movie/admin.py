from django.contrib import admin
from .models import Movie, Actor, Categories, Review, IdNumber


class InlineReview(admin.StackedInline):
    model = Review
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name', 'likes', 'actors__first_name', 'actors__id_name__number')
    list_display = ('name', 'watch_count', 'likes', 'rate', 'production_date', 'my_custom_list_display_field')
    readonly_fields = ('my_custom_list_display_field', 'likes')
    inlines = [InlineReview]

    def my_custom_list_display_field(self, obj):
        if obj.likes and obj.watch_count:
            total = 100 * (obj.likes / obj.watch_count)
            return '{} %'.format(round(total))
        return '0'

    my_custom_list_display_field.short_description = 'Watch/Likes Rating'

    fieldsets = (
        ["Main Section", {"fields": ["name", "description"]}],
        [None, {
            "fields": ["likes", "watch_count", "rate", "my_custom_list_display_field"]
        }
         ],
        ["Attachment Section ", {'fields': ["poster", "video"]}],
        ["Actors Section", {'fields': ["actors"]}]
    )
    #
    # def has_delete_permission(self, request, obj=None):
    #     if request.user.username == 'mina':
    #         return True
    #     return False


admin.site.register(Movie, MovieAdmin)

admin.site.register(Actor)

admin.site.register(Categories)

admin.site.register(Review)

admin.site.register(IdNumber)
