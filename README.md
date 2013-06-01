baciphacs
=========

Bar charts in pure HTML and CSS.

This library is designed for the kind of (desesperate) situation where
you want to display bar charts but with the constraint that your HTML
document must not depend on additional files or remote webservices.

baciphacs will use basic HTML code with some bits of CSS style embeded
in tags, to display a reasonably readable chart.

If you need pretty or advanced graphs and don't have any strict
constraints on your HTML's dependency, many libraries exists that
generate much much better looking graphs.

baciphacs is licensed under [the 2 close BSD License](LICENSE.txt),
and more detailed information about it can be found at
[GitHub](https://github.com/tibonihoo/baciphacs).


Example for horizontal bar charts
---------------------------------

```python
from baciphacs import DataSample
from baciphacs import GenerateHTMLHorizontalBarChart

data = [("ba",3,2),("c",6,1),("i",2,1),("p",4,1),("h",4,1),("a",3,1),("cs",3,2)]
dataSamples = [DataSample._make(t) for t in data]
print GenerateHTMLHorizontalBarChart(dataSamples,numStdev=2,color="blue")
```

<table cellspacing="0" cellpadding="0" border="0" style="width:80ex;font-family:monospace;">
<tr title="3(+/-4)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">ba</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:0%;height:1ex;background-color:blue;"></td>
      <td style="width:38%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:50%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="6(+/-2)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">c</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:50%;height:1ex;background-color:blue;"></td>
      <td style="width:25%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:25%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="2(+/-2)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">i</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:0%;height:1ex;background-color:blue;"></td>
      <td style="width:25%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:25%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="4(+/-2)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">p</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:25%;height:1ex;background-color:blue;"></td>
      <td style="width:25%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:25%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="4(+/-2)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">h</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:25%;height:1ex;background-color:blue;"></td>
      <td style="width:25%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:25%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="3(+/-2)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">a</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:12%;height:1ex;background-color:blue;"></td>
      <td style="width:26%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:25%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
<tr title="3(+/-4)">
  <th style="padding-top:.5ex;padding-right:1ex;text-align:right;">cs</th>
  <td style="padding-top:.5ex;width:100%;">
    <table cellspacing="0" cellpadding="0" border="0" style="width:100%">
    <tr>
      <td style="width:0%;height:1ex;background-color:blue;"></td>
      <td style="width:38%;height:1ex;background-color:blue;text-align:left">|</td>
      <td style="width:50%;height:1ex;text-align:right">|</td>
      <td></td>
    </tr>
    </table>
  </td>
</tr>
</table>

