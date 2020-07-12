import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sirtyman",
    version="0.0.1",
    author="Marcin Tyman",
    author_email="marcin.tyman@gmail.com",
    description="Training materials for decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sirtyman/decorators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
