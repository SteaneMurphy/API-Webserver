from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey
from marshmallow import fields


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[date]
    end_date: Mapped[date]                                                          #how to determine end date?
    status: Mapped[bool] = mapped_column(Boolean(), server_default="false")         #active (true) or disabled (false)       

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="subscriptions", cascade="all, delete")

    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
    plan: Mapped["Plan"] = relationship(back_populates="subscriptions")

    payment: Mapped["Payment"] = relationship(back_populates="subscription", cascade="all, delete")
    subscription_detail: Mapped["SubscriptionDetail"] = relationship(back_populates="subscription", cascade="all, delete")

class SubscriptionSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id"])
    plan = fields.Nested("PlanSchema")

    class Meta:
        fields = ("id", "start_date", "end_date", "status", "user", "plan")