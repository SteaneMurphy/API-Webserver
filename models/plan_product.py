from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from marshmallow import fields
from typing import List

class PlanProduct(db.Model):
    __tablename__ = "plan_products"

    id: Mapped[int] = mapped_column(primary_key=True)

    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
    plan: Mapped["Plan"] = relationship(back_populates="plan_product") 

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped[List["Product"]] = relationship(back_populates="plan_product") 

class PlanProductSchema(ma.Schema):
    plan = fields.Nested("PlanSchema")
    product = fields.Nested("ProductSchema")

    class Meta:
        fields = ("id", "plan", "product")