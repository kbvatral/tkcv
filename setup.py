import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkcv",
    version="0.0.1",
    author="Caleb Vatral",
    author_email="caleb.m.vatral@vanderbilt.edu",
    description="Simple Tkinter GUI wrapper around OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbvatral/tkcv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'opencv-contrib-python',
        'imutils',
        'pillow'
    ],
    python_requires='>=3.5',
)
