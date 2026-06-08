from sqlalchemy import select, update

from app.database.db_config import Session
from app.models.product import Product


def get_products():
    with Session() as session:
        result = session.execute(
            select(Product.user_id, Product.product_url, Product.last_price, Product.desired_price))
        return [row for row in result.fetchall()]


def update_product(article, new_price):
    with Session() as session:
        result = session.execute(select(Product).where(Product.product_url == article))
        product = result.scalar_one_or_none()
        product.last_price = new_price
        session.commit()
