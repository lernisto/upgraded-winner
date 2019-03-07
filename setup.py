import subprocess
from glob import glob
from os.path import splitext, basename

import setuptools


def get_version():
    try:
        git = subprocess.run(['git', 'describe', '--always'], capture_output=True)
        gitlabel = git.stdout.decode().strip()
        with open("VERSION","w") as fo:
            fo.write(gitlabel)
    except OSError:
        with open("VERSION","r") as fo:
            gitlabel = fo.read()

    return gitlabel



with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="upgraded-winner",
    version=get_version(),
    author="Terrel Shumway",
    author_email="ghdev@learnflask.dev",
    description="Accountability App for Tracking Progress Toward Goals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/learnflask/upgraded-winner",
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            "winner=winner:main"
        ]
    }
)
