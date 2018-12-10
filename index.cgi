#!/bin/sh

echo Content-type: text/html
echo 
title="SVG Text circle"


count=$(echo $QUERY_STRING | pcregrep -o1 '(?<=&|^)count=([^&$]*)')
count=${count:-2}
cat index_extends.pug | pug -P -p $PWD/default.pug -b $DOCUMENT_ROOT -O "{title: '$title', count: $count}" 2>&1


# For include-version:
# cat $DOCUMENT_ROOT/static/pug/default.pug | pug -P -p $PWD/default.pug 2>&1