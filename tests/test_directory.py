# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import unittest
import tempfile
import shutil

import dicom2nifti.convert_dir as convert_directory
import tests.test_data as test_data


class TestConversionDicom(unittest.TestCase):
    def test_convert_directory(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            convert_directory.convert_directory(test_data.GENERIC_ANATOMICAL, tmp_output_dir)

        finally:
            shutil.rmtree(tmp_output_dir)

    def test_remove_accents(self):

        assert convert_directory._remove_accents_(u'êén_ölîfānt@') == 'een_olifant'
        assert convert_directory._remove_accents_(')(*&^%$#@!][{}\\"|,./?><') == ')(.'





if __name__ == '__main__':
    unittest.main()
