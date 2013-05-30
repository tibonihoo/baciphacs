#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import namedtuple


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
  firstPartWidth = min(1.,max(0,relWidth-relErrorWidth))
  secondPartWidth = relWidth-firstPartWidth
  return """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%%">
<tr>
  <td style="width:%.0f%%;height:1ex;background-color:blue;"></td>
  <td style="width:%.0f%%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:%.0f%%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""" % (100*firstPartWidth,100*secondPartWidth,100*relErrorWidth)

def GenerateHTMLLabelledRow(label,htmlRowData):
  """Generate a <tr> row with the given label and data.
  'label' a string to be set at the begining of the row.
  'htmlRowData' the html content to be put next to the label (in a <td> tag)
  Note: the htmlRowData will be indented appropriately.
  """
  return """\
<tr>
  <th style="margin-top:.2ex;padding-right:1ex;text-align:right;">%s</th>
  <td style="margin-top:.2ex;width:100%%;">
%s
  </td>
</tr>""" % (label,"\n".join("    %s"%line for line in htmlRowData.splitlines()))

def GenerateHTMLHorizontalBarChart(dataSamples,numStdev):
  norm = max(ds.value+(numStdev*ds.stdev) for ds in dataSamples)
  bars = [ GenerateHTMLHorizontalBar(float(d.value)/norm,float(numStdev*d.stdev)/norm) for d in dataSamples ]
  return """\
<table cellspacing="0" cellpadding="0" border="0" style="width:50ex">
%s
</table>""" % "\n".join([GenerateHTMLLabelledRow(d.label,b) for b in bars])
