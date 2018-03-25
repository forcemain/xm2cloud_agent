### Debug:

```
2018-03-25 19:03:41,334 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 107 - ERROR - Call plugin agent.metrics.host._load [Errno 2] No such file or directory: '/proc/loadavg'
2018-03-25 19:03:41,335 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 107 - ERROR - Call plugin agent.metrics.host._load [Errno 2] No such file or directory: '/proc/loadavg'
<agent.metrics.host._mem: 
{
    "mem_swapused_percentage": {
        "name": "mem.swapused.percentage", 
        "value": 46.9
    }, 
    "mem_swapused": {
        "name": "mem.swapused", 
        "value": 1511784448
    }, 
    "mem_memtotal": {
        "name": "mem.memtotal", 
        "value": 8589934592
    }, 
    "mem_swaptotal": {
        "name": "mem.swaptotal", 
        "value": 3221225472
    }, 
    "mem_memfree": {
        "name": "mem.memfree", 
        "value": 82575360
    }, 
    "mem_swapfree": {
        "name": "mem.swapfree", 
        "value": 1709441024
    }, 
    "mem_memused": {
        "name": "mem.memused", 
        "value": 6297075712
    }, 
    "mem_memused_percentage": {
        "name": "mem.memused.percentage", 
        "value": 81.5
    }
}>
2018-03-25 19:03:41,337 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 107 - ERROR - Call plugin agent.metrics.host._cpu [Errno 2] No such file or directory: '/proc/stat'
<agent.metrics.host._df: 
{
    "df_bytes_used_percentage": {
        "name": "df.bytes.used.percentage/device=disk1s1,mount=/", 
        "value": 23.0
    }, 
    "df_bytes_free": {
        "name": "df.bytes.free/device=disk1s1,mount=/", 
        "value": 189134630912
    }, 
    "df_bytes_total": {
        "name": "df.bytes.used/device=disk1s1,mount=/", 
        "value": 56577372160
    }
}>
<agent.metrics.host._df: 
{
    "df_bytes_used_percentage": {
        "name": "df.bytes.used.percentage/device=disk1s4,mount=/private/var/vm", 
        "value": 2.2
    }, 
    "df_bytes_free": {
        "name": "df.bytes.free/device=disk1s4,mount=/private/var/vm", 
        "value": 189134630912
    }, 
    "df_bytes_total": {
        "name": "df.bytes.used/device=disk1s4,mount=/private/var/vm", 
        "value": 4294987776
    }
}>
2018-03-25 19:03:41,539 - agent.core.monitor - /Users/manmanli/xm-gits/xm2cloud_agent/agent/core/monitor.py - 107 - ERROR - Call plugin agent.metrics.user._redis._init Error 61 connecting to 127.0.0.1:6378. Connection refused.
^CMain process(91168) got GracefulExitException.
Monitor process(91169) got GracefulExitException.
```
