# ARW to TIFF

A short Python script that converts Sony .ARW files into .tiff format. Forked from horatioduke's [arwhatever](https://github.com/horatioduke/arwhatever).

## Dependencies

- [os-sys](https://pypi.org/project/os-sys/)
- [rawpy](https://pypi.org/project/rawpy/)
- [imageio](https://pypi.org/project/imageio/)
- [shutil](https://pypi.org/project/pytest-shutil/)

## How To Use

1. From within the main repo, run `virtualenv venv` to create a virtual environment.
2. From within the main repo, run `source venv/bin/activate` to activate it.
3. From within the main repo, run `pip3 install -r requirements.txt` to install dependencies
4. From within the main repo, run `python3 main.py` to create the I/O folders, if they don't already exist
5. Drop desired **.ARW** images for conversion in the **/input** folder.
6. From within the main repo, run `python3 main.py` again to convert files in the **/input** folder. You can find the converted files in the **/output** folder when the script completes.

