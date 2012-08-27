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

from PyQt4.QtCore import QSettings

class Stations():
    """Stations"""

    def __init__(self, parent):
        self.parent = parent
        self.qset = QSettings("bgradio", "bgradio")
        self.last = self.qset.value("last", None).toPyObject()
        self.map = self.qset.value("stations", {}).toPyObject()

        if not self.map:
            self.set_default()
            self.qset.setValue("stations", self.map)

    def set_default(self):
        self.map["Index radio"] = "http://live2.infonetmedia.si:8000/index"
        self.map["MFM Radio"] = "http://195.252.107.194:8012/listen.pls"
        self.map["Naxi Radio"] = "http://naxi64.streaming.rs:9160/listen.pls"
        self.map["Novosti Radio"] = "http://www.radionovosti.rs:443/radionovosti56s.mp3.m3u"
        self.map["Radio B92"] = "http://stream.b92.net:7999/radio-b92.ogg.m3u"
        self.map["Radio Beograd 1"] = "http://www.radiobeograd.rs/download/mp3s/radiobeograd1.asx"
        self.map["Radio Beograd 2"] = "http://www.radiobeograd.rs/download/mp3s/radiobeograd2.asx"
        self.map["Radio Pingvin"] = "http://radiopingvin.com/live.asx"
        self.map["Radio S"] = "http://sh1.beotel.net:8002/listen.pls"
        self.map["Roadstar Radio"] = "http://roadstar128.streaming.rs:9300"
        self.map["Studio B"] = "http://radio.studiob.rs:8004/listen.pls"
        self.map["TDI Radio"] = "http://streaming.tdiradio.com:9999/listen.pls"
        self.map["TopFM Radio"] = "http://109.206.96.11:8000/listen.pls"
