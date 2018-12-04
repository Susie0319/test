#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from c_paser import CParser

class ParseSbpFeature(CParser):
    def __init__(self, node):
        super(ParseSbpFeature, self).__init__(node)
        self.name="ParseSbpFeature"
