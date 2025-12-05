from pathlib import Path
from time import ctime
import shutil

# Raw string
# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()

# Return file name
# print(path.name)

# Return file name without extention
# print(path.stem)

# Return suffix attribute
# print(path.suffix)

# print(path.parent)

# path = path.with_name("file.txt")
# path = path.with_suffix(".txt")
# print(path)
# print(path.absolute())


path = Path("ecommerce_package_practice")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(py_files)
print(paths)

# Recursive search
paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(py_files)
print(paths)

# Working with files
# path = Path("ecommerce_package_practice/__init__.py")
source = Path("ecommerce_package_practice/__init__.py")
target = Path() / "Python Standard Library/__init__.py"

shutil.copy(source, target)
target.write_text(source.read_text())


# print(path.exists(), ctime(path.stat().st_ctime))

# with open("ecommerce_package_practice/__init__.py", "r") as file:
#     ...
# Reading from a file
# print(path.read_bytes())
# print(path.read_text())
