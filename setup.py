import setuptools

setuptools.setup(
    name="vietnamsub",                     # This is the name of the package
    version="0.0.6",                        # The initial release version
    author="ĐGK",                     # Full name of the author
    author_email='admin@hieudeeptry.ml',
    keywords=['vietnam', 'sub', 'python', 'python3'],
    url='https://github.com/khanh101106/Module',
    license="MIT",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package  y

)
