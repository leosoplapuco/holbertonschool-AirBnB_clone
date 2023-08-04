#!/usr/bin/python3

class BaseModel:
  """
  A base class for all models.

  Attributes:
    id (str): The unique identifier of the model.
    created_at (datetime): The date and time the model was created.
    updated_at (datetime): The date and time the model was last updated.
  """

  def __init__(self, id, created_at, updated_at):
    self.id = id
    self.created_at = created_at
    self.updated_at = updated_at

  def __str__(self):
    return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

  def save(self):
    self.updated_at = datetime.now()

  def to_dict(self):
    data = self.__dict__.copy()
    data["__class__"] = self.__class__.__name__
    data["created_at"] = data["created_at"].isoformat()
    data["updated_at"] = data["updated_at"].isoformat()
    return data
