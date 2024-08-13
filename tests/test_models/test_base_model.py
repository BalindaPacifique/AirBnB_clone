#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ this class is going to test all our codes from the BaseModel class"""
    def test_init(self):
        """this module test all the instance from the init module"""
        my_model = BaseModel()
        
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
    def test_save(self):
        """this module tests the save module from the BaseModel"""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        new_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at, new_updated_at)
    def test_to_dict(self):
        """this module tests for the to_dict function"""
        my_model = BaseModel()

        my_dict = my_model.to_dict()

        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict["__class__"],  'BaseModel')
        self.assertEqual(my_dict['id'], my_model.id)
        self.assertEqual(my_dict["created_at"], my_model.creted_at.isoformat())
        self.assertEqual(my_dict["updated_at"], my_model.updated_at.isoformat())
    def test_str(self):
        """this module tests for the str format used in the BaseModel"""
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith("[Basemodel]"))
        self.assertIn(my_model.id, str(my_model))
        # self.assertIn(my_model.created_at, str(my_model))
        self.assertIn(my_model.to_dict, str(my_model))
if __name__ == "__main__":
    unittest.main()