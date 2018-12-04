#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os, datetime, abc
from xml.etree import ElementTree as ET

class Base(object):
    #@staticmethod
    pass

class ParserBase(Base):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def Parse(cls, basic_data):
        raise NotImplementedError