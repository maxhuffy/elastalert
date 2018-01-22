# elastalert
Easy &amp; Flexible Alerting With ElasticSearch

Ingalls Version
Requires a config.yaml and smtp-auth.yaml in the /src/ directory!

config.yaml
~~~~ 
es_host: 
es_port: 9200
use_ssl: True
verify_certs: False
es_username: 
es_password: 
smtp_host: smtp.gmail.com
smtp_port: 465
smtp_ssl : true
from_addr: 
smtp_auth_file: /elastalert/smtp-auth.yaml
rules_folder: rules
run_every:
  minutes: 15
buffer_time:
  minutes: 15
writeback_index: elastalert_status
alert_time_limit:
  days: 1
~~~~ 

smtp-auth.yaml
~~~~ 
user: 
password: 
~~~~ 

Instructions:
>docker pull iinfosec/elasticsearch:elastalert
>docker run -it iinfosec/elasticsearch:elastalert python /elastalert/elastalert/elastalert.py
