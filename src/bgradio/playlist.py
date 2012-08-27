# -*- coding: utf-8 -*-
# Author: Milan Nikolic <gen2brain@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import urllib2
from StringIO import StringIO
import xml.etree.ElementTree as ET

class Playlist():
    """Parse playlist"""

    def __init__(self, url, parent=None):
        self.url = str(url)
        self.parent = parent
        if self.url[-3:] in ["m3u", "pls", "asx"]:
            self.playlist = self.get_playlist()

    def parse(self):
        if self.url.endswith("m3u"):
            return self.parse_m3u()
        elif self.url.endswith("pls"):
            return self.parse_pls()
        elif self.url.endswith("asx"):
            return self.parse_asx()
        else:
            return [self.url]

    def get_playlist(self):
        try:
            request = urllib2.Request(self.url)
            fd = urllib2.urlopen(request)
            data = fd.read()
            fd.close()
            return data
        except urllib2.URLError, err:
            self.playlist = None
            sys.stderr.write("%s: %s\n" % (self.url, str(err)))

    def parse_m3u(self):
        items = []
        if self.playlist:
            for line in self.playlist.splitlines():
                line = line.strip()
                if not line.startswith("#") and line:
                    items.append(line)
        return items

    def parse_pls(self):
        items = []
        if self.playlist:
            for line in self.playlist.splitlines():
                line = line.strip()
                if line.startswith("File"):
                    split = line.split("=")
                    items.append(split[1])
        return items

    def parse_asx(self):
        def to_parseable(tree):
            t = ET.tostring(tree)
            t = t.lower()
            return ET.fromstring(t)

        items = []
        et = ET.ElementTree()
        xml = et.parse(StringIO(self.playlist))
        tree = to_parseable(xml)
        for entry in tree.findall("entry"):
            ref = entry.find("ref")
            items.append(ref.attrib["href"])
        return items
