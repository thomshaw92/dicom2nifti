# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import unittest
import tempfile
import shutil
import os

import dicom2nifti.convert_philips as convert_philips
import tests.test_data as test_data
from dicom2nifti.exceptions import ConversionError
from tests.test_tools import compare_nifti, compare_bval, compare_bvec, ground_thruth_filenames


class TestConversionPhilips(unittest.TestCase):
    def test_dti(self):
        tmp_output_dir = tempfile.mkdtemp()
        try:
            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_DTI,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_DTI)[0]) == True
            assert compare_bval(results['BVAL_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI)[2]) == True
            assert compare_bvec(results['BVEC_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI)[3]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_DTI_002,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_DTI_002)[0]) == True
            assert compare_bval(results['BVAL_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI_002)[2]) == True
            assert compare_bvec(results['BVEC_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI_002)[3]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_ENHANCED_DTI,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_ENHANCED_DTI)[0]) == True
            assert compare_bval(results['BVAL_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_ENHANCED_DTI)[2]) == True
            assert compare_bvec(results['BVEC_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_ENHANCED_DTI)[3]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_DTI_IMPLICIT,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_DTI_IMPLICIT)[0]) == True
            assert compare_bval(results['BVAL_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI_IMPLICIT)[2]) == True
            assert compare_bvec(results['BVEC_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI_IMPLICIT)[3]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_DTI_IMPLICIT_002,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_DTI_IMPLICIT_002)[0]) == True
            assert compare_bval(results['BVAL_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI_IMPLICIT_002)[2]) == True
            assert compare_bvec(results['BVEC_FILE'],
                                ground_thruth_filenames(test_data.PHILIPS_DTI_IMPLICIT_002)[3]) == True

            self.assertRaises(ConversionError,
                              convert_philips.dicom_to_nifti,
                              test_data.PHILIPS_ENHANCED_DTI_IMPLICIT,
                              os.path.join(tmp_output_dir, 'test.nii.gz'))
        finally:
            shutil.rmtree(tmp_output_dir)

    def test_fmri(self):
        tmp_output_dir = tempfile.mkdtemp()
        try:
            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_FMRI,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_FMRI)[0]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_FMRI_IMPLICIT,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_FMRI_IMPLICIT)[0]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_ENHANCED_FMRI,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_ENHANCED_FMRI)[0]) == True
            self.assertRaises(ConversionError,
                              convert_philips.dicom_to_nifti,
                              test_data.PHILIPS_ENHANCED_FMRI_IMPLICIT,
                              os.path.join(tmp_output_dir, 'test.nii.gz'))
        finally:
            shutil.rmtree(tmp_output_dir)

    def test_anatomical(self):
        tmp_output_dir = tempfile.mkdtemp()
        try:
            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_ANATOMICAL,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_ANATOMICAL)[0]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_ANATOMICAL_IMPLICIT,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_ANATOMICAL_IMPLICIT)[0]) == True

            results = convert_philips.dicom_to_nifti(test_data.PHILIPS_ENHANCED_ANATOMICAL,
                                           os.path.join(tmp_output_dir, 'test.nii.gz'))
            assert compare_nifti(results['NII_FILE'],
                                 ground_thruth_filenames(test_data.PHILIPS_ENHANCED_ANATOMICAL)[0]) == True

            self.assertRaises(ConversionError,
                              convert_philips.dicom_to_nifti,
                              test_data.PHILIPS_ENHANCED_ANATOMICAL_IMPLICIT,
                              os.path.join(tmp_output_dir, 'test.nii.gz'))
        finally:
            shutil.rmtree(tmp_output_dir)

    def test_is_philips(self):
        assert convert_philips.is_philips(test_data.PHILIPS_ANATOMICAL)
        assert not convert_philips.is_philips(test_data.SIEMENS_ANATOMICAL)
        assert not convert_philips.is_philips(test_data.GE_ANATOMICAL)
        assert not convert_philips.is_philips(test_data.GENERIC_ANATOMICAL)

    def test_is_multiframe_dicom(self):
        assert convert_philips.is_multiframe_dicom(test_data.PHILIPS_ENHANCED_DTI)
        assert not convert_philips.is_multiframe_dicom(test_data.PHILIPS_DTI)
        assert convert_philips.is_multiframe_dicom(test_data.PHILIPS_ENHANCED_ANATOMICAL)
        assert not convert_philips.is_multiframe_dicom(test_data.PHILIPS_ANATOMICAL)
        assert convert_philips.is_multiframe_dicom(test_data.PHILIPS_ENHANCED_FMRI)
        assert not convert_philips.is_multiframe_dicom(test_data.PHILIPS_FMRI)

    def test_is_multiframe_dti(self):
        assert convert_philips._is_multiframe_dti(test_data.PHILIPS_ENHANCED_DTI)
        assert not convert_philips._is_multiframe_dti(test_data.PHILIPS_DTI)
        assert not convert_philips._is_multiframe_dti(test_data.PHILIPS_ENHANCED_ANATOMICAL)
        assert not convert_philips._is_multiframe_dti(test_data.PHILIPS_ANATOMICAL)
        assert not convert_philips._is_multiframe_dti(test_data.PHILIPS_ENHANCED_FMRI)
        assert not convert_philips._is_multiframe_dti(test_data.PHILIPS_FMRI)

    def test_is_multiframe_fmri(self):
        assert not convert_philips._is_multiframe_fmri(test_data.PHILIPS_ENHANCED_DTI)
        assert not convert_philips._is_multiframe_fmri(test_data.PHILIPS_DTI)
        assert not convert_philips._is_multiframe_fmri(test_data.PHILIPS_ENHANCED_ANATOMICAL)
        assert not convert_philips._is_multiframe_fmri(test_data.PHILIPS_ANATOMICAL)
        assert convert_philips._is_multiframe_fmri(test_data.PHILIPS_ENHANCED_FMRI)
        assert not convert_philips._is_multiframe_fmri(test_data.PHILIPS_FMRI)

    def test_is_multiframe_anatomical(self):
        assert not convert_philips._is_multiframe_anatomical(test_data.PHILIPS_ENHANCED_DTI)
        assert not convert_philips._is_multiframe_anatomical(test_data.PHILIPS_DTI)
        assert convert_philips._is_multiframe_anatomical(test_data.PHILIPS_ENHANCED_ANATOMICAL)
        assert not convert_philips._is_multiframe_anatomical(test_data.PHILIPS_ANATOMICAL)
        assert not convert_philips._is_multiframe_anatomical(test_data.PHILIPS_ENHANCED_FMRI)
        assert not convert_philips._is_multiframe_anatomical(test_data.PHILIPS_FMRI)

    def test_is_singleframe_fmri(self):
        assert not convert_philips._is_singleframe_fmri(test_data.PHILIPS_ENHANCED_DTI)
        assert not convert_philips._is_singleframe_fmri(test_data.PHILIPS_DTI)
        assert not convert_philips._is_singleframe_fmri(test_data.PHILIPS_ENHANCED_ANATOMICAL)
        assert not convert_philips._is_singleframe_fmri(test_data.PHILIPS_ANATOMICAL)
        assert not convert_philips._is_singleframe_fmri(test_data.PHILIPS_ENHANCED_FMRI)
        assert convert_philips._is_singleframe_fmri(test_data.PHILIPS_FMRI)

    def test_is_singleframe_dti(self):
        assert not convert_philips._is_singleframe_dti(test_data.PHILIPS_ENHANCED_DTI)
        assert convert_philips._is_singleframe_dti(test_data.PHILIPS_DTI)
        assert not convert_philips._is_singleframe_dti(test_data.PHILIPS_ENHANCED_ANATOMICAL)
        assert not convert_philips._is_singleframe_dti(test_data.PHILIPS_ANATOMICAL)
        assert not convert_philips._is_singleframe_dti(test_data.PHILIPS_ENHANCED_FMRI)
        assert not convert_philips._is_singleframe_dti(test_data.PHILIPS_FMRI)


if __name__ == '__main__':
    unittest.main()