#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(__, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(__, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual(__, string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual(__, string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(__, (a == b))

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual(__, string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual(__, string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual(__, hi)
        self.assertEqual(__, there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual(__, hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual(__, original)
