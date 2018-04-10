### For Debug:


```
:0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name opentype'.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
2018-04-10 10:08:42,281 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 71 - WARNING - Channel sender status, disconnected
2018-04-10 10:08:42,282 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 73 - WARNING - Channel receiver status, disconnected
2018-04-10 10:08:42,287 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-10 10:08:42,291 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-10 10:08:42,727 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Cancel"
2018-04-10 10:08:43,062 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Ack"
2018-04-10 10:08:43,062 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Nack"
2018-04-10 10:08:43,838 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file a05f0e70-5d94-4874-8c17-51a981d88ce4.json, deleted
2018-04-10 10:08:43,839 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file bf6dc365-d16b-4569-9d8c-eda4ed21a095.json, deleted
2018-04-10 10:08:43,839 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file e606d8de-d632-4e93-a614-699a59bb728c.json, deleted
2018-04-10 10:08:44,074 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 0953d8bf-1627-4679-b857-1425376dd157.json, deleted
2018-04-10 10:08:44,075 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 1fe15a1b-2f43-457a-94cb-01a8c9b50fb4.json, deleted
2018-04-10 10:08:44,075 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file da3e8523-bfd0-48fe-aa3f-d4ecb8ddd5b1.json, deleted
2018-04-10 10:08:44,076 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file d9194d6f-403a-4166-9cc0-6f6b3fb467cd.json, deleted
2018-04-10 10:08:44,076 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 833730af-695b-4b45-8a9a-a2a63faf479a.json, deleted
2018-04-10 10:08:44,854 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 5f465bde-cd57-4114-be31-52ed1daa3d59.json, deleted
2018-04-10 10:08:44,855 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 89249dbf-749c-434e-809f-b0100a048a25.json, deleted
2018-04-10 10:08:44,855 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 96d6083f-b2b7-4a6c-9e86-c9ccddb56abc.json, deleted
2018-04-10 10:08:44,856 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 65b8983f-511b-47c2-bc2a-0939dce40325.json, deleted
2018-04-10 10:08:44,856 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 9a7d729a-ccb0-4dde-a3c8-7dd1feb03ffd.json, deleted
2018-04-10 10:08:44,857 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file e1f248ca-7d64-4950-b32a-e2af6a4598c9.json, deleted
2018-04-10 10:08:44,857 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file 635085f1-9bdb-4dce-abd2-66ba0655ee18.json, deleted
2018-04-10 10:08:44,858 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file c521f3aa-96bd-4875-9183-e5727f190a32.json, deleted
2018-04-10 10:08:44,858 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 38 - WARNING - Expired event file aba91ee6-87a8-4a34-9282-20c26a912a68.json, deleted
2018-04-10 10:09:04,326 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-10 10:09:04,330 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-10 10:09:26,357 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-10 10:09:26,362 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-10 10:09:48,394 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-10 10:09:48,397 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
^CMonitor process(31489) got GracefulExitException.
Channel process(31490) got GracefulExitException.
Main process(31488) got GracefulExitException.
```

![amqp_message.png](https://raw.githubusercontent.com/xm2cloud/xm2cloud_agent/master/screenshot/amqp_message.png)
