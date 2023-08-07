#!/usr/bin/python3
""" this is the file_storage"""

from json import dump
from json import load


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects [obj.get("__class__") + "." + obj.get("id")] = obj

    def save(self):
        with open (self.__file_path,"w+") as f:
            dump(self.__objects, f)

    def reload(self):
        with open (self.__file_path,"r") as f:
            self.__objects = load(f)
