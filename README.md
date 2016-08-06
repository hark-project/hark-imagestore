# hark-imagestore

[![Build Status](https://travis-ci.org/hark-project/hark-imagestore.svg?branch=develop)](https://travis-ci.org/hark-project/hark-imagestore)

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

## Building

This project can be built as a Debian package to simplify deployment. The
debian configuration was built with the `make-deb` command from pypi.

You need some dependencies:

	sudo apt-get install python3-dev debhelper dh-virtualenv

Then just run:

	$ cd src && dpkg-buildpackage -uc -us -b

This will produce a `.deb` build artifact - a Debian package - at the root of
the repository. On Debian systems, you can install this with:

	# dpkg -i $filename

You can then run the system with:

	$ /usr/share/python/hark-imagestore/bin/hark_imagestore

### Updating the Debian Changelog

Before building the debian package as above, update the Debian changelog. The `git-dch` tool from `git-buildpackage` can do this:

	git-dch --debian-branch develop --auto

Per the man page:

> If the distribution of the topmost section in debian/changelog is UNRELEASED
> the changelog entries  will  be  inserted  into this section. Otherwise a new
> section will be created.

i.e. change `UNRELEASED` to `RELEASED` in the topmost distribution unless you
want the changelog added to it.

# License

GPLv3. See the LICENSE file for details.

# Python Support

Same as the main hark tool - see the [README#Python
Support](https://github.com/hark-project/hark#python-support).

# Running Tests

Again, same as the main hark tool - see its [README#Running
Tests](https://github.com/hark-project/hark#running-tests).

