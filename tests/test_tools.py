import os
import logging
import tempfile

import nibabel
import numpy
import shutil

import dicom2nifti.image_reorientation as image_reorientation

def ground_thruth_filenames(input_dir):
    nifti_file = input_dir + '_ground_truth.nii.gz'
    reoriented_nifti_file = input_dir + '_ground_truth_reoriented.nii.gz'
    bval_file = input_dir + '_ground_truth.bval'
    bvec_file = input_dir + '_ground_truth.bvec'
    return nifti_file, reoriented_nifti_file, bval_file, bvec_file


def compare_nifti(nifti_file_1, nifti_file_2):
    result = True
    logging.info("%s %s" % (nifti_file_1, nifti_file_2))
    work_dir = tempfile.mkdtemp()
    try:
        tmp_nifti_file_1 = os.path.join(work_dir, os.path.basename(nifti_file_1))
        tmp_nifti_file_2 = os.path.join(work_dir, os.path.basename(nifti_file_2))
        image_reorientation.reorient_image(nifti_file_1, tmp_nifti_file_1)
        image_reorientation.reorient_image(nifti_file_2, tmp_nifti_file_2)
        nifti_1 = nibabel.load(tmp_nifti_file_1)
        nifti_2 = nibabel.load(tmp_nifti_file_2)

        # check the affine
        if not numpy.allclose(nifti_1.affine, nifti_2.affine):
            logging.warning('affine mismatch')
            result = False

        # check the data
        if nifti_1.get_data_dtype() != nifti_2.get_data_dtype():
            logging.warning('dtype mismatch')
            result = False
        if not (nifti_1.get_data() == nifti_2.get_data()).all():
            logging.warning('data mismatch')
            logging.warning('perc 10:\n%s\n%s',
                            numpy.percentile(nifti_1.get_data(), 10),
                            numpy.percentile(nifti_2.get_data(), 10))
            logging.warning('perc 25:\n%s\n%s',
                            numpy.percentile(nifti_1.get_data(), 25),
                            numpy.percentile(nifti_2.get_data(), 25))
            logging.warning('perc 50:\n%s\n%s',
                            numpy.percentile(nifti_1.get_data(), 50),
                            numpy.percentile(nifti_2.get_data(), 50))
            logging.warning('perc 75:\n%s\n%s',
                            numpy.percentile(nifti_1.get_data(), 75),
                            numpy.percentile(nifti_2.get_data(), 75))
            logging.warning('perc 90:\n%s\n%s',
                            numpy.percentile(nifti_1.get_data(), 90),
                            numpy.percentile(nifti_2.get_data(), 90))
            result = False

    except:
        shutil.rmtree(work_dir)

    return result


def compare_bval(bval_file_1, bval_file_2):
    bval_1 = numpy.loadtxt(bval_file_1)
    bval_2 = numpy.loadtxt(bval_file_2)
    equal = numpy.array_equal(bval_1, bval_2)
    if not equal:
        logging.warning('bvals not equal\n%s\n', numpy.array2string(bval_1), numpy.array2string(bval_2))
    return equal


def compare_bvec(bvec_file_1, bvec_file_2):
    bvec_1 = numpy.loadtxt(bvec_file_1)
    bvec_2 = numpy.loadtxt(bvec_file_2)
    equal = numpy.array_equal(bvec_1, bvec_2)
    if not equal:
        logging.warning('bvecs not equal\n%s\n', numpy.array2string(bvec_1), numpy.array2string(bvec_2))
    return equal
