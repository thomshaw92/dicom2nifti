# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import unittest
import tempfile
import shutil
import os
import sys
import tests.test_data as test_data


class TestConversionDicom(unittest.TestCase):
    def test_main_function(self):
        tmp_output_dir = tempfile.mkdtemp()
        script_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'scripts','dicom2nifti')
        assert os.path.isfile(script_file)

        try:
            if sys.version_info > (3, 0):
                from importlib.machinery import SourceFileLoader
                dicom2nifti_module = SourceFileLoader("dicom2nifti_script", script_file).load_module()
            else:
                import imp
                dicom2nifti_module = imp.load_source('dicom2nifti_script', script_file)
            dicom2nifti_module.main([test_data.SIEMENS_ANATOMICAL, tmp_output_dir])

        finally:
            shutil.rmtree(tmp_output_dir)


if __name__ == '__main__':
    unittest.main()
