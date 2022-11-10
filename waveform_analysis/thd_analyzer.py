#!/usr/bin/env python3
import argparse
import sys

#from ..waveform_analysis._common import analyze_channels
#from ..waveform_analysis.thd import THDN
from _common import analyze_channels
from thd import THDN


#print('Frequency: %f Hz' % (fs * (true_i / len(windowed))))
#
#    print("THD+N:      %.4f%% or %.1f dB"    % (THDN  * 100, 20 * log10(THDN)))
#    print("A-weighted: %.4f%% or %.1f dB(A)" % (THDNA * 100, 20 * log10(THDNA)))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Calculate THD+N of a given audio file')
  parser.add_argument('filename')
  args = parser.parse_args()
  if args.filename is None:
    sys.exit('No filename')

  try:
      analyze_channels(args.filename, THDN)
  except IOError:
      print('Couldn\'t analyze "' + args.filename + '"\n')
  print('')
