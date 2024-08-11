import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f]

setuptools.setup(
    name="pythonfuzz",
    version="1.0.10",
    author="GitLab B.V.",
    maintainer="Marcell Perger",
    description="Coverage-guided fuzz testing for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing"
    ],
    python_requires='>=3.5.3',
    packages=setuptools.find_packages('.', exclude=("examples", "tests"))
)
