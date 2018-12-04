#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from xml_parser import XmlParser,XmlElement

class Siminfo(XmlElement):
    def __init__(self, attrs):
        super(Siminfo, self).__init__(attrs)
        self.key = attrs["operator_key"]
        self.value = attrs["operator_name"]
        self.sbp_id = ""
    def CheckMcc(self, mcc):
        plmn=self.attrs["mcc_mnc"]
        if plmn[:len(mcc)] == mcc:
            return True
        return False

#siminfo class
class ParserSiminfo(XmlParser):
    def __init__(self, node):
        super(ParserSiminfo, self).__init__(node)
        self.name="ParserSiminfo"
    def Parse(self, basic_data):
        #XmlParser.Parse(self, basic_data)
        root = ET.fromstring(open(self.file, 'r').read())
        for tag, attrs in self.tags.items():   
            #print tag,attrs,root
            nodes = root.findall(tag)
            #print NVs
            for sim_node in nodes:
                #print sim_node.tag,sim_node.text
                values={}
                for atr in attrs.split(","):
                    node = sim_node.find(".//*[@key='%s']" % atr)
                    values[atr] = node.text if node is not None else ""
                    #print atr,values[atr]
                sim = Siminfo(values)
                self.data[sim.key] = sim
        #print self.data
    def SetSbpId(sbp_id):
        pass