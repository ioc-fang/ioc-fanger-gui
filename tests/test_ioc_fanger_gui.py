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

    def test_fang(self):
        rv = self.app.post('/process', data={
            'text': 'example[.]com',
            'action': 'fang'
        })
        assert rv.data.decode() == 'example.com'

    def test_defang(self):
        rv = self.app.post('/process', data={
            'text': 'http://example.com/',
            'action': 'defang'
        })
        assert rv.data.decode() == 'hXXp://example[.]com/'
