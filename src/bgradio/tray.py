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

from PyQt4.QtCore import QPoint
from PyQt4.QtGui import QSystemTrayIcon, QIcon

from bgradio.menu import Menu

class Tray(QSystemTrayIcon):
    """System Tray"""

    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self)
        self.parent = parent
        self.menu = Menu(self.parent)
        self.setIcon(QIcon(
            ":icons/network-wireless-connected-25.png"))
        self.setVisible(True)
        self.activated.connect(self.on_activated)
        self.show()

    def show_message(self, title, message):
        self.showMessage(title, message, QSystemTrayIcon.NoIcon, 5000)

    def on_activated(self, event):
        rect = self.geometry()
        x, y = rect.x(), rect.y()
        if event in (self.Context, self.Trigger):
            self.setContextMenu(self.menu)
            self.contextMenu().popup(QPoint(x, y))
