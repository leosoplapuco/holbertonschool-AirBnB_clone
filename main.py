#!/usr/bin/python3

import models.base_model
import models.engine.file_storage

model = models.base_model.BaseModel()
model.id = "1234567890"
model.name = "John Doe"
models.engine.file_storage.save(model)
model = models.engine.file_storage.load("1234567890")
print(model.id)
print(model.name)
