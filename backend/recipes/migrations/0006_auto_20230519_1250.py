# Generated by Django 3.2.16 on 2023-05-19 05:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0005_auto_20230519_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': 'Список покупок', 'verbose_name_plural': 'Список покупок'},
        ),
        migrations.RemoveConstraint(
            model_name='shoppingcart',
            name='unique_shopping_cart',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение - 1')], verbose_name='Количество ингредиента'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingcart', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingcart', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name', 'measurement_unit'), name='unique_ingredient_model'),
        ),
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('name', 'author'), name='unique_recipe_model'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_shoppingcarts'),
        ),
    ]