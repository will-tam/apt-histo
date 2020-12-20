import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# The text of the VERSION file
VERSION = (HERE / "VERSION.md").read_text()

LICENSE = (HERE / "LICENSE.md").read_text()

setuptools.setup(
    keywords = ['apt','history'],
    name="apt-histo",
    version=VERSION,
#    version_files="VERSION.md",
    author="will",
    author_email="will_tam@club-internet.fr",
    description="Read /var/log/apt/history.log.* and display it usefully",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/will_tam-bash/apt-histo.git",
    packages=setuptools.find_packages(),
    license="GPLv3",
#    license_files="LICENSE.md",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: System :: Archiving :: Packaging",
    ],
    include_package_data=True,
)
