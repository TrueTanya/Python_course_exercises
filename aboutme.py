from pathlib import Path

print("Current file path", Path(__file__))
print("Absolute current file path", Path(__file__).absolute())

print("Related current file path", Path(__file__) / '..')
print("Conversion to full path", Path(Path(__file__) / '..').resolve())
print("Parent path", Path(__file__).parent)

# Папка data находящаяся в той же папке где и текущий файл
print("Директория в рядом с текущим файлом", Path(__file__) / '..' / 'data')

print(f"text about me: {__file__}")

# from pathlib import Path
# course = Path('/Users/xen/Dev/python-course')
# course
# PosixPath('/Users/xen/Dev/python-course')