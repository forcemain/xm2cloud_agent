### For Arch:
#### xm2cloud_agent is a powerful and graceful engine component for xm2cloud devops framework.


### For Task:
```
{
	"event_uuid": "0c563eef-34e5-48de-8a86-cc2965aa0d1a",
	"event_source": "xm2cloud_agent",
	"source_cluster_id": [1],
	"event_id": "0702c0ab-3fa1-4590-9247-9279904c0188",
	"metric_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94",
	"target_host_id": [1],
	"handled_event_id": null,
	"source_host_id": 1,
	"event_data": "{\"interpreter\": \"bash\", \"scripttext\": \"ping www.baidu.com\"}",
	"handled_event_host_id": null,
	"enc_method": null,
	"chain_event_id": null,
	"event_timestamp": 1524214567,
	"source_version": "0.0.1",
	"handled_event_cluster_id": null,
	"event_name": "execute_script",
	"target_hostgroup_id": null,
	"target_cluster_id": null,
	"source_hostgroup_id": [14],
	"handled_event_hostgroup_id": null
}
```

### For Debug:


```
:0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name opentype'.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
2018-04-20 17:14:40,256 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:14:43
2018-04-20 17:14:40,262 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 65 - INFO - Connecting to ops.xxoo.com:5672
2018-04-20 17:14:40,263 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:14:43
2018-04-20 17:14:40,265 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 126 - INFO - Connecting to ops.xxoo.com:5672
2018-04-20 17:14:40,265 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 73 - WARNING - Channel sender status, disconnected
2018-04-20 17:14:40,266 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 75 - WARNING - Channel receiver status, disconnected
2018-04-20 17:14:40,267 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:14:43
2018-04-20 17:14:40,272 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-20 17:14:40,275 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-20 17:14:40,305 - pika.adapters.base_connection - /Library/Python/2.7/site-packages/pika/adapters/base_connection.py - 217 - INFO - Connecting to 000.000.000.000:5672
2018-04-20 17:14:40,305 - pika.adapters.base_connection - /Library/Python/2.7/site-packages/pika/adapters/base_connection.py - 217 - INFO - Connecting to 000.000.000.000:5672
2018-04-20 17:14:40,584 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 42 - INFO - Connection opened
2018-04-20 17:14:40,584 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 52 - INFO - Adding connection close callback
2018-04-20 17:14:40,585 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 76 - INFO - Creating a new channel
2018-04-20 17:14:40,613 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 49 - INFO - Connection opened
2018-04-20 17:14:40,613 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 59 - INFO - Adding connection close callback
2018-04-20 17:14:40,614 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 88 - INFO - Creating a new channel
2018-04-20 17:14:40,657 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 80 - INFO - Channel opened
2018-04-20 17:14:40,658 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 89 - INFO - Adding channel close callback
2018-04-20 17:14:40,658 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 98 - INFO - Declaring exchange event_down_exchange
2018-04-20 17:14:40,659 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 122 - INFO - Issuing consumer related RPC commands
2018-04-20 17:14:40,659 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 128 - INFO - Adding consumer cancellation callback
2018-04-20 17:14:40,689 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 92 - INFO - Channel opened
2018-04-20 17:14:40,690 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 101 - INFO - Adding channel close callback
2018-04-20 17:14:40,690 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 110 - INFO - Declaring exchange event_up_exchange
2018-04-20 17:14:40,691 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 134 - INFO - Issuing consumer related RPC commands
2018-04-20 17:14:40,691 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 139 - INFO - Issuing Confirm.Select RPC command
2018-04-20 17:14:40,691 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:40,733 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 104 - INFO - Exchange declared
2018-04-20 17:14:40,734 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 108 - INFO - Declaring queue event_down_queue
2018-04-20 17:14:40,767 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 116 - INFO - Exchange declared
2018-04-20 17:14:40,771 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 120 - INFO - Declaring queue event_up_queue
2018-04-20 17:14:40,844 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 113 - INFO - Binding event_down_exchange to event_down_queue with event_engine.rpc
2018-04-20 17:14:40,883 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 125 - INFO - Binding event_up_exchange to event_up_queue with event_engine.rpc
2018-04-20 17:14:40,890 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 118 - INFO - Queue bound
2018-04-20 17:14:40,891 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 122 - INFO - Issuing consumer related RPC commands
2018-04-20 17:14:40,891 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 128 - INFO - Adding consumer cancellation callback
2018-04-20 17:14:40,891 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Cancel"
2018-04-20 17:14:40,931 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 130 - INFO - Queue bound
2018-04-20 17:14:40,932 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 134 - INFO - Issuing consumer related RPC commands
2018-04-20 17:14:40,932 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 139 - INFO - Issuing Confirm.Select RPC command
2018-04-20 17:14:40,933 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Ack"
2018-04-20 17:14:40,933 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Nack"
2018-04-20 17:14:40,934 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:41,694 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 1
2018-04-20 17:14:41,694 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 2
2018-04-20 17:14:41,695 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 3
2018-04-20 17:14:41,695 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 4
2018-04-20 17:14:41,695 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:41,749 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 1
2018-04-20 17:14:41,749 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 4 messages, 3 have yet to be confirmed, 1 were acked and 0 were nacked
2018-04-20 17:14:41,750 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 2
2018-04-20 17:14:41,750 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 4 messages, 2 have yet to be confirmed, 2 were acked and 0 were nacked
2018-04-20 17:14:41,754 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 3
2018-04-20 17:14:41,754 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 4 messages, 1 have yet to be confirmed, 3 were acked and 0 were nacked
2018-04-20 17:14:41,754 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 4
2018-04-20 17:14:41,754 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 4 messages, 0 have yet to be confirmed, 4 were acked and 0 were nacked
2018-04-20 17:14:41,937 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:42,700 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:42,943 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:43,259 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:14:46
2018-04-20 17:14:43,267 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:14:46
2018-04-20 17:14:43,267 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:14:46
2018-04-20 17:14:43,706 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 5
2018-04-20 17:14:43,707 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:43,757 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 5
2018-04-20 17:14:43,757 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 5 messages, 0 have yet to be confirmed, 5 were acked and 0 were nacked
2018-04-20 17:14:43,948 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:44,711 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:44,948 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:45,717 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:45,954 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:46,261 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:14:49
2018-04-20 17:14:46,269 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:14:49
2018-04-20 17:14:46,269 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:14:49
2018-04-20 17:14:46,722 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 6
2018-04-20 17:14:46,722 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:46,773 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 6
2018-04-20 17:14:46,773 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 6 messages, 0 have yet to be confirmed, 6 were acked and 0 were nacked
2018-04-20 17:14:46,956 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:47,308 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 115 - INFO - Events ready, next scheduled at 2018-04-20 17:15:02
2018-04-20 17:14:47,727 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 7
2018-04-20 17:14:47,727 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 8
2018-04-20 17:14:47,727 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 9
2018-04-20 17:14:47,728 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 10
2018-04-20 17:14:47,728 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 11
2018-04-20 17:14:47,728 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 12
2018-04-20 17:14:47,729 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 13
2018-04-20 17:14:47,729 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:47,807 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 7
2018-04-20 17:14:47,807 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 13 messages, 6 have yet to be confirmed, 7 were acked and 0 were nacked
2018-04-20 17:14:47,878 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 8
2018-04-20 17:14:47,878 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 13 messages, 5 have yet to be confirmed, 8 were acked and 0 were nacked
2018-04-20 17:14:47,931 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 9
2018-04-20 17:14:47,931 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 13 messages, 4 have yet to be confirmed, 9 were acked and 0 were nacked
2018-04-20 17:14:47,937 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 10
2018-04-20 17:14:47,937 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 13 messages, 3 have yet to be confirmed, 10 were acked and 0 were nacked
2018-04-20 17:14:47,962 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 14
2018-04-20 17:14:47,962 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 15
2018-04-20 17:14:47,962 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 16
2018-04-20 17:14:47,963 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:47,964 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 11
2018-04-20 17:14:47,964 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 16 messages, 5 have yet to be confirmed, 11 were acked and 0 were nacked
2018-04-20 17:14:48,014 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 12
2018-04-20 17:14:48,015 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 16 messages, 4 have yet to be confirmed, 12 were acked and 0 were nacked
2018-04-20 17:14:48,023 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 13
2018-04-20 17:14:48,024 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 16 messages, 3 have yet to be confirmed, 13 were acked and 0 were nacked
2018-04-20 17:14:48,083 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 14
2018-04-20 17:14:48,084 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 16 messages, 2 have yet to be confirmed, 14 were acked and 0 were nacked
2018-04-20 17:14:48,093 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 15
2018-04-20 17:14:48,093 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 16 messages, 1 have yet to be confirmed, 15 were acked and 0 were nacked
2018-04-20 17:14:48,143 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 16
2018-04-20 17:14:48,143 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 16 messages, 0 have yet to be confirmed, 16 were acked and 0 were nacked
2018-04-20 17:14:48,733 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:48,966 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:49,263 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:14:52
2018-04-20 17:14:49,271 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:14:52
2018-04-20 17:14:49,272 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:14:52
2018-04-20 17:14:49,737 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 17
2018-04-20 17:14:49,737 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:49,805 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 17
2018-04-20 17:14:49,805 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 17 messages, 0 have yet to be confirmed, 17 were acked and 0 were nacked
2018-04-20 17:14:49,971 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:50,743 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:50,975 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:51,749 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:51,977 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:52,264 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:14:55
2018-04-20 17:14:52,272 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:14:55
2018-04-20 17:14:52,275 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:14:55
2018-04-20 17:14:52,753 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 18
2018-04-20 17:14:52,753 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:52,833 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 18
2018-04-20 17:14:52,833 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 18 messages, 0 have yet to be confirmed, 18 were acked and 0 were nacked
2018-04-20 17:14:52,982 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:53,757 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:53,985 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:54,762 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:54,990 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:55,266 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:14:58
2018-04-20 17:14:55,274 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:14:58
2018-04-20 17:14:55,278 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:14:58
2018-04-20 17:14:55,764 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 19
2018-04-20 17:14:55,765 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:55,848 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 19
2018-04-20 17:14:55,848 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 19 messages, 0 have yet to be confirmed, 19 were acked and 0 were nacked
2018-04-20 17:14:55,996 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:56,767 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:57,000 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:57,772 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:58,005 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:58,269 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:01
2018-04-20 17:14:58,275 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:01
2018-04-20 17:14:58,281 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:01
2018-04-20 17:14:58,773 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 20
2018-04-20 17:14:58,774 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:58,841 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 20
2018-04-20 17:14:58,842 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 20 messages, 0 have yet to be confirmed, 20 were acked and 0 were nacked
2018-04-20 17:14:59,010 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:14:59,779 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:00,011 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:00,783 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:01,013 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:01,271 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:04
2018-04-20 17:15:01,276 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:04
2018-04-20 17:15:01,283 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:04
2018-04-20 17:15:01,789 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 21
2018-04-20 17:15:01,789 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:01,877 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 21
2018-04-20 17:15:01,877 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 21 messages, 0 have yet to be confirmed, 21 were acked and 0 were nacked
2018-04-20 17:15:02,018 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:02,330 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-20 17:15:02,333 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-20 17:15:02,792 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 22
2018-04-20 17:15:02,792 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 23
2018-04-20 17:15:02,793 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 24
2018-04-20 17:15:02,793 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:02,873 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 22
2018-04-20 17:15:02,873 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 24 messages, 2 have yet to be confirmed, 22 were acked and 0 were nacked
2018-04-20 17:15:02,874 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 23
2018-04-20 17:15:02,874 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 24 messages, 1 have yet to be confirmed, 23 were acked and 0 were nacked
2018-04-20 17:15:02,877 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 24
2018-04-20 17:15:02,877 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 24 messages, 0 have yet to be confirmed, 24 were acked and 0 were nacked
2018-04-20 17:15:03,024 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:03,796 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:04,028 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:04,273 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:07
2018-04-20 17:15:04,279 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:07
2018-04-20 17:15:04,285 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:07
2018-04-20 17:15:04,802 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 25
2018-04-20 17:15:04,803 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:04,886 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 25
2018-04-20 17:15:04,886 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 25 messages, 0 have yet to be confirmed, 25 were acked and 0 were nacked
2018-04-20 17:15:05,032 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:05,807 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:06,033 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:06,810 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:07,039 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:07,273 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:10
2018-04-20 17:15:07,280 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:10
2018-04-20 17:15:07,287 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:10
2018-04-20 17:15:07,813 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 26
2018-04-20 17:15:07,814 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:07,867 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 26
2018-04-20 17:15:07,868 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 26 messages, 0 have yet to be confirmed, 26 were acked and 0 were nacked
2018-04-20 17:15:08,044 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:08,819 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:09,050 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:09,368 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 115 - INFO - Events ready, next scheduled at 2018-04-20 17:15:24
2018-04-20 17:15:09,824 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 27
2018-04-20 17:15:09,825 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 28
2018-04-20 17:15:09,825 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 29
2018-04-20 17:15:09,826 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 30
2018-04-20 17:15:09,826 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 31
2018-04-20 17:15:09,826 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 32
2018-04-20 17:15:09,827 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 33
2018-04-20 17:15:09,827 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:09,913 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 27
2018-04-20 17:15:09,914 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 6 have yet to be confirmed, 27 were acked and 0 were nacked
2018-04-20 17:15:09,915 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 28
2018-04-20 17:15:09,915 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 5 have yet to be confirmed, 28 were acked and 0 were nacked
2018-04-20 17:15:09,917 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 29
2018-04-20 17:15:09,917 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 4 have yet to be confirmed, 29 were acked and 0 were nacked
2018-04-20 17:15:09,920 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 30
2018-04-20 17:15:09,920 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 3 have yet to be confirmed, 30 were acked and 0 were nacked
2018-04-20 17:15:09,925 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 31
2018-04-20 17:15:09,926 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 2 have yet to be confirmed, 31 were acked and 0 were nacked
2018-04-20 17:15:09,927 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 32
2018-04-20 17:15:09,928 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 1 have yet to be confirmed, 32 were acked and 0 were nacked
2018-04-20 17:15:09,929 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 33
2018-04-20 17:15:09,929 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 33 messages, 0 have yet to be confirmed, 33 were acked and 0 were nacked
2018-04-20 17:15:10,055 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:10,275 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:13
2018-04-20 17:15:10,282 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:13
2018-04-20 17:15:10,290 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:13
2018-04-20 17:15:10,832 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 34
2018-04-20 17:15:10,833 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:10,884 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 34
2018-04-20 17:15:10,884 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 34 messages, 0 have yet to be confirmed, 34 were acked and 0 were nacked
2018-04-20 17:15:11,057 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:11,839 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:12,063 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:12,841 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:13,069 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:13,277 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:16
2018-04-20 17:15:13,284 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:16
2018-04-20 17:15:13,293 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:16
2018-04-20 17:15:13,842 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 35
2018-04-20 17:15:13,843 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:13,905 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 35
2018-04-20 17:15:13,906 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 35 messages, 0 have yet to be confirmed, 35 were acked and 0 were nacked
2018-04-20 17:15:14,072 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:14,844 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:15,074 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:15,849 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:16,079 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:16,278 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:19
2018-04-20 17:15:16,286 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:19
2018-04-20 17:15:16,295 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:19
2018-04-20 17:15:16,851 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 36
2018-04-20 17:15:16,851 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:16,918 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 36
2018-04-20 17:15:16,918 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 36 messages, 0 have yet to be confirmed, 36 were acked and 0 were nacked
2018-04-20 17:15:17,083 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:17,856 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:18,085 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:18,860 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:19,090 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:19,281 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 219 - INFO - Events ready, next scheduled at 2018-04-20 17:15:22
2018-04-20 17:15:19,283 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 122 - INFO - Start handle local event: execute_script
2018-04-20 17:15:19,283 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: Start handle local event: execute_script
2018-04-20 17:15:19,286 - agent.handler.engine.user.execute_script - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/user/execute_script.py - 39 - INFO - agent.handler.engine.user.execute_script.ExecuteScriptEngineHandler handle event: <agent.models:
{
    "handled_event_host_id": null,
    "event_source": "xm2cloud_agent",
    "target_hostgroup_id": null,
    "source_cluster_id": [
        1
    ],
    "event_id": "0702c0ab-3fa1-4590-9247-9279904c0188",
    "metric_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94",
    "target_host_id": [
        1
    ],
    "source_host_id": 1,
    "target_cluster_id": null,
    "event_name": "execute_script",
    "enc_method": null,
    "chain_event_id": null,
    "event_timestamp": 1524215690,
    "source_version": "0.0.1",
    "handled_event_cluster_id": null,
    "handled_event_hostgroup_id": null,
    "event_uuid": "0c563eef-34e5-48de-8a86-cc2965aa0d1a",
    "event_data": "{\"interpreter\": \"bash\", \"scripttext\": \"ping www.baidu.com\"}",
    "source_hostgroup_id": [
        14
    ],
    "handled_event_id": null
}>
2018-04-20 17:15:19,287 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:22
2018-04-20 17:15:19,297 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:22
2018-04-20 17:15:19,864 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 37
2018-04-20 17:15:19,865 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 38
2018-04-20 17:15:19,865 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:19,918 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 37
2018-04-20 17:15:19,918 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 38 messages, 1 have yet to be confirmed, 37 were acked and 0 were nacked
2018-04-20 17:15:19,919 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 38
2018-04-20 17:15:19,919 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 38 messages, 0 have yet to be confirmed, 38 were acked and 0 were nacked
2018-04-20 17:15:20,092 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:20,334 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: PING www.a.shifen.com (115.239.211.112): 56 data bytes
2018-04-20 17:15:20,338 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: Request timeout for icmp_seq 0
2018-04-20 17:15:20,347 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=1 ttl=53 time=12.877 ms
2018-04-20 17:15:20,866 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 39
2018-04-20 17:15:20,867 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 40
2018-04-20 17:15:20,867 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 41
2018-04-20 17:15:20,867 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:20,919 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 39
2018-04-20 17:15:20,919 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 41 messages, 2 have yet to be confirmed, 39 were acked and 0 were nacked
2018-04-20 17:15:20,920 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 40
2018-04-20 17:15:20,920 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 41 messages, 1 have yet to be confirmed, 40 were acked and 0 were nacked
2018-04-20 17:15:20,920 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 41
2018-04-20 17:15:20,921 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 41 messages, 0 have yet to be confirmed, 41 were acked and 0 were nacked
2018-04-20 17:15:21,097 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:21,347 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=2 ttl=53 time=11.524 ms
2018-04-20 17:15:21,873 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 42
2018-04-20 17:15:21,873 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:21,961 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 42
2018-04-20 17:15:21,962 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 42 messages, 0 have yet to be confirmed, 42 were acked and 0 were nacked
2018-04-20 17:15:22,102 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:22,282 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:25
2018-04-20 17:15:22,288 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:25
2018-04-20 17:15:22,299 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:25
2018-04-20 17:15:22,369 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=3 ttl=53 time=31.960 ms
2018-04-20 17:15:22,876 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 43
2018-04-20 17:15:22,877 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 44
2018-04-20 17:15:22,877 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:22,941 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 43
2018-04-20 17:15:22,941 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 44 messages, 1 have yet to be confirmed, 43 were acked and 0 were nacked
2018-04-20 17:15:22,942 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 44
2018-04-20 17:15:22,942 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 44 messages, 0 have yet to be confirmed, 44 were acked and 0 were nacked
2018-04-20 17:15:23,104 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:23,381 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=4 ttl=53 time=39.236 ms
2018-04-20 17:15:23,883 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 45
2018-04-20 17:15:23,883 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:23,961 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 45
2018-04-20 17:15:23,964 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 45 messages, 0 have yet to be confirmed, 45 were acked and 0 were nacked
2018-04-20 17:15:24,105 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:24,376 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-20 17:15:24,377 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-20 17:15:24,380 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=5 ttl=53 time=34.337 ms
2018-04-20 17:15:24,890 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 46
2018-04-20 17:15:24,890 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 47
2018-04-20 17:15:24,891 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 48
2018-04-20 17:15:24,891 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 49
2018-04-20 17:15:24,891 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:24,953 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 46
2018-04-20 17:15:24,953 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 49 messages, 3 have yet to be confirmed, 46 were acked and 0 were nacked
2018-04-20 17:15:24,954 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 47
2018-04-20 17:15:24,954 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 49 messages, 2 have yet to be confirmed, 47 were acked and 0 were nacked
2018-04-20 17:15:24,958 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 48
2018-04-20 17:15:24,958 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 49 messages, 1 have yet to be confirmed, 48 were acked and 0 were nacked
2018-04-20 17:15:24,959 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 49
2018-04-20 17:15:24,960 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 49 messages, 0 have yet to be confirmed, 49 were acked and 0 were nacked
2018-04-20 17:15:25,109 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:25,284 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:28
2018-04-20 17:15:25,290 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:28
2018-04-20 17:15:25,302 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:28
2018-04-20 17:15:25,365 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=6 ttl=53 time=15.447 ms
2018-04-20 17:15:25,905 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 50
2018-04-20 17:15:25,905 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 51
2018-04-20 17:15:25,905 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:25,955 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 50
2018-04-20 17:15:25,956 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 51 messages, 1 have yet to be confirmed, 50 were acked and 0 were nacked
2018-04-20 17:15:25,957 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 51
2018-04-20 17:15:25,957 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 51 messages, 0 have yet to be confirmed, 51 were acked and 0 were nacked
2018-04-20 17:15:26,113 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:26,369 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=7 ttl=53 time=15.197 ms
2018-04-20 17:15:26,912 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 52
2018-04-20 17:15:26,912 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:26,968 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 52
2018-04-20 17:15:26,968 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 52 messages, 0 have yet to be confirmed, 52 were acked and 0 were nacked
2018-04-20 17:15:27,116 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:27,367 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=8 ttl=53 time=8.867 ms
2018-04-20 17:15:27,916 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 53
2018-04-20 17:15:27,916 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:27,968 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 53
2018-04-20 17:15:27,968 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 53 messages, 0 have yet to be confirmed, 53 were acked and 0 were nacked
2018-04-20 17:15:28,118 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:28,285 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:31
2018-04-20 17:15:28,291 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:31
2018-04-20 17:15:28,304 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:31
2018-04-20 17:15:28,384 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=9 ttl=53 time=23.344 ms
2018-04-20 17:15:28,921 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 54
2018-04-20 17:15:28,922 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 55
2018-04-20 17:15:28,922 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:28,971 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 54
2018-04-20 17:15:28,972 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 55 messages, 1 have yet to be confirmed, 54 were acked and 0 were nacked
2018-04-20 17:15:28,973 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 55
2018-04-20 17:15:28,974 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 55 messages, 0 have yet to be confirmed, 55 were acked and 0 were nacked
2018-04-20 17:15:29,122 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:29,371 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=10 ttl=53 time=9.889 ms
2018-04-20 17:15:29,925 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 56
2018-04-20 17:15:29,925 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:29,978 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 56
2018-04-20 17:15:29,978 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 56 messages, 0 have yet to be confirmed, 56 were acked and 0 were nacked
2018-04-20 17:15:30,125 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:30,406 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: 64 bytes from 115.239.211.112: icmp_seq=11 ttl=53 time=44.277 ms
2018-04-20 17:15:30,408 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 137 - INFO - Finish handle local event: execute_script
2018-04-20 17:15:30,408 - agent.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/engine/baseengine.py - 66 - INFO - Event 0702c0ab-3fa1-4590-9247-9279904c0188 stdout: Finish handle local event: execute_script
2018-04-20 17:15:30,409 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 169 - INFO - Send response_execute_script event, retcode: None, result: None
2018-04-20 17:15:30,928 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 57
2018-04-20 17:15:30,928 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 58
2018-04-20 17:15:30,929 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 59
2018-04-20 17:15:30,929 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:30,980 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 57
2018-04-20 17:15:30,980 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 59 messages, 2 have yet to be confirmed, 57 were acked and 0 were nacked
2018-04-20 17:15:30,983 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 58
2018-04-20 17:15:30,983 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 59 messages, 1 have yet to be confirmed, 58 were acked and 0 were nacked
2018-04-20 17:15:30,984 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 59
2018-04-20 17:15:30,984 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 59 messages, 0 have yet to be confirmed, 59 were acked and 0 were nacked
2018-04-20 17:15:31,126 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:31,287 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:34
2018-04-20 17:15:31,293 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:34
2018-04-20 17:15:31,310 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:34
2018-04-20 17:15:31,400 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 115 - INFO - Events ready, next scheduled at 2018-04-20 17:15:46
2018-04-20 17:15:31,936 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 60
2018-04-20 17:15:31,936 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 61
2018-04-20 17:15:31,937 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 62
2018-04-20 17:15:31,937 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 63
2018-04-20 17:15:31,937 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 64
2018-04-20 17:15:31,938 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 65
2018-04-20 17:15:31,938 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 66
2018-04-20 17:15:31,939 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 67
2018-04-20 17:15:31,939 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:31,988 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 60
2018-04-20 17:15:31,989 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 7 have yet to be confirmed, 60 were acked and 0 were nacked
2018-04-20 17:15:31,992 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 61
2018-04-20 17:15:31,992 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 6 have yet to be confirmed, 61 were acked and 0 were nacked
2018-04-20 17:15:31,993 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 62
2018-04-20 17:15:31,993 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 5 have yet to be confirmed, 62 were acked and 0 were nacked
2018-04-20 17:15:31,995 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 63
2018-04-20 17:15:31,995 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 4 have yet to be confirmed, 63 were acked and 0 were nacked
2018-04-20 17:15:32,001 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 64
2018-04-20 17:15:32,001 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 3 have yet to be confirmed, 64 were acked and 0 were nacked
2018-04-20 17:15:32,002 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 65
2018-04-20 17:15:32,002 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 2 have yet to be confirmed, 65 were acked and 0 were nacked
2018-04-20 17:15:32,003 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 66
2018-04-20 17:15:32,003 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 1 have yet to be confirmed, 66 were acked and 0 were nacked
2018-04-20 17:15:32,003 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 67
2018-04-20 17:15:32,003 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 67 messages, 0 have yet to be confirmed, 67 were acked and 0 were nacked
2018-04-20 17:15:32,128 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:32,944 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:33,131 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:33,944 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:34,136 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:34,289 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:37
2018-04-20 17:15:34,295 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:37
2018-04-20 17:15:34,311 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:37
2018-04-20 17:15:34,947 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 68
2018-04-20 17:15:34,947 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:34,996 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 68
2018-04-20 17:15:34,996 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 68 messages, 0 have yet to be confirmed, 68 were acked and 0 were nacked
2018-04-20 17:15:35,139 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:35,952 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:36,143 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:36,954 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:37,144 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:37,290 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:40
2018-04-20 17:15:37,297 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:40
2018-04-20 17:15:37,315 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:40
2018-04-20 17:15:37,960 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 69
2018-04-20 17:15:37,961 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:38,013 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 69
2018-04-20 17:15:38,014 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 69 messages, 0 have yet to be confirmed, 69 were acked and 0 were nacked
2018-04-20 17:15:38,149 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:38,963 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:39,154 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:39,966 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:40,156 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:40,291 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:43
2018-04-20 17:15:40,297 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:43
2018-04-20 17:15:40,319 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:43
2018-04-20 17:15:40,972 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 70
2018-04-20 17:15:40,973 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:41,058 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 70
2018-04-20 17:15:41,058 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 70 messages, 0 have yet to be confirmed, 70 were acked and 0 were nacked
2018-04-20 17:15:41,158 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:41,974 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:42,164 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:42,977 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:43,167 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:43,293 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:46
2018-04-20 17:15:43,299 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:46
2018-04-20 17:15:43,321 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:46
2018-04-20 17:15:43,982 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 71
2018-04-20 17:15:43,983 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:44,051 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 71
2018-04-20 17:15:44,051 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 71 messages, 0 have yet to be confirmed, 71 were acked and 0 were nacked
2018-04-20 17:15:44,169 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:44,984 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:45,174 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:45,988 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:46,175 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:46,294 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:49
2018-04-20 17:15:46,301 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:49
2018-04-20 17:15:46,323 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:49
2018-04-20 17:15:46,424 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-20 17:15:46,427 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-20 17:15:46,991 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 72
2018-04-20 17:15:46,992 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 73
2018-04-20 17:15:46,992 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 74
2018-04-20 17:15:46,992 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 75
2018-04-20 17:15:46,993 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:47,045 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 72
2018-04-20 17:15:47,046 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 75 messages, 3 have yet to be confirmed, 72 were acked and 0 were nacked
2018-04-20 17:15:47,047 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 73
2018-04-20 17:15:47,048 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 75 messages, 2 have yet to be confirmed, 73 were acked and 0 were nacked
2018-04-20 17:15:47,049 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 74
2018-04-20 17:15:47,049 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 75 messages, 1 have yet to be confirmed, 74 were acked and 0 were nacked
2018-04-20 17:15:47,051 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 75
2018-04-20 17:15:47,052 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 75 messages, 0 have yet to be confirmed, 75 were acked and 0 were nacked
2018-04-20 17:15:47,181 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:47,995 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:48,185 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:48,998 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:49,186 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:49,296 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:52
2018-04-20 17:15:49,302 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:52
2018-04-20 17:15:49,326 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:52
2018-04-20 17:15:50,000 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 76
2018-04-20 17:15:50,001 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:50,067 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 76
2018-04-20 17:15:50,068 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 76 messages, 0 have yet to be confirmed, 76 were acked and 0 were nacked
2018-04-20 17:15:50,191 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:51,005 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:51,196 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:52,006 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:52,197 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:52,298 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:55
2018-04-20 17:15:52,305 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:55
2018-04-20 17:15:52,332 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:55
2018-04-20 17:15:53,007 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 77
2018-04-20 17:15:53,008 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:53,085 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 77
2018-04-20 17:15:53,085 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 77 messages, 0 have yet to be confirmed, 77 were acked and 0 were nacked
2018-04-20 17:15:53,199 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:53,443 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 115 - INFO - Events ready, next scheduled at 2018-04-20 17:16:08
2018-04-20 17:15:54,011 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 78
2018-04-20 17:15:54,011 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 79
2018-04-20 17:15:54,011 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 80
2018-04-20 17:15:54,012 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 81
2018-04-20 17:15:54,012 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 82
2018-04-20 17:15:54,012 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 83
2018-04-20 17:15:54,013 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 84
2018-04-20 17:15:54,013 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:54,083 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 78
2018-04-20 17:15:54,083 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 6 have yet to be confirmed, 78 were acked and 0 were nacked
2018-04-20 17:15:54,084 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 79
2018-04-20 17:15:54,084 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 5 have yet to be confirmed, 79 were acked and 0 were nacked
2018-04-20 17:15:54,085 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 80
2018-04-20 17:15:54,085 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 4 have yet to be confirmed, 80 were acked and 0 were nacked
2018-04-20 17:15:54,087 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 81
2018-04-20 17:15:54,087 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 3 have yet to be confirmed, 81 were acked and 0 were nacked
2018-04-20 17:15:54,088 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 82
2018-04-20 17:15:54,088 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 2 have yet to be confirmed, 82 were acked and 0 were nacked
2018-04-20 17:15:54,088 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 83
2018-04-20 17:15:54,089 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 1 have yet to be confirmed, 83 were acked and 0 were nacked
2018-04-20 17:15:54,089 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 84
2018-04-20 17:15:54,089 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 84 messages, 0 have yet to be confirmed, 84 were acked and 0 were nacked
2018-04-20 17:15:54,203 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:55,015 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:55,207 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:55,301 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:15:58
2018-04-20 17:15:55,306 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:15:58
2018-04-20 17:15:55,336 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:15:58
2018-04-20 17:15:56,022 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 85
2018-04-20 17:15:56,022 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:56,111 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 85
2018-04-20 17:15:56,111 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 85 messages, 0 have yet to be confirmed, 85 were acked and 0 were nacked
2018-04-20 17:15:56,212 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:57,024 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:57,218 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:58,028 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:58,228 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:58,302 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 206 - INFO - No events ready, next scheduled at 2018-04-20 17:16:01
2018-04-20 17:15:58,308 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-20 17:16:01
2018-04-20 17:15:58,339 - agent.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-20 17:16:01
2018-04-20 17:15:59,029 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 86
2018-04-20 17:15:59,030 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:15:59,108 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 86
2018-04-20 17:15:59,109 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 86 messages, 0 have yet to be confirmed, 86 were acked and 0 were nacked
2018-04-20 17:15:59,233 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:16:00,030 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-20 17:16:00,237 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
^CHeartbeat process(83148) got GracefulExitException.
Channel process(83147) got GracefulExitException.
2018-04-20 17:16:00,692 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 183 - INFO - Stopping
2018-04-20 17:16:00,692 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 174 - INFO - Closing the channel
2018-04-20 17:16:00,693 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 529 - INFO - Closing channel (0): 'Normal shutdown' on <Channel number=1 OPEN conn=<SelectConnection OPEN socket=('192.168.3.239', 63559)->('000.000.000.000', 5672) params=<ConnectionParameters host=ops.xxoo.com port=5672 virtual_host=/event_engine ssl=False>>>
2018-04-20 17:16:00,693 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 191 - INFO - Closing connection
2018-04-20 17:16:00,694 - pika.connection - /Library/Python/2.7/site-packages/pika/connection.py - 1147 - INFO - Closing connection (200): Normal shutdown
2018-04-20 17:16:00,694 - pika.connection - /Library/Python/2.7/site-packages/pika/connection.py - 1159 - INFO - Connection.close is waiting for 1 channels to close: <SelectConnection CLOSING socket=('192.168.3.239', 63559)->('000.000.000.000', 5672) params=<ConnectionParameters host=ops.xxoo.com port=5672 virtual_host=/event_engine ssl=False>>
2018-04-20 17:16:00,694 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 188 - INFO - Stopped
Main process(83143) got GracefulExitException.
2018-04-20 17:16:00,695 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 162 - INFO - Stopping
2018-04-20 17:16:00,695 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 146 - INFO - Sending a Basic.Cancel RPC command to RabbitMQ
2018-04-20 17:16:00,695 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 166 - INFO - Stopped
Monitor process(83146) got GracefulExitException.
Engine process(83145) got GracefulExitException.

```
