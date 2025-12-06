from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile

# working with zip files
zip = ZipFile("files.zip", "w")
with ZipFile("files.zip", "w") as zip:
    # point to the FOLDER, not to a file
    # raw string so \P and \_ don't break
    for path in Path(r"..\Python Standard Library").rglob("*.*"):
        if path.is_file():
            # store the file with the name you will look for later
            arcname = path.relative_to(Path(r"..\Python Standard Library"))
            zip.write(path, arcname)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")

# Path(r"C:\Program Files\Microsoft")
# Path("usr/local/bin")
# Path()
# Path() / "ecommerce_package_practice" / Path("ecommerce_package_practice")
# Path.home()
# path = Path("ecommerce_package_practice\ecommerce\__init__.py")
# print(path.exists(), path.is_file(), path.is_dir())

# # file name
# print(path.name)

# # file name without extention
# print(path.stem)

# # Only file extention
# print(path.suffix)

# # Path parent
# print(path.parent)

# Only representation of path without existed file
# path = path.with_name("file.txt")
# print(path.absolute())

# Change extention of file
# path = path.with_suffix(".txt")
# print(path)

# Working wit directories
# path = Path("ecommerce_package_practice\ecommerce")
# # path.exists()
# # path.mkdir()
# # path.rmdir()
# # path.rename("ecommerce2")
# # print(path.iterdir())

# paths = [p for p in path.iterdir() if p.is_dir()]
# # py_files = [p for p in path.glob("*.py")]
# py_files = [p for p in path.rglob("*.py")]
# print(paths)
# print(py_files)

# Working with files
# path = Path("ecommerce_package_practice\ecommerce\__init__.py")
# # path.exists()
# # path.rename("__init__.txt")
# # path.unlink()
# # print(path.stat())
# # print(ctime(path.stat().st_ctime))

# # print(path.read_bytes())
# # print(path.read_text())
# # print(path.write_text("..."))
# # print(path.write_bytes())

# # Copy file to current directory
# source = Path("..\ecommerce_package_practice\ecommerce\__init__.py")
# target = Path() / "__init__.py"

# shutil.copy(source, target)
# target.write_text(source.read_text())
