# To ignore numpy errors:
#     pylint: disable=E1101
# icoMetrix DICOM-related utilities


import difflib
import sys

import dicom


def dicom_diff(file1, file2):
    """ Shows the fields that differ between two DICOM images.

    Inspired by https://code.google.com/p/pydicom/source/browse/source/dicom/examples/DicomDiff.py
    """

    datasets = dicom.read_file(file1), dicom.read_file(file2)

    rep = []

    for dataset in datasets:
        lines = (str(dataset.file_meta)+"\n"+str(dataset)).split('\n')
        lines = [line + '\n' for line in lines]  # add the newline to the end
        rep.append(lines)

    diff = difflib.Differ()
    for line in diff.compare(rep[0], rep[1]):
        if (line[0] == '+') or (line[0] == '-'):
            sys.stdout.write(line)

if __name__ == "__main__":
    print("--------------------- CTP - ORIG -----------------------")
    dicom_diff("/Users/abrys/Documents/data/DCM2NII/CTP/1.3.6.1.4.1.25403.260248567109012.6496.20160302100538.83.dcm",
               "/Users/abrys/Documents/data/DCM2NII/ZIP_orig/IM-0001-0001.dcm")
    print("--------------------- CTP - DECOMP -----------------------")
    dicom_diff("/Users/abrys/Documents/data/DCM2NII/CTP/1.3.6.1.4.1.25403.260248567109012.6496.20160302100538.83.dcm",
               "/Users/abrys/Documents/data/DCM2NII/ZIP/IM-0001-0001.dcm")