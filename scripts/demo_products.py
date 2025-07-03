from products.models import Product, Category
from django.core.files import File
from pathlib import Path
from django.conf import settings
from django.utils.text import slugify

def run():
    if Product.objects.exists():
        print("🟡 Продукты уже есть. Пропуск.")
        return

    BASE_DIR = Path(settings.BASE_DIR)
    img_path = BASE_DIR / "media" / "products"

    # Обязательно указываем slug
    category, _ = Category.objects.get_or_create(
        name="Электроника",
        slug=slugify("Электроника")
    )

    products_data = [
        {
            "name": "Xiaomi 13T",
            "description": "AMOLED экран и камера Leica",
            "price": 45990,
            "image_file": img_path / "01_xiaomi.jpg"
        },
        {
            "name": "Sony WH-1000XM5",
            "description": "Наушники с шумоподавлением",
            "price": 32990,
            "image_file": img_path / "02_sony.jpg"
        },
        {
            "name": "MacBook Air M2",
            "description": "M2 чип и дисплей Retina",
            "price": 124990,
            "image_file": img_path / "03_macbook.jpg"
        }
    ]

    for item in products_data:
        product = Product(
            name=item["name"],
            description=item["description"],
            price=item["price"],
            category=category
        )
        if item["image_file"].exists():
            with open(item["image_file"], "rb") as f:
                product.image.save(item["image_file"].name, File(f), save=False)
        else:
            print(f"❌ Нет файла: {item['image_file']}")
        product.save()
        print(f"✅ Добавлен товар: {product.name}")
