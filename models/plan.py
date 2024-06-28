from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Float, Integer
from typing import List
from marshmallow import fields

#USER ENTITY MODEL
class Plan(db.Model):
    __tablename__ = "plans"

    #attributes
    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())
    price: Mapped[float] = mapped_column(Float())
    length: Mapped[int] = mapped_column(Integer())
    product_limit: Mapped[int] = mapped_column(Integer())                                     

    #ORM Relationships
    subscriptions: Mapped["Subscription"] = relationship(back_populates='plan')

#Marshmallow Schema
class PlanSchema(ma.Schema):
    class Meta:
        fields = ("id", "plan_name", "description", "price", "length", "product_limit")