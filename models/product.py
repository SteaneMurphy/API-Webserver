from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text

class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())
    license: Mapped[str] = mapped_column(String(100))                                   #determine using JWT

    plan_product: Mapped["PlanProduct"] = relationship(back_populates='product')

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "product_name", "description", "license")