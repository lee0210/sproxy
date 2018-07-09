import setuptools

setuptools.setup(
    name="sproxy",
    version="0.0.1",
    author="Lee Li",
    author_email="chunwai.c.lee@gmail.com",
    description="A simple proxy",
    package_dir={'':'src'},
    packages=setuptools.find_packages('src'),
)
