#!/usr/bin/env python3

class YouTubeConfiguration:
  '''
  Class that contains configuration used by downloader.
  '''
  _link = None # Link to be downloaded
  _directory = None # Where to download files
  _audio_only = True # Download audio only
  _playlist = False # Download playlist

  @property
  def link(self):
    return self._link

  @link.setter
  def link(self, link):
    self._link = link

  @property
  def audio_only(self):
    return self._audio_only

  @audio_only.setter
  def audio_only(self, audio):
    self._audio_only = audio

  @property
  def playlist(self):
    return self._playlist
  
  @playlist.setter
  def playlist(self, playlist):
    self._playlist = playlist

  @property
  def directory(self):
    return self._directory
  
  @directory.setter
  def directory(self, dir):
    self._directory = dir

  def __str__(self):
    return """
YouTube Configuration Parameters:
Link: %s
Audio only: %s
Playlist: %s
""" % (self.link, self.audio_only, self.playlist)