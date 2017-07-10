from __future__ import print_function

import os

import logging

import dicom2nifti
import dicom2nifti.settings as settings
import dicom2nifti.image_reorientation as image_reorientation


def subdir_count(path):
    count = 0
    for f in os.listdir(path):
        child = os.path.join(path, f)
        if os.path.isdir(child):
            count += 1
    return count


def main():
    for root, dir_names, _ in os.walk(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                   'tests',
                                                   'data')):
        settings.disable_validate_multiframe_implicit()
        # New directory
        for dir_name in dir_names:
            dir_path = os.path.join(root, dir_name)
            if subdir_count(dir_path) > 0:
                continue  # not processing because not lowest level of directory
            logging.info(dir_path)
            output_file = dir_path + '_ground_truth.nii.gz'
            reoriented_file = dir_path + '_ground_truth_reoriented.nii.gz'
            # noinspection PyBroadException
            try:
                if not os.path.isfile(output_file):
                    dicom2nifti.dicom_series_to_nifti(dir_path, output_file, False)
                    image_reorientation.reorient_image(output_file, reoriented_file)
            except:  # explicitly capturing everything here
                pass


if __name__ == "__main__":
    main()
