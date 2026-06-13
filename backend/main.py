from fastapi import FastAPI
import psutil
import subprocess

app = FastAPI()

@app.get("/stats/cpu")
def cpu():
    return {"cpu_percent": psutil.cpu_percent(interval=1)}

@app.get("/stats/memory")
def memory():
    mem = psutil.virtual_memory()
    return {
        "total": (mem.total/(1024*1024*1024)),
        "used": (mem.used/(1024*1024*1024)),
        "percent": mem.percent
    }

@app.get("/stats/disk")
def disk():
    d = psutil.disk_usage('/')
    return {
        "total": (d.total/(1024*1024*1024)),
        "used": (d.used/(1024*1024*1024)),
        "percent": d.percent
    }

@app.get("/stats/temperature")
def temperature(): # vcgencmd is Raspberrypi specific so it would crash on windows or wsl 
    temp = subprocess.check_output(
        "vcgencmd measure_temp", shell=True
    ).decode().strip()
    return {"temperature": temp}

@app.get("/stats/battery")
def battery_info():
    battery = psutil.sensors_battery()
    return {"Battery_percentage": battery[0],
            "charger_plugged": battery[2]}

@app.get("/stats/network")
def addrs():
    network_address = psutil.net_if_addrs()
    ipv4 = network_address["eth0"][0][1]
    ipv6 = network_address["eth0"][1][1]
    return {"IPV4": ipv4, "IPV6":ipv6}

@app.get("/stats")
def all_info():
    battery = battery_info()
    network= addrs()
    try:
        temp = temperature()
    except:
        temp = "unavaliable"
    cpu_percentage = cpu()
    mem = memory()
    disk_usage = disk()
    return {"status":{
        "Battery_info": battery,
        "Network": network,
        "temp": temp,
        "cpu_per" : cpu_percentage,
        "memory": mem,
        "Disk Usage": disk_usage
    }}

@app.get("/health")
def health():
    return {"status": "ok"} 