#! /bin/bash
date_in_file=`tail -1 /val/log/simple.log | cut -d' ' -f1,2|cut -d',' -f1`
date_in_file_in_format=`date +%s -d "$date_in_file"`
current_date=`date +%s`
rashozhdenie=$[$current_date-$date_in_file_in_format]
if (( rashozhdenie > 600 )); then

/usr/bin/sendEmail -f from_user@nop.nop -t to_user@nop.nop -u "Critical. Logs is none $rashozhdenie sec" -m "Critical. Logs is none $rashozhdenie sec" -o message-charset=UTF-8

fi

