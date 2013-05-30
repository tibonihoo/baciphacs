#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import namedtuple


DataSample = namedtuple("DataSample","label value stdev")


def GenerateHTMLHorizontalBar(relWidth,relErrorWidth):
  """Generate the HTML code of an horizontal bar included in a potentially wider chart.
  'relWidth': amplitude of the bar as a proportion of the full chart's width (between 0 and 1)
  'relErrorWidth': proportion of the error margin wrt to the full chart's width.
  The error margin is shown before and after the tip of the bar.
  """
  if not (0. < relWidth < 1.):
    raise ValueError("Invalid relwidth '%s', it must be between 0 and 1" % relWidth)
  if not (0. < relErrorWidth < 1.):
    raise ValueError("Invalid relwidth '%s', it must be between 0 and 1" % relErrorWidth)
  firstPartWidth = max(0,relWidth-relErrorWidth)
  secondPartWidth = relWidth - relErrorWidth
  return """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%%">
  <tr>
    <td style="width:%.1f%%;height:1ex;background-color:blue;"></td>
    <td style="width:%.1f%%;height:1ex;background-color:blue;text-align:left">|</td>
    <td style="width:%.1f%%;height:1ex;text-align:right">|</td>
    <td></td>
  </tr>
</table>""" % (firstPartWidth,secondPartWidth,relErrorWidth)

  
