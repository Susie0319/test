#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from c_paser import CParser

class ParseWoFeature(CParser):
    def __init__(self, node):
        super(ParseWoFeature, self).__init__(node)
        self.name="ParseWoFeature"