# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import os
import shutil
import tempfile
import unittest

import tests.test_data as test_data

import dicom2nifti.compressed_dicom as compressed_dicom


class TestCompressedDicom(unittest.TestCase):

    def test_is_compressed(self):
        assert compressed_dicom._is_compressed(os.path.join(test_data.GENERIC_COMPRESSED, 'IM-0001-0001-0001.dcm')) is True
        assert compressed_dicom._is_compressed(os.path.join(test_data.GENERIC_ANATOMICAL, 'IM-0001-0001-0001.dcm')) is False

    def test_read_file(self):
        temporary_directory = tempfile.mkdtemp()
        try:
            dicom_file = os.path.join(temporary_directory, 'IM-0001-0001-0001.dcm')
            input_file = os.path.join(test_data.GENERIC_COMPRESSED, 'IM-0001-0001-0001.dcm')
            shutil.copy(input_file, dicom_file)
            dicom_headers = compressed_dicom.read_file(dicom_file)
            pixel_data = dicom_headers.pixel_array
            self.assertIsNotNone(pixel_data)

        finally:
            shutil.rmtree(temporary_directory)


if __name__ == '__main__':
    unittest.main()
