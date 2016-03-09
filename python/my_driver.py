#!/usr/bin/env python2.7
# This is free and unencumbered software released into the public domain.
from conreality import ddk

class MyArgumentParser(ddk.ArgumentParser):
  def init(self):
    self.add_argument('id', nargs='?', default='default',
      help='the ID of the camera to attach to')
    self.add_argument('-r', '--fps', type=int, default=30,
      help='set the frames per second (FPS) rate (default: 30)')

class MyDriver(ddk.Driver):
  def init(self):
    pass # TODO

  def exit(self):
    pass # TODO

  def loop(self):
    while True:
      self.pause() # TODO

if __name__ == '__main__':
  MyDriver(argparser=MyArgumentParser).run()
