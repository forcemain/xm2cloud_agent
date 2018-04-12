### For Arch:
![xm2cloud.png](https://raw.githubusercontent.com/xm2cloud/xm2cloud_agent/master/docs/screenshot/design/xm2cloud.png)

### For Debug:


```
2018-04-11 23:33:36,491 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._load.Collector [Errno 2] No such file or directory: '/proc/loadavg'
2018-04-11 23:33:36,492 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 101 - ERROR - Call plugin agent.metrics.host._cpu.Collector [Errno 2] No such file or directory: '/proc/stat'
2018-04-11 23:33:36,492 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 88 - DEBUG - Verified monitor event data: <agent.metrics.host._df.Df:
{
    "df_bytes_used_percentage": {
        "name": "df.bytes.used.percentage",
        "value": 22.1,
        "tags": {
            "device": "disk1s1",
            "mount": "/"
        }
    },
    "df_bytes_free": {
        "name": "df.bytes.free",
        "value": 193201545216,
        "tags": {
            "device": "disk1s1",
            "mount": "/"
        }
    },
    "df_bytes_total": {
        "name": "df.bytes.used",
        "value": 54657937408,
        "tags": {
            "device": "disk1s1",
            "mount": "/"
        }
    }
}>
2018-04-11 23:33:36,494 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 88 - DEBUG - Verified monitor event data: <agent.metrics.host._df.Df:
{
    "df_bytes_used_percentage": {
        "name": "df.bytes.used.percentage",
        "value": 1.1,
        "tags": {
            "device": "disk1s4",
            "mount": "/private/var/vm"
        }
    },
    "df_bytes_free": {
        "name": "df.bytes.free",
        "value": 193201545216,
        "tags": {
            "device": "disk1s4",
            "mount": "/private/var/vm"
        }
    },
    "df_bytes_total": {
        "name": "df.bytes.used",
        "value": 2147504128,
        "tags": {
            "device": "disk1s4",
            "mount": "/private/var/vm"
        }
    }
}>
2018-04-11 23:33:37,187 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 63
2018-04-11 23:33:37,187 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 64
2018-04-11 23:33:37,188 - agent.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_agent/agent/handler/channel/rabbitmq.py - 83 - INFO - Published message # 65
2018-04-11 23:33:37,188 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-11 23:33:37,188 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 311 - DEBUG - add_timeout: added timeout 5925860671553823760; deadline=1 at 1523460818.19
2018-04-11 23:33:37,243 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 69 - DEBUG - Go check channel sender disconnected
2018-04-11 23:33:37,244 - agent.core.channel - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/channel.py - 80 - DEBUG - Go check channel receiver disconnected
2018-04-11 23:33:37,244 - agent.core.engine - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/engine.py - 110 - INFO - No events ready, next scheduled at 2018-04-11 23:33:40
2018-04-11 23:33:37,358 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 220 - DEBUG - Processing 1:Basic.Ack
2018-04-11 23:33:37,358 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 234 - DEBUG - Calling <bound method RabbitMQChannelSender.on_delivery_confirmation of <agent.handler.channel.rabbitmq.RabbitMQChannelSender object at 0x103179c90>> for "1:Basic.Ack"
2018-04-11 23:33:37,359 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 63
2018-04-11 23:33:37,359 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 65 messages, 13 have yet to be confirmed, 52 were acked and 0 were nacked
2018-04-11 23:33:37,359 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 220 - DEBUG - Processing 1:Basic.Ack
2018-04-11 23:33:37,360 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 234 - DEBUG - Calling <bound method RabbitMQChannelSender.on_delivery_confirmation of <agent.handler.channel.rabbitmq.RabbitMQChannelSender object at 0x103179c90>> for "1:Basic.Ack"
2018-04-11 23:33:37,360 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 64
2018-04-11 23:33:37,360 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 65 messages, 12 have yet to be confirmed, 53 were acked and 0 were nacked
2018-04-11 23:33:37,361 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 220 - DEBUG - Processing 1:Basic.Ack
2018-04-11 23:33:37,361 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 234 - DEBUG - Calling <bound method RabbitMQChannelSender.on_delivery_confirmation of <agent.handler.channel.rabbitmq.RabbitMQChannelSender object at 0x103179c90>> for "1:Basic.Ack"
2018-04-11 23:33:37,361 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 148 - INFO - Received ack for delivery tag: 65
2018-04-11 23:33:37,361 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 158 - INFO - Published 65 messages, 11 have yet to be confirmed, 54 were acked and 0 were nacked
2018-04-11 23:33:37,490 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-11 23:33:37,491 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 311 - DEBUG - add_timeout: added timeout 7499915758516998160; deadline=1 at 1523460818.49
2018-04-11 23:33:38,189 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-11 23:33:38,190 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 311 - DEBUG - add_timeout: added timeout -3275537958151406425; deadline=1 at 1523460819.19
2018-04-11 23:33:38,496 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-11 23:33:38,497 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 311 - DEBUG - add_timeout: added timeout -4880188214039714137; deadline=1 at 1523460819.5
2018-04-11 23:33:39,191 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-11 23:33:39,191 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 311 - DEBUG - add_timeout: added timeout 7191954076363872102; deadline=1 at 1523460820.19
2018-04-11 23:33:39,499 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 166 - INFO - Scheduling next message for 1.0 seconds
2018-04-11 23:33:39,499 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 311 - DEBUG - add_timeout: added timeout -6928836100462463130; deadline=1 at 1523460820.5
^CChannel process(70978) got GracefulExitException.
Engine process(70976) got GracefulExitException.
Main process(70974) got GracefulExitException.
2018-04-11 23:33:40,145 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 183 - INFO - Stopping
2018-04-11 23:33:40,146 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 174 - INFO - Closing the channel
2018-04-11 23:33:40,146 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 529 - INFO - Closing channel (0): 'Normal shutdown' on <Channel number=1 OPEN conn=<SelectConnection OPEN socket=('192.168.43.170', 59988)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.cloud.com port=5672 virtual_host=/event_engine ssl=False>>>
2018-04-11 23:33:40,147 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 1300 - DEBUG - Entering blocking state on frame <Channel.Close(['class_id=0', 'method_id=0', 'reply_code=0', 'reply_text=Normal shutdown'])>; acceptable_replies=[<class 'pika.spec.CloseOk'>]
2018-04-11 23:33:40,147 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 1307 - DEBUG - Adding on_synchronous_complete callback
2018-04-11 23:33:40,147 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 164 - DEBUG - Added: {'callback': <bound method Channel._on_synchronous_complete of <Channel number=1 CLOSING conn=<SelectConnection OPEN socket=('192.168.43.170', 59988)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.cloud.com port=5672 virtual_host=/event_engine ssl=False>>>>, 'only': None, 'one_shot': True, 'arguments': None, 'calls': 1}
2018-04-11 23:33:40,148 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 1312 - DEBUG - Adding passed-in callback
2018-04-11 23:33:40,148 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 164 - DEBUG - Added: {'callback': <bound method Channel._on_closeok of <Channel number=1 CLOSING conn=<SelectConnection OPEN socket=('192.168.43.170', 59988)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.cloud.com port=5672 virtual_host=/event_engine ssl=False>>>>, 'only': None, 'one_shot': True, 'arguments': None, 'calls': 1}
2018-04-11 23:33:40,148 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 191 - INFO - Closing connection
2018-04-11 23:33:40,149 - pika.connection - /Library/Python/2.7/site-packages/pika/connection.py - 1147 - INFO - Closing connection (200): Normal shutdown
2018-04-11 23:33:40,149 - pika.connection - /Library/Python/2.7/site-packages/pika/connection.py - 1159 - INFO - Connection.close is waiting for 1 channels to close: <SelectConnection CLOSING socket=('192.168.43.170', 59988)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.cloud.com port=5672 virtual_host=/event_engine ssl=False>>
2018-04-11 23:33:40,150 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 523 - DEBUG - Stopping IOLoop
2018-04-11 23:33:40,150 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 502 - DEBUG - Cleaning up IOLoop
2018-04-11 23:33:40,150 - agent.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/sender.py - 188 - INFO - Stopped
2018-04-11 23:33:40,151 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 162 - INFO - Stopping
2018-04-11 23:33:40,151 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 146 - INFO - Sending a Basic.Cancel RPC command to RabbitMQ
2018-04-11 23:33:40,151 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 247 - DEBUG - Cancelling consumer: ctag1.dba16184f0a04f32a478e52c20f545a1 (nowait=False)
2018-04-11 23:33:40,151 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 164 - DEBUG - Added: {'callback': <bound method RabbitMQChannelReceiver.on_cancelok of <agent.handler.channel.rabbitmq.RabbitMQChannelReceiver object at 0x103179fd0>>, 'only': None, 'one_shot': True, 'arguments': None, 'calls': 1}
2018-04-11 23:33:40,152 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 1300 - DEBUG - Entering blocking state on frame <Basic.Cancel(['consumer_tag=ctag1.dba16184f0a04f32a478e52c20f545a1', 'nowait=False'])>; acceptable_replies=[(<class 'pika.spec.CancelOk'>, {'consumer_tag': 'ctag1.dba16184f0a04f32a478e52c20f545a1'})]
2018-04-11 23:33:40,152 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 1307 - DEBUG - Adding on_synchronous_complete callback
2018-04-11 23:33:40,152 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 164 - DEBUG - Added: {'callback': <bound method Channel._on_synchronous_complete of <Channel number=1 OPEN conn=<SelectConnection OPEN socket=('192.168.43.170', 59989)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.cloud.com port=5672 virtual_host=/event_engine ssl=False>>>>, 'only': None, 'one_shot': True, 'arguments': {'consumer_tag': 'ctag1.dba16184f0a04f32a478e52c20f545a1'}, 'calls': 1}
2018-04-11 23:33:40,152 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 1312 - DEBUG - Adding passed-in callback
2018-04-11 23:33:40,152 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 164 - DEBUG - Added: {'callback': <bound method Channel._on_cancelok of <Channel number=1 OPEN conn=<SelectConnection OPEN socket=('192.168.43.170', 59989)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.cloud.com port=5672 virtual_host=/event_engine ssl=False>>>>, 'only': None, 'one_shot': True, 'arguments': {'consumer_tag': 'ctag1.dba16184f0a04f32a478e52c20f545a1'}, 'calls': 1}
2018-04-11 23:33:40,153 - pika.adapters.select_connection - /Library/Python/2.7/site-packages/pika/adapters/select_connection.py - 523 - DEBUG - Stopping IOLoop
2018-04-11 23:33:40,153 - agent.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_agent/agent/util/amqp/receiver.py - 166 - INFO - Stopped
Monitor process(70977) got GracefulExitException.
```