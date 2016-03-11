# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import unittest
import tempfile
import shutil

import dicom2nifti.convert_directory as convert_directory
import tests.test_data as test_data


class TestConversionDicom(unittest.TestCase):
    def test_convert_directory(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            convert_directory.convert_directory(test_data.GENERIC_ANATOMICAL, tmp_output_dir)

        finally:
            shutil.rmtree(tmp_output_dir)



if __name__ == '__main__':
    unittest.main()
