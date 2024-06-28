from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Float, Integer
from typing import List
from marshmallow import fields

class Plan(db.Model):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(100))                                 #determine plans that exist, start with four types
    description: Mapped[str] = mapped_column(Text())
    price: Mapped[float] = mapped_column(Float())
    length: Mapped[int] = mapped_column(Integer())
    product_limit: Mapped[int] = mapped_column(Integer())                                     

    subscriptions: Mapped["Subscription"] = relationship(back_populates='plan', cascade="all, delete")
    subscription_details: Mapped["SubscriptionDetail"] = relationship(back_populates='plan')

class PlanSchema(ma.Schema):
    class Meta:
        fields = ("id", "plan_name", "description", "price", "length", "product_limit")