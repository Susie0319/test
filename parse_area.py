#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from c_paser import CParser

class ParseAreaFeature(CParser):
    def __init__(self, node):
        super(ParseAreaFeature, self).__init__(node)
        self.name="ParseAreaId"
    def Parse(self, basic_data):
        fd = open(self.file,"r")
        for index, f in self.functions.items():
            f.Parse(basic_data, fd, self.data)
        pass