#!/usr/bin/python3
""" Unittest for FileStorage class
"""

from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

from os import path, remove
import unittest


class Test_all(unittest.TestCase):
    """ Test for the all method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_all_empty(self):
        """ Test Empty Dictionary """
        self.assertEqual(storage.all(), {})

    def test_basemodel(self):
        """ Test with basemodel object """
        b = BaseModel()
        storage.new(b)
        storage.save()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)


class Test_new(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_no_arg(self):
        """ Test no passing argument """
        with self.assertRaises(TypeError):
            storage.new()

    # ... (other test methods)


class Test_save(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_save_base(self):
        """ Save method with base model """
        dic = {"id": "123"}
        b = BaseModel(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        # ... (assertions)

    # ... (other test methods)


class Test_reload(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_no_file(self):
        """ Test if no error happens when to file is present """
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.reload()
