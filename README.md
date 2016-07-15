# hark-imagestore

Image service for the [hark project](https://hark-project.net).

The design and useability of hark depends upon it being able to easily find and
download prebuilt VM images. This is a small web service which the `hark` tool
can query to get a list of available images, metadata for the images and download URLs for them.

# Installation

Unlike the hark tool itself, hark-imagestore will not be packaged conveniently
for end-users as it's rare that people will need to run it themselves.

To install from pypi, just run:

	pip install hark-imagestore

## From Source

After checking out the repo:

	cd src && pip install .

# License

GPLv3. See the LICENSE file for details.

# Python Support

Same as the main hark tool - see the [README#Python Support](https://github.com/hark-project/hark#python-support).

# Running Tests

Again, same as the main hark tool - see its [README#Running Tests](https://github.com/hark-project/hark#running-tests).
