#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os, datetime, abc
from xml.etree import ElementTree as ET
from base import Base,ParserBase
        
class XmlElement(Base):
    def __init__(self, attrs):
        self.attrs = attrs
        self.key=""
        self.value=""
    def Check(self, field):
        for key,value in field.items():
            if self.attrs[key] <> value:
                return False
        return True
    
class XmlParser(ParserBase):
    def __init__(self, node):
        self.name="XmlParser"
        self.file=node.attrib["name"]
        self.tags={}
        self.data={}
        for child in node.getchildren():
            tag = child.attrib["tag"]
            attr = child.attrib["attrib"]
            self.tags[tag] = attr
    def GetElement(self, keys):
        for index, ele in self.data.items():
            if ele.Check(keys):
                return ele
        return None