import setuptools, sys, os

sys.path.insert(0, os.path.abspath('src/'))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtubedownloader",
    version="0.0.1",
    author="Norbert L J",
    author_email="horazon88@gmail.com",
    description="Learning project to download packages from youtube",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/norbertlj/python-projects/youtubedownloader",
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.5',
)