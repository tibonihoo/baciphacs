#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import namedtuple
import math

DataSample = namedtuple("DataSample","label value stdev")


def GenerateHTMLHorizontalBar(relWidth,relErrorWidth):
  """Generate the HTML code of an horizontal bar included in a potentially wider chart.
  'relWidth': amplitude of the bar as a proportion of the full chart's width (between 0 and 1)
  'relErrorWidth': proportion of the error margin wrt to the full chart's width.
  The error margin is shown before and after the tip of the bar.
  Pre-requisite: relWidth+relErrorWidth<=1.
  """
  if not (0. <= relWidth <= 1.):
    raise ValueError("Invalid relwidth '%s', it must be between 0 and 1" % relWidth)
  if not (0. <= relErrorWidth <= 1.):
    raise ValueError("Invalid relwidth '%s', it must be between 0 and 1" % relErrorWidth)
  if relWidth+relErrorWidth>1.:
    raise ValueError("Invalid relwidth and relErrorwidth (%s,%s), their sum must not be greater than one" % (relErrorWidth,relErrorWidth))
  # use floor to amplify a little the error bar
  firstPartWidth = math.floor(100*min(1.,max(0,relWidth-relErrorWidth)))
  secondPartWidth = 100*relWidth-firstPartWidth
  thirdPartWidth = min(math.ceil(100*relErrorWidth),100-secondPartWidth-firstPartWidth)
  return """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%%">
<tr>
  <td style="width:%.0f%%;height:1ex;background-color:blue;"></td>
  <td style="width:%.0f%%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:%.0f%%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""" % (firstPartWidth,secondPartWidth,thirdPartWidth)

def GenerateHTMLLabelledRow(label,title,htmlRowData):
  """Generate a <tr> row with the given label and data.
  'label' a string to be set at the begining of the row.
  'title' the title associated to the full row (typically visible in a tooltip)
  'htmlRowData' the html content to be put next to the label (in a <td> tag)
  Note: the htmlRowData will be indented appropriately.
  """
  return """\
<tr title="%s">
  <th style="margin-top:.2ex;padding-right:1ex;text-align:right;">%s</th>
  <td style="margin-top:.2ex;width:100%%;">
%s
  </td>
</tr>""" % (title,label,"\n".join("    %s"%line for line in htmlRowData.splitlines()))

def GenerateHTMLHorizontalBarChart(dataSamples,numStdev):
  """Generate the code of an HTML table showing one horizontal bar for each data sample.
  Error bars are also shown for each dataSample at 'value+/-(numStdev*stdev)'.
  'dataSamples' a list of Datasample instances.
  'numStdev' the size of the error margin as a number of each sample's standard deviation.
  """
  norm = max(ds.value+(numStdev*ds.stdev) for ds in dataSamples)
  bars = [ GenerateHTMLHorizontalBar(float(d.value)/norm,float(numStdev*d.stdev)/norm) for d in dataSamples ]
  return """\
<table cellspacing="0" cellpadding="0" border="0" style="width:80ex;font-family:monospace;">
%s
</table>""" % "\n".join([GenerateHTMLLabelledRow(d.label,"%s(+/-%s)"%(d.value,numStdev*d.stdev),b) for d,b in zip(dataSamples,bars)])
