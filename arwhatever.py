import os
import rawpy
import imageio
import shutil

print("""
This process may take some time depending on the size of your raw images and how many you need to convert.
Better this than sending everything to that one hour photo and ending up brutally murdered by some Robin Williams type psycho.
""")

jpg_extension = ".jpg"
arw_extension = ".ARW"

arw_dump_path = "./ARW_dump"
jpg_dump_path = "./jpg_dump"

if os.path.isdir(arw_dump_path) is False:
    os.mkdir(arw_dump_path)

if os.path.isdir(jpg_dump_path) is False:
    os.mkdir(jpg_dump_path)

for file in os.listdir():
    
    if file.endswith(arw_extension):
        with rawpy.imread(file) as raw:
            rgb = raw.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=8)
            ### above line originally "rgb = raw.postprocess()"
        imageio.imsave(file.replace(arw_extension, jpg_extension), rgb)
        shutil.move(file, arw_dump_path)

for file in os.listdir():
    if file.endswith(jpg_extension):
        shutil.move(file, jpg_dump_path)