import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files

filename =  get_testdata_files("CT_small.dcm")[0]
dataset = pydicom.dcmread(filename)

print("filename: ", filename)
print("storage type: ", dataset.SOPClassUID)

pat_name = dataset.PatientName
print("patient name: ", pat_name.family_name + " " + pat_name.given_name)
print("patient id: ", dataset.PatientID)
print("modality: ", dataset.Modality)
print("study date: ", dataset.StudyDate);

if 'PixelData' in dataset:
    rows = int(dataset.Rows)
    cols = int(dataset.Columns)
    print("image size: {rows:d} x {cols:d} bytes".format(rows=rows, cols=cols, size=len(dataset.PixelData)))

    if 'PixelSpacing' in dataset:
        print("pixel spacing: ", dataset.PixelSpacing)

print("slice location: ", dataset.get('SliceLocation', "(missing)"))

plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
plt.show()
