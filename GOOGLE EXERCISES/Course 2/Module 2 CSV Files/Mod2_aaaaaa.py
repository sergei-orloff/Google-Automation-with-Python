import shutil
du = shutil.disk_usage("/")
print(du)
percentage = du.free/du.total*100
print(percentage)
# ==============================
import psutil
cpuPerc = psutil.cpu_percent(0.1)
print(cpuPerc)
