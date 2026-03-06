import time
import psutil

def monitor_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f'Загрузка CPU: {cpu_percent:.1f}%')

def monitor_memory():
    memory = psutil.virtual_memory()
    used_memory_mb = memory.used / (1024 * 1024)
    total_memory_mb = memory.total / (1024 * 1024)
    percent_used = memory.percent
    
    print(f'Использовано ОЗУ: {used_memory_mb:.2f} MB ({percent_used:.1f}%)')
    print(f'Всего доступно: {total_memory_mb:.2f} MB')

def monitor_disk():
    disk_usage = psutil.disk_usage('/')
    used_space_gb = disk_usage.used / (1024 * 1024 * 1024)
    total_space_gb = disk_usage.total / (1024 * 1024 * 1024)
    percent_used = disk_usage.percent
    
    print(f'Использованное пространство на диске: {used_space_gb:.2f} GB ({percent_used:.1f}%)')
    print(f'Общий объем диска: {total_space_gb:.2f} GB')

while True:
    print("--- Текущие показатели ---")
    monitor_cpu()
    monitor_memory()
    monitor_disk()
        
    time.sleep(5)
