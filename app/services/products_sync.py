from sqlite3 import SQLITE_ROW

from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError

from app.database.db_config import Session
from app.models.product import Product


def get_products():
    try:
        with Session() as session:
            result = session.execute(
                select(Product.user_id, Product.product_url, Product.last_price, Product.desired_price))
            return [row for row in result.fetchall()]
    except SQLAlchemyError as ex:
        # ОТправляем письмо хозяину с ощибкой ex
        return []


def update_product(article, new_price):
    try:
        with Session() as session:
            result = session.execute(select(Product).where(Product.product_url == article))
            product = result.scalar_one_or_none()
            product.last_price = new_price
            session.commit()
    except SQLAlchemyError as ex:
        # ОТправляем письмо хозяину с ощибкой ex
        pass
