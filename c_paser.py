#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os, datetime, abc
from xml.etree import ElementTree as ET
from base import Base,ParserBase

class CParserElement(ParserBase):
    def __init__(self, node):
        self.partten=node.attrib["partten"]
        self.start_tag=node.attrib["start_tag"] if "start_tag" in node.attrib else ""
        self.end_tag=node.attrib["end_tag"] if "end_tag" in node.attrib else ""
    def Parse(self, basic_data, fd, data):
        pass
    def StripComment(self, line, multi_lined=False):
        return line, multi_lined
    def GetCodeBlock(self, lines, partten, start_tag, end_tag):
        ret=[]
        return ret

class CFunction(CParserElement):
    def __init__(self, node):
        CParserElement.__init__(self, node)
        self.blocks={}
        for child in node.getchildren():
            block=CBlock(child)
            self.blocks[hash(block)]=block
    def Parse(self, basic_data, fd, data):
        func_lines=self.GetCodeBlock(fd.readlines(), self.partten, self.start_tag, self.end_tag)
        print func_lines
        while len(func_lines)>0:
            for hash, block in self.blocks.items():
                block.Parse()

class CBlock(CParserElement):
    def __init__(self, node):
        CParserElement.__init__(self, node)
        self.mcc_indicator=None
        self.macro_indicator=None
        self.feature_parser={}
        child = node.find(".//mcc_indicator")
        if child is not None:
            self.mcc_indicator=CParserElement(child)
        child = node.find(".//macro_indicator")
        if child is not None:
            self.macro_indicator=CMacro(child)
        features=node.findall(".//feature")
        sn=0
        for f_node in features:
            f = CFeatureParser(f_node)
            self.feature_parser[sn] = f
            sn+=1
    def Parse(self, basic_data, lines, data):
        pass

def CMacro(CParserElement):
    def __init__(self, node):
        CParserElement.__init__(self, node)
        self.macros={}
        for child in node.getchildren():
            m=child.attrib["name"]
            v=child.attrib["value"]
            self.macros[m]=v
    def Parse(self, basic_data, lines, data):
        pass
    
class CFeatureParser(CParserElement):
    def __init__(self, node):
        CParserElement.__init__(self, node)
    def Parse(self, basic_data, lines, data):
        pass

class CParser(ParserBase):
    def __init__(self, node):
        self.name="CParser"
        self.file=node.attrib["name"]
        self.type=node.attrib["out_type"]
        self.output=node.attrib["out_dir"] if "out_dir" in node.attrib else ""
        self.functions={}
        self.data={}
        for child in node.getchildren():
            f = CFunction(child)
            self.functions[hash(f)] = f
        print self.functions
    def Parse(self, basic_data):
        fd = open(self.file,"r")
        for index, f in self.functions.items():
            f.Parse(basic_data, fd, self.data)
    #@classmethod
    #def GetFunction(cls, file, dest):
    #    pass
    #@classmethod
    #def GetBlock(cls, function, out_blocks):
    #    pass
    #@classmethod
    #def GetFeature(cls, line, features):
    #    pass
    @classmethod
    def SaveToFile(cls):
        pass