#!/usr/bin/env python3

import unittest,os

from youtubedownloader.YouTubeConfiguration import YouTubeConfiguration
from youtubedownloader.YouTubeDownloader import YouTubeDownloader, WrongConfigurationClassException, LinkIsNotAStringException, DirectoryDoesNotExist, DirectoryIsNotAStringException

class YouTubeDownloaderLink(unittest.TestCase):
  def test_initial_configuration_raise_exception(self):
    with self.assertRaises(WrongConfigurationClassException):
      YouTubeDownloader('Test')

  def test_check_configuration_raise_exception_wrong_link(self):
    yc = YouTubeConfiguration()
    with self.assertRaises(LinkIsNotAStringException):
      YouTubeDownloader(yc)

  def test_check_configuration_raise_exception_wrong_directory(self):
    yc = YouTubeConfiguration()
    yc.link = 'Link'
    with self.assertRaises(DirectoryIsNotAStringException):
      YouTubeDownloader(yc)

  def test_check_configuration_raise_exception_not_existing_directory(self):
    yc = YouTubeConfiguration()
    yc.link = 'Link'
    yc.directory = '/tmp/a/b/c/d/e/f/g'
    with self.assertRaises(DirectoryDoesNotExist):
      YouTubeDownloader(yc)

  def test_download_single_file(self):
    yc = YouTubeConfiguration()
    yc.link = 'https://www.youtube.com/watch?v=d5P5Tz3VH94'
    yc.directory = '/tmp'
    yc._audio_only = True
    yd = YouTubeDownloader(yc)
    yd.download()
    fn = 'ALESTORM_-_Hangover_(Taio_Cruz_Cover)__Napalm_Records.mp4'
    p = yc.directory + '/' + fn
    self.assertTrue(os.path.exists(p))
    os.remove(p)

  def test_download_playlist(self):
    yc = YouTubeConfiguration()
    yc.link = 'https://www.youtube.com/watch?v=d5P5Tz3VH94&list=PLDAh7xyZ0aiitM04Tve5z0NQx5okjcVpk'
    yc.directory = '/tmp'
    #p = yc.directory + '/' + fn
    yc._audio_only = True
    yc.playlist = True
    yd = YouTubeDownloader(yc)
    yd.download()
    fns = [ 'ALESTORM_-_Hangover_(Taio_Cruz_Cover)__Napalm_Records.mp4', 'ALESTORM_-_Drink_(Official_Video)__Napalm_Records.mp4',
            'ALESTORM_-_Mexico_(Official_Video)__Napalm_Records.mp4', 'ALESTORM_-_Shipwrecked__Napalm_Records.mp4',
            'ALESTORM_-_Alestorm_(Official_Video)__Napalm_Records.mp4' ]
    for fn in fns:
      p = yc.directory + '/' + fn
      self.assertTrue(os.path.exists(p))
      os.remove(p)

if __name__ == '__main__':
  unittest.main()
