import os
import rawpy
import imageio
import shutil

tiff_extension = ".tiff"
arw_extension = ".ARW"

input_path = "input"
output_path = "output"

input_created_this_run = False
output_created_this_run = False

print('\n')

if os.path.isdir('./' + input_path) is False:
  print("Creating Input Folder at /input...")
  os.mkdir('./' + input_path)
  input_created_this_run = True

if os.path.isdir('./' + output_path) is False:
  print("Creating Output Folder at /output...")
  os.mkdir('./' + output_path)
  output_created_this_run = True

if os.path.isdir('./' + output_path) and os.path.isdir('./' + input_path):
  input_output_created = True

if input_output_created:
  if input_created_this_run or output_created_this_run:
    print("Created folders for file I/O.\n \
      Please Run again for processing and conversion \n")

  else:
    print('\n')
    print("Checking input folder for conversion...")
    print('\n')

    if input_output_created:
      for file in os.listdir(input_path):
        filepath = input_path + '/' + file
        if file.endswith(arw_extension):
          with rawpy.imread(filepath) as raw:
            print('Processing:', file)
            rgb = raw.postprocess(
              use_camera_wb=True,
            )
          imageio.imsave(filepath.replace(arw_extension, tiff_extension), rgb)
          shutil.move(filepath.replace(arw_extension, tiff_extension), output_path)
      
    print("\n")
    print("Done!")
    print("\n")