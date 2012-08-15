#!/usr/bin/env python

import os
import sys
from distutils.core import setup

sys.path.append(os.path.realpath("src"))

setup(name = "BGRadio",
        version = "0.1.0",
        description = "",
        long_description = "",
        author = "Milan Nikolic",
        author_email = "gen2brain@gmail.com",
        license = "GNU GPLv3",
        url = "https://github.com/gen2brain/bgradio",
        packages = ["bgradio"],
        package_dir = {"": "src"},
        scripts = ["bgradio"],
        requires = ["PyQt4"],
        platforms = ["Linux", "Windows"],
        data_files = [
            ("share/applications", ["data/bgradio.desktop"])
            ]
        )
