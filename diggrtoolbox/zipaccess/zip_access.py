#!/usr/bin/env python3
"""
Zip Access is a small tool providing access to zipped
json files.
"""

import zipfile
import json

FILE_EXT = ".json"


class ZipAccess:
    """
    Baseclass for the ZipSingleAccess and ZipMultiAccess classes
    """

    def __init__(self, filename, file_ext=FILE_EXT):

        if zipfile.is_zipfile(filename):
            self.filename = filename
            self.z = zipfile.ZipFile(self.filename)
        else:
            raise zipfile.BadZipFile

        self.file_ext = file_ext

    def json(self, content_filename=None):
        """
        Opens the zipfile and returns the first zipped
        JSON file as python object
        """
        if not content_filename:
            content_filename = self.z.filelist[0].filename
        with self.z.open(content_filename) as content_file:
            content = content_file.read()
            return json.loads(content.decode("utf-8"))


class ZipSingleAccess(ZipAccess):
    """
    This class is meant to provide access to a single
    JSON-file in a zipfile.
    """

    def json(self):
        """
        Opens the zipfile and returns the zipped
        JSON file as python object
        """

        if len(self.z.filelist) > 1:
            raise ValueError("Not more than one file per zipfile allowed.")

        return super().json()


class ZipMultiAccess(ZipAccess):
    """
    This class is meant to provide access to a Zip file containing
    one base json file and a folder with other json files extending the first
    """

    def get(self, file_id):
        for filename in self.z.namelist():
            if "/" in filename:
                if file_id == filename.split("/")[1][:-len(self.file_ext)]:
                    return self.json(filename)
        else:
            raise ValueError("Item {} not found.".format(file_id))
