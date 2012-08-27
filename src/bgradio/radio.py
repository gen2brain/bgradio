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

from PyQt4.QtCore import QThread, pyqtSignal

from bgradio import vlc
from bgradio.playlist import Playlist

class Radio(QThread):
    """VLC Radio"""

    action_play = pyqtSignal(tuple)
    action_pause = pyqtSignal()
    action_stop = pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self)
        self.parent = parent
        self.title = None
        self.genre = None

        self.vlc = vlc.Instance()
        self.player = self.vlc.media_player_new()

        self.action_play.connect(self.on_play)
        self.action_pause.connect(self.on_pause)
        self.action_stop.connect(self.on_stop)

        self.event = self.player.event_manager()
        for event in [vlc.EventType.MediaPlayerOpening,
                vlc.EventType.MediaPlayerBuffering,
                vlc.EventType.MediaPlayerStopped,
                vlc.EventType.MediaPlayerPlaying,
                vlc.EventType.MediaPlayerPaused]:
            self.event.event_attach(event, self.on_state_changed)

    def get_metadata(self):
        try:
            self.media.parse()
            self.title = self.media.get_meta(vlc.Meta.Title)
            self.genre = self.media.get_meta(vlc.Meta.Genre)
        except IndexError, err:
            sys.stderr.write("metaData IndexError: %s\n" % str(err))

    def on_play(self, station):
        name, url = station
        playlist = Playlist(url, self).parse()
        if playlist:
            self.media = self.vlc.media_new(playlist[0])
            self.player.set_media(self.media)
            self.player.play()

    def on_pause(self):
        if self.player.is_playing():
            self.player.pause()
        else:
            self.player.play()

    def on_stop(self):
        self.player.stop()

    def run(self):
        self.exec_()

    def on_state_changed(self, event):
        if event.type == vlc.EventType.MediaPlayerOpening:
            self.parent.state_changed.emit("loading")
        elif event.type == vlc.EventType.MediaPlayerBuffering:
            self.parent.state_changed.emit("buffering")
        elif event.type == vlc.EventType.MediaPlayerStopped:
            self.parent.state_changed.emit("stopped")
        elif event.type == vlc.EventType.MediaPlayerPlaying:
            self.get_metadata()
            self.parent.state_changed.emit("playing")
        elif event.type == vlc.EventType.MediaPlayerPaused:
            self.parent.state_changed.emit("paused")
