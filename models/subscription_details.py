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

    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id", ondelete="CASCADE"))
    plan: Mapped["Plan"] = relationship(back_populates="subscription_detail", cascade="all, delete") 

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    product: Mapped["Product"] = relationship(back_populates="subscription_detail", cascade="all, delete")

    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscriptions.id", ondelete="CASCADE"))
    subscription: Mapped["Subscription"] = relationship(back_populates="subscription_detail", cascade="all, delete") 

class SubscriptionDetailSchema(ma.Schema):
    plan = fields.Nested("PlanSchema")
    product = fields.Nested("ProductSchema")
    subscription = fields.Nested("SubscriptionSchema")

    class Meta:
        fields = ("id", "license", "plan", "product", "subscription")