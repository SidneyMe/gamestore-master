from django.contrib import admin
from gamestore.models import User, Game, Payment, Tag
from ajax_select.admin import AjaxSelectAdmin
from gamestore.forms import CreateGameForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(AjaxSelectAdmin):
    form = CreateGameForm


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
