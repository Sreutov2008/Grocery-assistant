import logging
import csv

from accessify import private

from django.core.management.base import BaseCommand

from recipes.models import Ingredient

MESSAGE = 'Данные успешно загружены в таблицу'

logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w'
)


class Command(BaseCommand):
    """Менеджкоманда для загрузки ингридиентов в БД"""
    def handle(self, *args, **options):
        self.import_ingredients()
        logging.info('Загрузка данных завершена')

    @private
    def import_ingredients(self, file='ingredients.csv'):
        logging.info(f'Загрузка данных из {file} в базу:')
        file_path = f'./data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                status, created = Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )
