from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean

#USER ENTITY MODEL
class User(db.Model):
    __tablename__ = "users"

    #attributes
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(100))
    admin: Mapped[bool] = mapped_column(Boolean(), server_default="false")      #admin role 'false' by default
    date_created: Mapped[date]
    last_login: Mapped[date]                                                    #initialised at date.today() but will overwrite on each successive login

    #ORM Relationships
    subscriptions: Mapped["Subscription"] = relationship(back_populates='user', cascade="all, delete")
    tickets: Mapped["Ticket"] = relationship(back_populates='user', cascade="all, delete")

#Marshmallow Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password", "admin", "date_created", "last_login")