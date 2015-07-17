mysql binlog:

    mysqlbinlog /path/to/mysql-bin.000999 | \
      grep -i -e "^update" -e "^insert" -e "^delete" -e "^replace" -e "^alter" | \
      cut -c1-100 | tr '[A-Z]' '[a-z]' | \
      sed -e "s/\t/ /g;s/\`//g;s/(.*$//;s/ set .*$//;s/ as .*$//" | sed -e "s/ where .*$//" | \
      sort | uniq -c | sort -nr 

The Slow Query Log:
    
    
    show variables like 'long_query_time';
    
    SET GLOBAL general_log = 'OFF';
    SET GLOBAL slow_query_log = 'OFF';
