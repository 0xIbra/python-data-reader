from xml.etree import cElementTree as ET
import os
import time


class XMLReader:

    def __init__(self, file_path, arguments={}):
        self.__file_path = file_path
        self.__arguments = arguments

        if 'tag_path' not in arguments:
            raise Exception('"tag_path" argument is required to parse XML.')

        self.__tag_path = arguments['tag_path']

    def iterate(self):
        """ Iterates over objects specified with "tag_path" argument and yields them one by one. """

        root = ET.parse(self.__file_path).getroot()

        generator = root.iterfind(self.__tag_path)
        for entry in generator:
            yield entry
