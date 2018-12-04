#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree
from parse_sbp_id import ParseSbpId
from  parse_area_id import ParseAreaId
from  parse_feature_index import ParserFeatureIndex
from  parse_siminfo import ParserSiminfo
from  parse_imc import ParseImcFeature
from  parse_sbp import ParseSbpFeature
from  parse_area import ParseAreaFeature
from  parse_wo import ParseWoFeature

config_file="./.config.xml"

def GetParser(xml_node):
    # print xml_node
    obj = None
    if xml_node is None or "parser" not in xml_node.attrib:
        return obj
    parser = xml_node.attrib["parser"]
    #eval_code=compile(str, "", "eval")
    #eval(eval_code)
    cls = globals()[parser]   #getattr(module, 'classname')
    obj = cls(xml_node)
    #obj = eval("obj=%s(xml_node)" % parser, {"xml_node": xml_node})
    # print obj
    return obj

if __name__ == '__main__':
    root = ElementTree.fromstring(open(config_file, 'r').read())
    basic_data={}
    basic_datas = root.find("basic_data")
    print basic_datas
    for node in basic_datas:
        parser = GetParser(node)
        parser.Parse(basic_data)
        basic_data[parser.name] = parser
    
    #parse feature from source code
    files = root.find("feature_files")
    for node in files:
    	parser = GetParser(node)
        parser.Parse(basic_data)
        parser.SaveToFile()

    #extra rule handling
    rules = root.find("extra_rules")
    for node in rules:
    	#parser = GetParser(node)
        #parser.Parse(basic_data_parses, node)
        #parser.SaveToFile()
        pass
    print "finish"


