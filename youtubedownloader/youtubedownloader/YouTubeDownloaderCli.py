#!/usr/bin/env python3

import sys, getopt, os
from YouTubeConfiguration import YouTubeConfiguration
from YouTubeDownloader import YouTubeDownloader

def usage(message_text, exit_code=1):
  sys.exit(exit_code)

def help():
  print('''youtubedownloader.py -l link

Downloads video or mp3 from youtube.
-a, --audio-only    Downloads only audio. Set by default.
-d, --directory     Path where to download files.
-l, --link          Youtube link to be downloaded.
-h, --help          Prints this help message.
-v, --video         Downloads audio + video. Default is audio only.''')
  sys.exit()

def main(argv):
  ytconfig = YouTubeConfiguration()
  try:
    opts, args = getopt.getopt(argv, 'ad:l:hpv', [ 'audio-only', 'directory=', 'help', 'link=', 'playlist', 'video' ] )
  except getopt.GetoptError:
    usage('youtubedownloader.py -l link', 5)
  for opt, arg in opts:
    if opt in ['-l', '--link']:
      ytconfig.link = str(arg)
    elif opt in ['-v', '--video']:
      ytconfig.audio_only = False
    elif opt in ['-a', '--audio-only']:
      ytconfig.audio_only = True
    elif opt in ['-p', '--playlist']:
      ytconfig.playlist = True
    elif opt in ['-d', '--directory']:
      ytconfig.directory = str(arg)
    elif opt in ['-h', '--help']:
      help()
  #print(ytconfig)
  yt = YouTubeDownloader(ytconfig)
  yt.download()

if __name__ == "__main__":
  main(sys.argv[1:])
