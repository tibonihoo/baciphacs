#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from baciphacs import DataSample
from baciphacs import GenerateSampleBar

class TestGenerateSampleBar(unittest.TestCase):
  
  def test_trivial_sample_bar_is_ok(self):
    d = DataSample("mouf",6,1)
    htmlSnippet = GenerateSampleBar(d,maxAmplitude=10,numStdev=2)
    self.assertTrue(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
  <tr>
    <td style="width:40%;height:1ex;background-color:blue;"></td>
    <td style="width:20%;height:1ex;background-color:blue;text-align:left">|</td>
    <td style="width:20%;height:1ex;text-align:right">|</td>
    <td></td>
  </tr>
</table>""",
      htmlSnippet)

  def test_sample_with_stdev_bigger_than_value_bar_first_part_is_null(self):
    d = DataSample("mouf",1,3)
    htmlSnippet = GenerateSampleBar(d,maxAmplitude=10,numStdev=2)
    self.assertTrue(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
  <tr>
    <td style="width:0%;height:1ex;background-color:blue;"></td>
    <td style="width:10%;height:1ex;background-color:blue;text-align:left">|</td>
    <td style="width:60%;height:1ex;text-align:right">|</td>
    <td></td>
  </tr>
</table>""",
      htmlSnippet)
    
  def test_sample_with_negative_stdev_raises_exception(self):
    d = DataSample("mouf",6,-3)
    self.assertRaises(ValueError,GenerateSampleBar,d,maxAmplitude=10,numStdev=2)

  def test_sample_with_negative_value_raises_exception(self):
    d = DataSample("mouf",-6,3)
    self.assertRaises(ValueError,GenerateSampleBar,d,maxAmplitude=10,numStdev=2)
    
  def test_negative_numStdev_raises_exception(self):
    d = DataSample("mouf",6,3)
    self.assertRaises(ValueError,GenerateSampleBar,d,maxAmplitude=10,numStdev=-2)

if __name__ == '__main__':
  unittest.main()
