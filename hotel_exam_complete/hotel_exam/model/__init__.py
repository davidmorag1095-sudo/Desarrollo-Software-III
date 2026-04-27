"""Data models for the hotel exam practice application.

This package defines simple domain objects for the hotel management
application: guests (huespedes), rooms (habitaciones) and reservations
(reservas). Each class encapsulates the attributes of a single entity
and performs basic validation in its constructor to prevent the creation
of objects with invalid state. No business rules involving multiple
objects live in these classes; instead they are delegated to the
service layer.
"""
