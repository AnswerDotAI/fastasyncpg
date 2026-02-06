__all__ = ["Album", "Artist", "Cat", "Customer", "Dog", "Employee", "Genre", "Invoice", "Invoice_Line", "Media_Type", "Playlist", "Playlist_Track", "Toy", "Track"]
from dataclasses import dataclass
import datetime,decimal
from uuid import UUID
from fastcore.utils import UNSET
@dataclass
class Album:
    album_id: int | None = UNSET
    title: str | None = UNSET
    artist_id: int | None = UNSET

@dataclass
class Artist:
    artist_id: int | None = UNSET
    name: str | None = UNSET

@dataclass
class Cat:
    id: int | None = UNSET
    name: str | None = UNSET
    weight: float | None = UNSET
    uid: int | None = UNSET

@dataclass
class Customer:
    customer_id: int | None = UNSET
    first_name: str | None = UNSET
    last_name: str | None = UNSET
    company: str | None = UNSET
    address: str | None = UNSET
    city: str | None = UNSET
    state: str | None = UNSET
    country: str | None = UNSET
    postal_code: str | None = UNSET
    phone: str | None = UNSET
    fax: str | None = UNSET
    email: str | None = UNSET
    support_rep_id: int | None = UNSET

@dataclass
class Dog:
    id: int | None = UNSET
    name: str | None = UNSET
    age: int | None = UNSET

@dataclass
class Employee:
    employee_id: int | None = UNSET
    last_name: str | None = UNSET
    first_name: str | None = UNSET
    title: str | None = UNSET
    reports_to: int | None = UNSET
    birth_date: datetime.datetime | None = UNSET
    hire_date: datetime.datetime | None = UNSET
    address: str | None = UNSET
    city: str | None = UNSET
    state: str | None = UNSET
    country: str | None = UNSET
    postal_code: str | None = UNSET
    phone: str | None = UNSET
    fax: str | None = UNSET
    email: str | None = UNSET

@dataclass
class Genre:
    genre_id: int | None = UNSET
    name: str | None = UNSET

@dataclass
class Invoice:
    invoice_id: int | None = UNSET
    customer_id: int | None = UNSET
    invoice_date: datetime.datetime | None = UNSET
    billing_address: str | None = UNSET
    billing_city: str | None = UNSET
    billing_state: str | None = UNSET
    billing_country: str | None = UNSET
    billing_postal_code: str | None = UNSET
    total: decimal.Decimal | None = UNSET

@dataclass
class Invoice_Line:
    invoice_line_id: int | None = UNSET
    invoice_id: int | None = UNSET
    track_id: int | None = UNSET
    unit_price: decimal.Decimal | None = UNSET
    quantity: int | None = UNSET

@dataclass
class Media_Type:
    media_type_id: int | None = UNSET
    name: str | None = UNSET

@dataclass
class Playlist:
    playlist_id: int | None = UNSET
    name: str | None = UNSET

@dataclass
class Playlist_Track:
    playlist_id: int | None = UNSET
    track_id: int | None = UNSET

@dataclass
class Toy:
    id: int | None = UNSET
    name: str | None = UNSET
    dog_id: int | None = UNSET

@dataclass
class Track:
    track_id: int | None = UNSET
    name: str | None = UNSET
    album_id: int | None = UNSET
    media_type_id: int | None = UNSET
    genre_id: int | None = UNSET
    composer: str | None = UNSET
    milliseconds: int | None = UNSET
    bytes: int | None = UNSET
    unit_price: decimal.Decimal | None = UNSET

