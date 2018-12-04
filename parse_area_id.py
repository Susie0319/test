#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from c_paser import CParser

#sbp_id class
class ParseAreaId(CParser):
    def __init__(self, node):
        super(ParseAreaId, self).__init__(node)
        self.name="ParseAreaId"
