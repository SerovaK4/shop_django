from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Удаление всей информации из БД"""
        all_products = Product.objects.all()
        for item in all_products:
            item.delete()

        all_category = Category.objects.all()
        for item_c in all_category:
            item_c.delete()
        """Заполнение БД"""
        category_list = [
            {'id': '1', 'name': 'Мебель', 'description': 'Предметы комнатной обстановки'},
            {'id': '2', 'name': 'Техника', 'description': 'Средства труда'}

        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'id': '1', 'name': 'диван-кровать', 'description': 'и диван, и кровать', 'category': Category.objects.get(pk=1), 'price': '60000'},
            {'id': '2', 'name': 'стол', 'description': 'обеденный на 6 персон', 'category': Category.objects.get(pk=2), 'price': '40000'},
            {'id': '3', 'name': 'Телевизор', 'category': Category.objects.get(pk=1), 'price': '30000'}
        ]
        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(products_for_create)