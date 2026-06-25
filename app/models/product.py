from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.db_config import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    marketplace = Column(String)
    article = Column(String)
    desired_price = Column(Integer)
    last_price = Column(Integer, default=0)
    product_name = Column(String)

    user = relationship("User", back_populates="products")
