#!/usr/bin/env python3

from pytube import YouTube, Playlist
from YouTubeConfiguration import YouTubeConfiguration
import os, sys

class YouTubeDownloaderException(Exception):
  pass

class WrongConfigurationClassException(YouTubeDownloaderException):
  pass

class LinkIsNotAStringException(YouTubeDownloaderException):
  pass

class DirectoryIsNotAStringException(YouTubeDownloaderException):
  pass

class DirectoryDoesNotExist(YouTubeDownloaderException):
  pass

class YouTubeDownloader:
  '''
  Class that performs download.
  '''

  def ___init___(self):
    self._youtube_config = None # YouTubeConfiguration class.

  def __init__(self, configuration):
    if not isinstance(configuration, YouTubeConfiguration):
      raise WrongConfigurationClassException()
    self._youtube_config = configuration
    self._check_configuration()

  def _check_configuration(self):
    if not isinstance(self._youtube_config, YouTubeConfiguration):
      raise WrongConfigurationClassException()
    if (not isinstance(self._youtube_config.link, str)) or self._youtube_config.link is None:
      raise LinkIsNotAStringException()
    if (not isinstance(self._youtube_config.directory, str)) or self._youtube_config.directory is None:
      print(self._youtube_config.directory)
      raise DirectoryIsNotAStringException()
    if (not os.path.exists(self._youtube_config.directory)):
      raise DirectoryDoesNotExist() 

  def download_single(self, video_link):
    youtube = YouTube(video_link)
    streams = youtube.streams
    # Choose best stream (sound or video)
    stream = streams.get_audio_only() if self._youtube_config._audio_only else streams.get_highest_resolution()
    # Create file name?
    title = youtube.title.replace(" ", "_")
    # Download
    stream.download(output_path=self._youtube_config.directory, filename=title)

  def download(self):
    try:
      # Check if configuration is set
      self._check_configuration()
    except YouTubeDownloader.WrongConfigurationClassException:
      print("Youtube downloader got unaproperiate class as configuration.")
      sys.exit(16)
    except YouTubeDownloader.LinkIsNotAStringException:
      print("Youtube downloader got link which was not a string.")
      sys.exit(17)
    except YouTubeDownloader.DirectoryIsNotAStringException:
      print("Youtube downloader got directory which is not a string.")
      sys.exit(18)
    except YouTubeDownloader.DirectoryDoesNotExistException:
      print("Youtube downloader got directory that doesn't exist.")
      sys.exit(19)
    # Download single file
    if self._youtube_config.playlist == False:
      self.download_single(self._youtube_config.link)
    # Download playlist
    else:
      pl = Playlist(self._youtube_config.link)
      for video in pl.video_urls:
        self.download_single(video)
