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

  def test_generate_bar_with_relErrorWidth_rounding_to_upper_int_increase_left_error_width(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.353,.1765)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:17%;height:1ex;background-color:blue;"></td>
  <td style="width:18%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:18%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)

  def test_generate_bar_with_relErrorWidth_rounding_to_lower_int_increase_right_error_width(self):
    htmlSnippet = GenerateHTMLHorizontalBar(.226,.113)
    self.assertEqual(
      """\
<table cellspacing="0" cellpadding="0" border="0" style="width:100%">
<tr>
  <td style="width:11%;height:1ex;background-color:blue;"></td>
  <td style="width:12%;height:1ex;background-color:blue;text-align:left">|</td>
  <td style="width:12%;height:1ex;text-align:right">|</td>
  <td></td>
</tr>
</table>""",
      htmlSnippet)
    
class TestGenerateHTMLLabelledRow(unittest.TestCase):

  def test_generate_row_with_label_is_ok(self):
    htmlSnippet = GenerateHTMLLabelledRow("my_label","my_title","MARKER")
    self.assertEqual(
      """\
<tr title="my_title">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="padding-top:.5ex;width:100%;">
    MARKER
  </td>
</tr>""",
      htmlSnippet)

  def test_generate_row_with_label_and_multine_data_is_indented_correctly(self):
    htmlSnippet = GenerateHTMLLabelledRow("my_label","my_title","MARKER\nOTHER")
    self.assertEqual(
      """\
<tr title="my_title">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="padding-top:.5ex;width:100%;">
    MARKER
    OTHER
  </td>
</tr>""",
      htmlSnippet)

class TestGenerateHTMLHorizontalBarChart(unittest.TestCase):

  def test_generate_bar_chart_with_single_sample(self):
    htmlSnippet = GenerateHTMLHorizontalBarChart([DataSample("my_label",6,1)],3)
    self.assertEqual("""\
<table cellspacing="0" cellpadding="0" border="0" style="width:80ex;font-family:monospace;">
<tr title="6(+/-3)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:33%;height:1ex;background-color:blue;"></td>
      <td style="width:34%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:33%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
</table>""",htmlSnippet)

  def test_generate_bar_chart_with_more_than_one_sample(self):
    htmlSnippet = GenerateHTMLHorizontalBarChart([DataSample("my_label",6,1),DataSample("other_label",5,4)],3)
    self.assertEqual("""\
<table cellspacing="0" cellpadding="0" border="0" style="width:80ex;font-family:monospace;">
<tr title="6(+/-3)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">my_label</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:17%;height:1ex;background-color:blue;"></td>
      <td style="width:18%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:18%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="5(+/-12)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">other_label</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:0%;height:1ex;background-color:blue;"></td>
      <td style="width:29%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:71%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
</table>""",htmlSnippet)

if __name__ == '__main__':
  unittest.main()
