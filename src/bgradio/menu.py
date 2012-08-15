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

from PyQt4.QtGui import QApplication, QMenu, QAction, QActionGroup, QIcon

class Menu(QMenu):
    """Context menu"""

    def __init__(self, parent=None):
        QMenu.__init__(self)
        self.parent = parent

        self.stations_menu = self.addMenu("Stations")
        self.add_stations()

        self.addSeparator()

        self.action_pause = QAction(
                QIcon(":icons/media-playback-pause.png"), "Pause", self)
        self.action_pause.triggered.connect(self.parent.radio.action_pause.emit)
        self.action_pause.setEnabled(False)
        self.addAction(self.action_pause)

        self.action_stop = QAction(
                QIcon(":icons/media-playback-stop.png"), "Stop", self)
        self.action_stop.triggered.connect(self.parent.radio.action_stop.emit)
        self.action_stop.setEnabled(False)
        self.addAction(self.action_stop)

        self.addSeparator()

        action = QAction(
                QIcon(":icons/application-exit.png"), "&Close", self)
        action.triggered.connect(QApplication.quit)
        self.addAction(action)

    def add_stations(self):
        self.stations = {}
        group = QActionGroup(self)
        group.setExclusive(True)
        for name in sorted(self.parent.stations.map.keys()):
            url = self.parent.stations.map[name]
            self.stations[name] = QAction(str(name), self)
            self.stations[name].setCheckable(True)
            self.stations[name].setActionGroup(group)
            self.stations[name].triggered.connect(
                    lambda _=0, st=(name, url):
                    self.parent.station_changed.emit(st))
            self.stations_menu.addAction(self.stations[name])
