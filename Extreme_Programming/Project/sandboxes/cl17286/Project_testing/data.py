import os
import csv


class Data:


    def check_password_strength(self):
        pass

    def suggest_password(self):
        pass

    def import_data(self):
        pass

    def list_all_password(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r") as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')

    def add_password(self):
        pass

    def search_password_regex(self):
        pass

