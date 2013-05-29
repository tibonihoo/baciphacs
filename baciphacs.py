#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import namedtuple


DataSample = namedtuple("DataSample","label value stdev")


def GenerateSampleBar(dataSample,maxAmplitude,numStdev):
  """Generate the HTML code of the bar corresponding to a given data sample.
  'dataSample': the data sample to represent (instance of DataSample).
  'maxAmplitude': maximum value (over all samples include their value+numStdev*stdev).
  'numStdev': set how many times the stdev should the error bars indicate.
  """
  if dataSample.value<0:
    raise ValueError("Invalid data sample '%s', the value is expected to be positive" % str(dataSample))
  if dataSample.stdev<0:
    raise ValueError("Invalid data sample '%s', the stdev is expected to be positive" % str(dataSample))
  if numStdev<0:
    raise ValueError("Invalid numStdev '%s', it must be positive" % numStdev)
  valueProportion = float(dataSample.value)/float(maxAmplitude)
  stdevProportion = float(dataSample.stdev)/float(maxAmplitude)
  firstPartWidth = max(0,valueProportion-numStdev*stdevProportion)
  secondPartWidth = valueProportion-firstPartWidth
  thirdPartWidth = numStdev*stdevProportion
  return """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%%">
  <tr>
    <td style="width:%.1f%%;height:1ex;background-color:blue;"></td>
    <td style="width:%.1f%%;height:1ex;background-color:blue;text-align:left">|</td>
    <td style="width:%.1f%%;height:1ex;text-align:right">|</td>
    <td></td>
  </tr>
</table>""" % (firstPartWidth,secondPartWidth,thirdPartWidth)

  
