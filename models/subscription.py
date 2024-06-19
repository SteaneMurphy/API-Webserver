from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, ForeignKey

class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[date]
    end_date: Mapped[date]
    status: Mapped[bool] = mapped_column(Boolean(), server_default="false")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    #plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))

class SubscriptionSchema(ma.Schema):
    class Meta:
        fields = ("id", "start_date", "end_date", "status", "last", "last_login")