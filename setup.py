import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
       name='mod3',
       version='1.0.0',
       py_modules=['mod3'],
       author='ziejaCode',
       author_email='ziejaCode@gaga.con',
       long_description=long_description,
       url='https://github.com/czarny25/mod3.git',
       description="Test class for study"
     )