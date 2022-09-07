__author__ ="penclai"

from unittest import TestCase
import os
from trunk.PasswordManager_main import PasswordManager_main

class TestPasswordManager(TestCase):

    def test_empty(self):
        self.assertEqual(PasswordManager_main.empty_checker("15"), False)
        self.assertEqual(PasswordManager_main.empty_checker(""), True)

    def test_create_account(self):
        pass
        # self.assertEqual(on)

    def test_check_username(self):
        self.assertEqual(PasswordManager_main.username_checker("Aiden"), True)

    def test_create_account_db(self):
        self.assertEqual(PasswordManager_main.create_account_db(100),True)
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/100_AccountPassword.csv"))

    def test_get_last_id_user(self):
        self.assertEqual(PasswordManager_main.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Dummy_data/UserAccount.csv")),"4")

    def test_get_last_id_account(self):
        self.assertEqual(PasswordManager_main.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Dummy_data/1_AccountPassword.csv")),"3")


    def test_append_password_to_csv(self):
        pass

    def test_append_account_to_csv(self):
        pass