import psutil
import os
import time

# Define thresholds for alerting
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"WARNING: High CPU usage detected! {cpu_usage}%")
    else:
        print(f"CPU usage is normal: {cpu_usage}%")
        
def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"WARNING: High memory usage detected! {memory_usage}%")
    else:
        print(f"Memory usage is normal: {memory_usage}%")
        
def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        print(f"WARNING: High disk usage detected! {disk_usage}%")
    else:
        print(f"Disk usage is normal: {disk_usage}%")

def check_running_processes():
    processes = len(psutil.pids())
    print(f"Number of running processes: {processes}")
    
def monitor_system_health():
    print("System Health Check:")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    
if __name__ == "__main__":
    while True:
        monitor_system_health()
        time.sleep(60)  # Check every 60 seconds
