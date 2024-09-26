import psutil

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')

memory_total_mb = memory_info.total / (1024 * 1024)
memory_used_mb = memory_info.used / (1024 * 1024)
disk_total_gb = disk_usage.total / (1024 * 1024 * 1024)
disk_used_gb = disk_usage.used / (1024 * 1024 * 1024)

print(cpu_usage, memory_total_mb, memory_used_mb, disk_total_gb, disk_used_gb)