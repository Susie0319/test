#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from xml_parser import XmlParser,XmlElement

class FeatureNv(XmlElement):
    def __init__(self, attrs):
        super(FeatureNv, self).__init__(attrs)
        self.key = int(attrs["FEATUREINDEX"])
        #self.value = attrs["FIELD"]
    
#feature_index class 
class ParserFeatureIndex(XmlParser):
    def __init__(self, node):
        super(ParserFeatureIndex, self).__init__(node)
        self.name="ParserFeatureIndex"
    def Parse(self, basic_data):
        root = ET.fromstring(open(self.file, 'r').read())
        for tag, attrs in self.tags.items():
            #print tag,attrs,root
            NVs = root.findall(tag)
            #print NVs
            for nv_node in NVs:
                #print nv_node
                values = {}
                for atr in attrs.split(","):
                    values[atr] = nv_node.attrib[atr]
                nv = FeatureNv(values)
                self.data[nv.key] = nv
        #print self.data