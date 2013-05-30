#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from baciphacs import DataSample
from baciphacs import GenerateHTMLHorizontalBar
from baciphacs import GenerateHTMLLabelledRow
from baciphacs import GenerateHTMLHorizontalBarChart


class TestGenerateHTMLHorizontalBar(unittest.TestCase):
  
  def test_generate_bar_with_values_is_ok(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.6,.1)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:50%;height:1ex;background-color:blue;"></td>
  <td style="width:10%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:10%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)

  def test_generate_bar_with_stdev_bigger_than_value_first_part_is_null(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.1,.3)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:0%;height:1ex;background-color:blue;"></td>
  <td style="width:10%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:30%;height:1ex;text-align:right">|</td>
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
    
  def test_generate_bar_with_relErrorWidth_plus_relWidth_greater_than_one_raises_exception(self):
    self.assertRaises(ValueError,GenerateHTMLHorizontalBar,.6,.5)
    
  def test_generate_bar_with_relErrorWidth_0_is_ok(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.1,0)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:10%;height:1ex;background-color:blue;"></td>
  <td style="width:0%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:0%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)

  def test_generate_bar_with_relWidth_0_is_ok(self):
    htmlSnippet = GenerateHTMLHorizontalBar(0,.3)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:0%;height:1ex;background-color:blue;"></td>
  <td style="width:0%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:30%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)
    
  def test_generate_bar_with_relWidth_1_is_ok(self):
    htmlSnippet = GenerateHTMLHorizontalBar(1.,0)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:100%;height:1ex;background-color:blue;"></td>
  <td style="width:0%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:0%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)

  def test_generate_bar_with_relErrorWidth_1_is_ok(self):
    htmlSnippet = GenerateHTMLHorizontalBar(0,1)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:0%;height:1ex;background-color:blue;"></td>
  <td style="width:0%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:100%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)


class TestGenerateHTMLLabelledRow(unittest.TestCase):

  def test_generate_row_with_label_is_ok(self):
    htmlSnippet = GenerateHTMLLabelledRow("my_label","MARKER")
    self.assertEqual(
      """\
<tr>
  <th style="margin-top:.2ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="margin-top:.2ex;">
    MARKER
  </td>
</tr>""",
      htmlSnippet)

  def test_generate_row_with_label_and_multine_data_is_indented_correctly(self):
    htmlSnippet = GenerateHTMLLabelledRow("my_label","MARKER\nOTHER")
    self.assertEqual(
      """\
<tr>
  <th style="margin-top:.2ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="margin-top:.2ex;">
    MARKER
    OTHER
  </td>
</tr>""",
      htmlSnippet)

class TestGenerateHTMLHorizontalBarChart(unittest.TestCase):

  def test_generate_bar_chart_with_single_sample(self):
    htmlSnippet = GenerateHTMLHorizontalBarChart([DataSample("my_label",6,1)],3)
    self.assertEqual("""\
<table cellspacing="0" cellpadding="0" border="0" style="width:50ex">
<tr>
  <th style="margin-top:.2ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="margin-top:.2ex;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:33%;height:1ex;background-color:blue;"></td>
      <td style="width:33%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:33%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
</table>""",htmlSnippet)


    
if __name__ == '__main__':
  unittest.main()
