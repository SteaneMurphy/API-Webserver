from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Boolean
from marshmallow import fields

class Ticket(db.Model):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    issue_description: Mapped[str] = mapped_column(Text())
    date_created: Mapped[date]
    status: Mapped[str] = mapped_column(String(100), server_default="in progress")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="tickets")

class TicketSchema(ma.Schema):
    user = fields.Nested("UserSchema")

    class Meta:
        fields = ("id", "issue_description", "date_created", "status", "user")