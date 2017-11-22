# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import os
import shutil
import tempfile
import unittest

import dicom2nifti.convert_dir as convert_directory

@unittest.skip('only in dti fixes branch')
class TestDTIDirectory(unittest.TestCase):
    """
    1yhA225_MR1		2jBp892_MR1		5Yeb682_MR1
    2AEu984_MR3		2quc733_MR1		fluox_uza_56_tp1bis
    2GWP485_MR1		3Dsy246_MR1		fluox_zgv_141_tp1
    2arJ393_MR1		4wPM484
    """

    # def test_convert_dti_01(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/1yhA225_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/1yhA225_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/1yhA225_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_02(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/2AEu984_MR3', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/2AEu984_MR3',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/2AEu984_MR3')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_03(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/2GWP485_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/2GWP485_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/2GWP485_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_04(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/2arJ393_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/2arJ393_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/2arJ393_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_05(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/2jBp892_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/2jBp892_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/2jBp892_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_06(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/2quc733_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/2quc733_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/2quc733_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_07(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/3Dsy246_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/3Dsy246_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/3Dsy246_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_08(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/4wPM484', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/4wPM484',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/4wPM484')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_09(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/5Yeb682_MR1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/5Yeb682_MR1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/5Yeb682_MR1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_10(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/fluox_uza_56_tp1bis', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/fluox_uza_56_tp1bis',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/fluox_uza_56_tp1bis')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)
    #
    # def test_convert_dti_11(self):
    #
    #     tmp_output_dir = tempfile.mkdtemp()
    #     os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/fluox_zgv_141_tp1', exist_ok=True)
    #     try:
    #         convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/fluox_zgv_141_tp1',
    #                                             '/Users/abrys/Documents/data/dcm2nii_dti/results/fluox_zgv_141_tp1')
    #
    #     finally:
    #         shutil.rmtree(tmp_output_dir)

    def test_convert_dti_12(self):

        tmp_output_dir = tempfile.mkdtemp()
        os.makedirs('/Users/abrys/Documents/data/dcm2nii_dti/results/JB_b700', exist_ok=True)
        try:
            convert_directory.convert_directory('/Users/abrys/Documents/data/dcm2nii_dti/JB_b700',
                                                '/Users/abrys/Documents/data/dcm2nii_dti/results/JB_b700')

        finally:
            shutil.rmtree(tmp_output_dir)


if __name__ == '__main__':
    unittest.main()
