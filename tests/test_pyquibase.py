# Copyright 2017 Eun Woo Song

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest
import sqlite3

from pyquibase.pyquibase import Pyquibase

class TestPyquibase(unittest.TestCase):

    def tearDown(self):
        """
        Delete the database
        """
        os.remove("testdb.sqlite")

    def test_liquibase_update_xml(self):
        self.pyquibase = Pyquibase.sqlite(
            'testdb.sqlite',
            os.path.join(os.path.dirname(__file__), 'db-changelog-1.xml')
        )

        # run liquibase update
        self.pyquibase.update()

        # verify that liquibase has been executed properly by
        # executing sql queries
        con = sqlite3.connect('testdb.sqlite')
        con.execute("INSERT INTO test VALUES (1, 'test')")
        actual = con.execute('SELECT * FROM test').fetchall()
        expected = [(1, 'test')]

        self.assertListEqual(actual, expected)

    def test_liquibase_update_yml(self):
        self.pyquibase = Pyquibase.sqlite(
            'testdb.sqlite',
            os.path.join(os.path.dirname(__file__), 'db-changelog-1.yaml')
        )
        # run liquibase update
        self.pyquibase.update()

        # verify that liquibase has been executed properly by
        # executing sql queries
        con = sqlite3.connect('testdb.sqlite')
        con.execute("INSERT INTO test VALUES (1, 'test')")
        actual = con.execute('SELECT * FROM test').fetchall()
        expected = [(1, 'test')]

        self.assertListEqual(actual, expected)
