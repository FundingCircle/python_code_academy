#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutClasses(Koan):
    class Dog:
        "Dogs need regular walkies. Never, ever let them drive."

    def test_instances_of_classes_can_be_created_adding_parentheses(self):
        # NOTE: The .__name__ attribute will convert the class
        # into a string value.
        fido = self.Dog()
        self.assertEqual(__, fido.__class__.__name__)

    class Dog2:
        def __init__(self):
            self._name = 'Paul'

        def set_name(self, a_name):
            self._name = a_name

    def test_init_method_is_the_constructor(self):
        dog = self.Dog2()
        self.assertEqual(__, dog._name)

    def test_private_attributes_are_not_really_private(self):
        dog = self.Dog2()
        dog.set_name("Fido")
        self.assertEqual(__, dog._name)
        # The _ prefix in _name implies private ownership, but nothing is truly
        # private in Python.

    class Dog3:
        def __init__(self):
            self._name = None

        def set_name(self, a_name):
            self._name = a_name

        def get_name(self):
            return self._name

        name = property(get_name, set_name)

    def test_that_name_can_be_read_as_a_property(self):
        fido = self.Dog3()
        fido.set_name("Fido")

        # access as method
        self.assertEqual(__, fido.get_name())

        # access as property
        self.assertEqual(__, fido.name)

    # ------------------------------------------------------------------

    class Dog4:
        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, a_name):
            self._name = a_name

    def test_creating_properties_with_decorators_is_slightly_easier(self):
        fido = self.Dog4()

        fido.name = "Fido"
        self.assertEqual(__, fido.name)

    # ------------------------------------------------------------------

    class Dog5:
        def __init__(self, initial_name):
            self._name = initial_name

        @property
        def name(self):
            return self._name

    def test_init_provides_initial_values_for_instance_variables(self):
        fido = self.Dog5("Fido")
        self.assertEqual(__, fido.name)

    def test_different_objects_have_different_instance_variables(self):
        fido = self.Dog5("Fido")
        rover = self.Dog5("Rover")

        self.assertEqual(__, rover.name == fido.name)

    # ------------------------------------------------------------------
