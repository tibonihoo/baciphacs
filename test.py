#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from baciphacs import DataSample
from baciphacs import GenerateHTMLHorizontalBar

class TestGenerateHTMLHorizontalBar(unittest.TestCase):
  
  def test_generate_bar_with_values_is_ok(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.6,.1)
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

  def test_generate_bar_with_stdev_bigger_than_value_first_part_is_null(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.1,.3)
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
    
  def test_generate_bar_with_negative_relWidth_raises_exception(self):
    self.assertRaises(ValueError,GenerateHTMLHorizontalBar,-.6,.3)

  def test_generate_bar_with_negative_relErrorWidth_raises_exception(self):
    self.assertRaises(ValueError,GenerateHTMLHorizontalBar,.6,-.3)
    
  def test_generate_bar_with_relWidth_greater_than_one_raises_exception(self):
    self.assertRaises(ValueError,GenerateHTMLHorizontalBar,6,.3)

  def test_generate_bar_with_relErrorWidth_greater_than_one_raises_exception(self):
    self.assertRaises(ValueError,GenerateHTMLHorizontalBar,.6,3)


    
if __name__ == '__main__':
  unittest.main()
