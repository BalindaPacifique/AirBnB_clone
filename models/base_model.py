#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for model objects, providing common attributes and methods for managing identity, timestamps, and basic serialization."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Optional positional arguments (ignored).
            **kwargs: Optional keyword arguments to set instance attributes.
                    Special keys:
                        - 'created_at' (str/datetime): Timestamp of creation.
                        - 'updated_at' (str/datetime): Timestamp of last update.
                        - Other keys will set corresponding instance attributes.

        Raises:
            ValueError: If a non-datetime value is provided for 'created_at' or 'updated_at'.
        """
        for key, value in kwargs.items():
            if key == "__class__":
                continue

            if key in {"created_at", "updated_at"}:
                if not isinstance(value, (str, datetime)):
                    raise ValueError(
                        f"Invalid value for '{key}'. Expected a datetime string or object.")
                value = datetime.strptime(
                    value, "%Y-%m-%dT%H:%M:%S.%f") if isinstance(value, str) else value

            setattr(self, key, value)

        if "id" not in kwargs:
            self.id = str(uuid4())

        if "created_at" not in kwargs:
            self.created_at = datetime.now()

        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()

    def save(self):
        """
        Update the Public Instance Attr updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary representing the instance's attributes.
                  Includes class name, ID, and formatted timestamps.
        """
        cls_name = self.__class__.__name__
        obj_dict = {key: value.isoformat() if isinstance(value, datetime) else value
                    for key, value in self.__dict__.items()}
        obj_dict['__class__'] = cls_name
        return obj_dict

    def __str__(self):
        """Returns a human-readable string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
