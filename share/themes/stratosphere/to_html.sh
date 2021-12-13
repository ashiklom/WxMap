#!/bin/sh

echo '<html>'
echo '<body bgcolor="#000000" text="white">'

#echo '<table style="width:100%">'
echo '<table>'

while read iname; do

  field=`echo $iname | cut -d'.' -f1`
  level=`echo $iname | cut -d'.' -f2`
  bname=`basename $iname`
  thumb=`basename $iname ".png"`.thumb.png
  imtag='<img src="'$thumb'">'

  echo '<tr>'

  echo '<td align="center" valign="center">'
  echo '<a href="https://portal.nccs.nasa.gov/datashare/gmao_ops/pub/fp/.internal/stratosphere/nps/'$iname'">'$imtag'</a>'

  echo '</td>'
  echo '</tr>'

done

echo '</body>'
echo '</html>'


exit 0
