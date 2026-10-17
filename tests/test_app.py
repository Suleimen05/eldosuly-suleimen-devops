import os
import unittest
from unittest.mock import patch

from app.main import student_details, student_page


class StudentAppTests(unittest.TestCase):
    def test_default_student_details(self):
        with patch.dict(os.environ, {}, clear=True):
            student = student_details()

        self.assertEqual(student["name"], "Сүлеймен")
        self.assertEqual(student["surname"], "Елдосұлы")
        self.assertEqual(student["group"], "IT2-2310")
        self.assertEqual(student["id"], "38320")

    def test_environment_values_are_used(self):
        values = {
            "STUDENT_NAME": "Demo",
            "STUDENT_SURNAME": "Student",
            "STUDENT_GROUP": "TEST-1",
            "STUDENT_ID": "42",
        }
        with patch.dict(os.environ, values):
            student = student_details()

        self.assertEqual(student["name"], "Demo")
        self.assertEqual(student["id"], "42")
        self.assertIn("TEST-1", student_page(student))

    def test_page_escapes_environment_text(self):
        student = student_details()
        student["name"] = "<script>alert(1)</script>"

        page = student_page(student)

        self.assertNotIn("<script>", page)
        self.assertIn("&lt;script&gt;", page)


if __name__ == "__main__":
    unittest.main()
