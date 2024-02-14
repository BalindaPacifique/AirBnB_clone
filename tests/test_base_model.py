#!/usr/bin/python3
""" Unittest for BaseModel class
"""

import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from os import path, remove


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """ Set up any resources needed for the tests """
        # Add any setup code you need for your tests here
        pass

    def tearDown(self):
        """ Clean up any resources created during the tests """
        # Add any cleanup code you need for your tests here
        try:
            remove("file.json")
        except Exception:
            pass

    def test_init(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save(self):
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_to_dict(self):
        with patch('models.base_model.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2022, 1, 1, 12, 0, 0)
            instance = BaseModel()
            instance_dict = instance.to_dict()
            expected_dict = {
                'id': instance.id,
                'created_at': '2022-01-01T12:00:00',
                'updated_at': '2022-01-01T12:00:00',
                '__class__': 'BaseModel'
            }
            self.assertEqual(instance_dict, expected_dict)

    def test_str(self):
        instance = BaseModel()
        str_representation = str(instance)
        expected_str = "[BaseModel] ({}) {}".format(
            instance.id, instance.__dict__)
        self.assertEqual(str_representation, expected_str)
