from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)


class BaseAdminSettings(admin.ModelAdmin):
    """Кастомная админпанель"""
    empty_value_display = '-пусто-'
    list_filter = ('author', 'name', 'tags')


@admin.register(Tag)
class TagAdmin(BaseAdminSettings):
    """Кастомная админпанель для тегов"""
    list_display = (
        'name',
        'color',
        'slug'
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(BaseAdminSettings):
    """Кастомная админпанель для ингридиентов"""
    list_display = (
        'name',
        'measurement_unit'
    )
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(BaseAdminSettings):
    """Кастомная админпанель для рецепта"""
    list_display = (
        'name',
        'author',
        'added_in_favorites'
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('added_in_favorites',)
    filter_horizontal = ('tags',)

    def added_in_favorites(self, obj):
        return obj.favorites.all().count()

    added_in_favorites.short_description = 'Количество добавлений в избранное'


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    """Кастомная админпанель для ингридиентов в рецептах"""
    list_display = (
        'ingredient',
        'amount',
    )
    list_filter = ('ingredient',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Кастомная админ панель для избранного"""
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Кастомная админпанель для изранных рецептов"""
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    search_fields = ('user',)
