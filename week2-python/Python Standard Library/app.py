from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
import csv
import json
import sqlite3

# working with JSON files
# movies = [
#     {"id": 1, "title": "Avatar", "year": 2012},
#     {"id": 2, "title": "Fast and Furious", "year": 2002}
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"], movies[0]["year"])

# working with CSV files, create
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "prduct_id", "price"])
#     writer.writerow([1000, 123546612, 1250])
#     writer.writerow([2000, 12612, 120])
# # working with CSV files, read
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)


# working with zip files
# zip = ZipFile("files.zip", "w")
# with ZipFile("files.zip", "w") as zip:
#     # point to the FOLDER, not to a file
#     # raw string so \P and \_ don't break
#     # for path in Path(r"..\Python Standard Library").rglob("*.*"):
#     for path in Path(r"..\ecommerce_package_practice\ecommerce").rglob("*.*"):
#         if path.is_file():
#             # store the file with the name you will look for later
#             # arcname = path.relative_to(Path(r"..\Python Standard Library"))
#             arcname = path.relative_to(
#                 Path(r"..\ecommerce_package_practice\ecommerce"))
#             zip.write(path, arcname)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")

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
