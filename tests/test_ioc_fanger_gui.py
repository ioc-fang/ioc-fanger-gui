#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from ioc_fanger_gui import ioc_fanger_gui


class IocFangerGuiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = ioc_fanger_gui.app.test_client()

    def test_get_index(self):
        rv = self.app.get('/')
        self.assertIn('IOC Fanger GUI', rv.data.decode())
        self.assertIn('GUI for fanging and defanging indicators of compromise.', rv.data.decode())
        self.assertIn('Welcome!', rv.data.decode())
        self.assertIn('This is the start of something great.', rv.data.decode())
