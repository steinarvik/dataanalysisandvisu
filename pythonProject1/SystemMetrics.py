import psutil
from datetime import datetime
import pandas
import os

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')

system_metrics = {
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'cpu_usage': cpu_usage,
    'memory_total_mb': memory_info.total / (1024 * 1024),
    'memory_used_mb': memory_info.used / (1024 * 1024),
    'disk_total_gb': disk_info.total /  (1024 * 1024 * 1024),
    'disk_used_gb': disk_info.used /  (1024 * 1024 * 1024)
    }
filepath = 'system_metrics.csv'

print(system_metrics)
df = pandas.DataFrame(system_metrics, index=[0])

if os.path.exists(filepath):
    df_existing = pandas.read_csv(filepath)
    df_existing = pandas.concat([df_existing, df])
    df_existing.to_csv(filepath, header=True, index=False)
else:
    df.to_csv(filepath, header=True, index=False)