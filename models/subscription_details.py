from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from marshmallow import fields
from typing import List
from security.auth import generate_license

class SubscriptionDetail(db.Model):
    __tablename__ = "subscription_details"

    id: Mapped[int] = mapped_column(primary_key=True)
    license: Mapped[str] = mapped_column(String(100))                                   

    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
    plan: Mapped["Plan"] = relationship(back_populates="subscription_detail") 

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="subscription_detail")

    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscriptions.id"))
    subscription: Mapped["Subscription"] = relationship(back_populates="subscription_detail") 

class SubscriptionDetailSchema(ma.Schema):
    plan = fields.Nested("PlanSchema")
    product = fields.Nested("ProductSchema")
    subscription = fields.Nested("SubscriptionSchema")

    class Meta:
        fields = ("id", "license", "plan", "product", "subscription")