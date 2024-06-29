from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey
from marshmallow import fields
from typing import List

#USER ENTITY MODEL
class Subscription(db.Model):
    __tablename__ = "subscriptions"

    #attributes
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[date] = date.today()
    end_date: Mapped[date] = date.today()                                                   #set by plan length
    status: Mapped[bool] = mapped_column(Boolean(), server_default="false")                 #subscription is active (true) or disabled (false)       
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE")) 
    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
    
    #ORM Relationships
    user: Mapped["User"] = relationship(back_populates="subscriptions")
    plan: Mapped["Plan"] = relationship(back_populates="subscriptions")
    payment: Mapped["Payment"] = relationship(back_populates="subscription", cascade="all, delete")
    subscription_details: Mapped[List["SubscriptionDetail"]] = relationship(back_populates="subscription", cascade="all, delete")

#Marshmallow Schema
class SubscriptionSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id"])
    plan = fields.Nested("PlanSchema")

    class Meta:
        fields = ("id", "start_date", "end_date", "status", "user", "plan", "plan_id", "products")