from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import List

#ENTITY MODEL
class Product(db.Model):
    __tablename__ = "products"

    #attributes
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())

    #ORM Relationships
    subscription_details: Mapped["SubscriptionDetail"] = relationship(back_populates='product')

#Marshmallow Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "product_name", "description", "subscription_detail")