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

from PyQt4.QtGui import QWidget, QIcon
from PyQt4.QtCore import pyqtSignal, QString

from bgradio.tray import Tray
from bgradio.radio import Radio
from bgradio.stations import Stations

class BGRadio(QWidget):
    """Belgrade Radio Stations"""

    state_changed = pyqtSignal(str)
    station_changed = pyqtSignal(tuple)

    def __init__(self, opts):
        QWidget.__init__(self)
        self.opts = opts
        self.radio = Radio(self)
        self.stations = Stations(self)
        self.tray = Tray(self)

        self.state_changed.connect(
                self.on_state_changed)
        self.station_changed.connect(
                self.on_station_changed)

        self.radio.start()
        if self.stations.last:
            self.station_changed.emit(self.stations.last)
            self.tray.menu.stations[QString(
                self.stations.last[0])].setChecked(True)

    def set_enabled(self, enabled=True):
        self.tray.menu.action_pause.setEnabled(enabled)
        self.tray.menu.action_stop.setEnabled(enabled)

    def set_paused(self, paused=True):
        if paused:
            text = "Play"
            icon = "media-playback-start.png"
        else:
            text = "Pause"
            icon = "media-playback-pause.png"
        self.tray.menu.action_pause.setText(text)
        self.tray.menu.action_pause.setIcon(
                QIcon(":icons/%s" % icon))

    def on_state_changed(self, state):
        if state == "stopped":
            self.set_enabled(False)
            self.tray.setIcon(QIcon(
                ":icons/network-wireless-connected-00.png"))
            for action in self.tray.menu.stations.values():
                action.setChecked(False)
        elif state == "loading":
            self.tray.setIcon(QIcon(
                ":icons/network-wireless-connected-50.png"))
        elif state == "playing":
            self.set_enabled(True)
            self.set_paused(False)
            self.tray.setIcon(QIcon(
                ":icons/network-wireless.png"))
            if self.radio.title and self.radio.genre:
                self.tray.setToolTip(self.radio.title)
                self.tray.show_message(self.radio.title, self.radio.genre)
        elif state == "paused":
            self.set_enabled(True)
            self.set_paused(True)
            if self.radio.title:
                self.tray.setToolTip("%s - paused" % self.radio.title)
            self.tray.setIcon(QIcon(
                ":icons/network-wireless-connected-25.png"))

    def on_station_changed(self, station):
        name, url = station
        self.radio.action_play.emit(station)
        self.stations.qset.setValue("last", station)
