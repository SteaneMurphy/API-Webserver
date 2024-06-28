from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from marshmallow import fields
from typing import List
from security.auth import generate_license

#USER ENTITY MODEL
class SubscriptionDetail(db.Model):
    __tablename__ = "subscription_details"

    #attributes
    id: Mapped[int] = mapped_column(primary_key=True)
    license: Mapped[str] = mapped_column(String(100))                                   
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscriptions.id", ondelete="CASCADE"))
    
    #ORM Relationships 
    product: Mapped["Product"] = relationship(back_populates="subscription_details")   
    subscription: Mapped["Subscription"] = relationship(back_populates="subscription_details", cascade="all, delete") 

#Marshmallow Schema
class SubscriptionDetailSchema(ma.Schema):
    plan = fields.Nested("PlanSchema")
    product = fields.Nested("ProductSchema")
    subscription = fields.Nested("SubscriptionSchema")

    class Meta:
        fields = ("id", "license", "product", "subscription")