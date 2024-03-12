#!/usr/bin/python3
"""Initializes the package"""

from models.engine.file_storage import FileStorage

#create an instance of FileStorage
storage = FileStorage()

#Reload the storage instance to load any existing data
storage.reload()
