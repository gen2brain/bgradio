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

from PyQt4.phonon import Phonon
from PyQt4.QtCore import QThread, pyqtSignal

from bgradio.playlist import Playlist

class Radio(QThread):
    """Phonon Radio"""

    action_play = pyqtSignal(tuple)
    action_pause = pyqtSignal()
    action_stop = pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self)
        self.parent = parent
        self.title = None
        self.genre = None
        self.media = Phonon.MediaObject()
        self.audio = Phonon.AudioOutput(Phonon.MusicCategory)
        self.path = Phonon.createPath(self.media, self.audio)

        self.action_play.connect(self.on_play)
        self.action_pause.connect(self.on_pause)
        self.action_stop.connect(self.on_stop)
        self.media.stateChanged.connect(self.on_state_changed)

    def set_source(self, source):
        source = Phonon.MediaSource(source)
        if source.type() != -1:
            self.media.setCurrentSource(source)

    def get_metadata(self):
        try:
            self.title = self.media.metaData(Phonon.TitleMetaData)[0]
            self.genre = self.media.metaData(Phonon.GenreMetaData)[0]
        except IndexError, err:
            sys.stderr.write("metaData IndexError: %s\n" % str(err))

    def on_play(self, station):
        name, url = station
        playlist = Playlist(url, self).parse()
        if playlist:
            self.set_source(playlist[0])
            self.media.play()

    def on_pause(self):
        state = self.media.state()
        if state == Phonon.PlayingState:
            self.media.pause()
        elif state == Phonon.PausedState:
            self.media.play()

    def on_stop(self):
        self.media.stop()

    def run(self):
        self.exec_()

    def on_state_changed(self, state, oldstate):
        if state == Phonon.LoadingState:
            self.parent.state_changed.emit("loading")
        elif state == Phonon.BufferingState:
            self.parent.state_changed.emit("buffering")
        elif state == Phonon.StoppedState and \
                oldstate == Phonon.PlayingState:
            self.parent.state_changed.emit("stopped")
        elif state == Phonon.PlayingState:
            self.get_metadata()
            self.parent.state_changed.emit("playing")
        elif state == Phonon.PausedState:
            self.parent.state_changed.emit("paused")
        elif state == Phonon.ErrorState:
            self.parent.state_changed.emit("error")

