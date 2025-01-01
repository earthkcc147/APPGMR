import subprocess
import platform

def get_android_device_info():
    """ดึงข้อมูลระบบและฮาร์ดแวร์ของอุปกรณ์ Android"""
    try:
        commands = {
            "รุ่นอุปกรณ์": "getprop ro.product.model",
            "ยี่ห้อ": "getprop ro.product.brand",
            "เวอร์ชัน Android": "getprop ro.build.version.release",
            "ชื่ออุปกรณ์": "getprop ro.product.device",
            "เวอร์ชัน Kernel": "uname -r",
            "ฮาร์ดแวร์": "getprop ro.hardware",
            "Bootloader": "getprop ro.bootloader",
            "ความละเอียดหน้าจอ": "wm size",
            "ความหนาแน่นหน้าจอ": "wm density",
            "ระดับแบตเตอรี่": "dumpsys battery | grep level",
            "สถานะแบตเตอรี่": "dumpsys battery | grep status",
            "อุณหภูมิแบตเตอรี่": "dumpsys battery | grep temperature",
            "แรงดันไฟฟ้าแบตเตอรี่": "dumpsys battery | grep voltage",
            "ข้อมูล CPU": "cat /proc/cpuinfo | grep Hardware",
            "ความเร็วสูงสุดของ CPU": "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq",
            "ความเร็วต่ำสุดของ CPU": "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq",
            "จำนวนคอร์ของ CPU": "grep -c ^processor /proc/cpuinfo",
            "RAM ทั้งหมด": "grep MemTotal /proc/meminfo",
            "RAM ที่เหลืออยู่": "grep MemAvailable /proc/meminfo",
            "พื้นที่เก็บข้อมูล": "df -h /data | grep /data",
            "สถานะ Wi-Fi": "dumpsys wifi | grep 'Wi-Fi is'",
            "ที่อยู่ IP": "ip addr show wlan0 | grep 'inet '",
            "ที่อยู่ MAC": "cat /sys/class/net/wlan0/address",
            "IMEI (ช่อง SIM 1)": "service call iphonesubinfo 1 | cut -c 52-66 | tr -d '.[:space:]'",
            "IMEI (ช่อง SIM 2)": "service call iphonesubinfo 2 | cut -c 52-66 | tr -d '.[:space:]'",
            "ผู้ให้บริการ SIM": "getprop gsm.operator.alpha",
            "รหัสเครือข่าย": "getprop gsm.operator.numeric",
            "สถานะเครือข่ายมือถือ": "dumpsys connectivity | grep 'Mobile'",
            "สถานะ GPS": "dumpsys location | grep 'mStarted' | tail -n 1",
            "แอปที่ติดตั้ง": "pm list packages -3",
            "แอปที่กำลังทำงาน": "ps -A | grep u0_a",
            "เวลาที่ใช้งานเครื่อง": "cat /proc/uptime | awk '{print $1}'",
            "สถานะความร้อน": "dumpsys thermalservice | grep status",
            "ที่อยู่ MAC ของ Bluetooth": "settings get secure bluetooth_address",
            "ประเภทเครือข่ายที่ใช้งาน": "dumpsys connectivity | grep 'Active network'",
            "ความแรงสัญญาณ Wi-Fi": "dumpsys wifi | grep 'mWifiInfo'",
            "ความสว่างหน้าจอ": "settings get system screen_brightness",
            "สถานะ USB Debugging": "getprop persist.sys.usb.config",
            "อุปกรณ์เสียงออก": "dumpsys audio | grep 'Output device'",
            "ภาษาปัจจุบัน": "getprop persist.sys.language",
            "เขตเวลา": "getprop persist.sys.timezone",
            "เวลาเปิดเครื่องล่าสุด": "uptime -s",
            "จำนวนกระบวนการที่ทำงาน": "ps | wc -l",
            "ความจุแบตเตอรี่": "dumpsys battery | grep capacity",
            "สถานะ SIM": "dumpsys telephony.registry | grep SIM",
            "รายละเอียดการเชื่อมต่อเครือข่าย": "dumpsys connectivity | grep -A 10 'NetworkAgentInfo'",
            "ข้อมูล Bluetooth": "dumpsys bluetooth_manager | grep 'Bluetooth'",
            "ความเร็วเน็ตไร้สาย": "cat /sys/class/net/wlan0/speed",
            "สถานะการเชื่อมต่อ USB": "lsusb",
            "ประวัติการใช้งานแอป": "logcat -d -s ActivityManager",
        }
        info = {}
        for key, cmd in commands.items():
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            info[key] = result.stdout.strip()
        return info
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return {}

def get_ios_device_info():
    """ดึงข้อมูลระบบของอุปกรณ์ iOS"""
    try:
        commands = {
            "ชื่ออุปกรณ์": "sysctl -n hw.model",
            "เวอร์ชัน iOS": "sw_vers -productVersion",
            "ข้อมูล CPU": "sysctl -n machdep.cpu.brand_string",
            "จำนวนคอร์ของ CPU": "sysctl -n hw.ncpu",
            "RAM ทั้งหมด": "sysctl -n hw.memsize",
            "พื้นที่เก็บข้อมูล": "df -h / | grep /",
            "สถานะ Wi-Fi": "ifconfig en0 | grep status",
            "ที่อยู่ IP": "ifconfig en0 | grep inet",
            "ที่อยู่ MAC": "ifconfig en0 | grep ether",
            "เวลาที่ใช้งานเครื่อง": "sysctl -n kern.boottime",
            "จำนวนกระบวนการที่ทำงาน": "ps aux | wc -l",
            "สถานะ Bluetooth": "system_profiler SPBluetoothDataType",
            "ข้อมูลแบตเตอรี่": "system_profiler SPPowerDataType",
            "ประเภทเครือข่าย": "networksetup -getnetworkserviceenabled Wi-Fi",
            "อุณหภูมิอุปกรณ์": "sysctl -n dev.cpu.0.temperature",
            "ข้อมูลพื้นที่เก็บข้อมูล": "df -h / | grep /",
            "รายละเอียดการเชื่อมต่อเครือข่าย": "ifconfig en0",
        }
        info = {}
        for key, cmd in commands.items():
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            info[key] = result.stdout.strip()
        return info
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return {}

def get_pc_info():
    """ดึงข้อมูลระบบของ PC"""
    try:
        commands = {
            "ชื่อเครื่อง": "hostname",
            "ระบบปฏิบัติการ": "uname -o",
            "เวอร์ชัน OS": "uname -r",
            "CPU": "lscpu | grep 'Model name'",
            "จำนวนคอร์ของ CPU": "nproc",
            "RAM": "free -h | grep Mem",
            "พื้นที่เก็บข้อมูล": "df -h / | grep /",
            "ที่อยู่ IP": "hostname -I",
            "จำนวนกระบวนการที่ทำงาน": "ps aux | wc -l",
            "รายละเอียดการเชื่อมต่อเครือข่าย": "ifconfig | grep inet",
            "สถานะ Wi-Fi": "nmcli device status",
            "ข้อมูลการเชื่อมต่อ Ethernet": "ethtool eth0",
            "ประวัติการใช้งานแอป": "ps aux",
            "ความเร็วของเน็ตเวิร์ก": "ifstat",
            "การใช้ CPU": "top -n 1 | grep Cpu",
            "การใช้พื้นที่ดิสก์": "df -h",
            "รายละเอียด USB": "lsusb",
        }
        info = {}
        for key, cmd in commands.items():
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            info[key] = result.stdout.strip()
        return info
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return {}

def get_macbook_info():
    """ดึงข้อมูลระบบของ MacBook"""
    try:
        commands = {
            "ชื่อเครื่อง": "hostname",
            "ระบบปฏิบัติการ": "sw_vers -productName",
            "เวอร์ชัน OS": "sw_vers -productVersion",
            "CPU": "sysctl -n machdep.cpu.brand_string",
            "จำนวนคอร์ของ CPU": "sysctl -n hw.ncpu",
            "RAM": "sysctl -n hw.memsize",
            "พื้นที่เก็บข้อมูล": "df -h / | grep /",
            "ที่อยู่ IP": "ifconfig en0 | grep inet",
            "จำนวนกระบวนการที่ทำงาน": "ps aux | wc -l",
            "สถานะ Bluetooth": "system_profiler SPBluetoothDataType",
            "ข้อมูลแบตเตอรี่": "system_profiler SPPowerDataType",
            "รายละเอียดการเชื่อมต่อเครือข่าย": "ifconfig en0",
        }
        info = {}
        for key, cmd in commands.items():
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            info[key] = result.stdout.strip()
        return info
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return {}

def get_raspberry_pi_info():
    """ดึงข้อมูลระบบของ Raspberry Pi"""
    try:
        commands = {
            "ชื่อเครื่อง": "hostname",
            "ระบบปฏิบัติการ": "uname -o",
            "เวอร์ชัน OS": "uname -r",
            "CPU": "cat /proc/cpuinfo | grep 'model name'",
            "จำนวนคอร์ของ CPU": "nproc",
            "RAM": "free -h | grep Mem",
            "พื้นที่เก็บข้อมูล": "df -h / | grep /",
            "ที่อยู่ IP": "hostname -I",
            "จำนวนกระบวนการที่ทำงาน": "ps aux | wc -l",
            "รายละเอียดการเชื่อมต่อเครือข่าย": "ifconfig | grep inet",
            "สถานะ Wi-Fi": "iw dev wlan0 link",
            "การใช้งาน CPU": "top -n 1 | grep Cpu",
            "การใช้พื้นที่ดิสก์": "df -h",
            "การใช้พื้นที่ /tmp": "df -h /tmp",
            "ข้อมูลการเชื่อมต่อ GPIO": "gpio readall",
            "อุณหภูมิของ CPU": "cat /sys/class/thermal/thermal_zone0/temp",
            "สถานะการทำงานของอุปกรณ์": "vcgencmd get_mem arm && vcgencmd get_mem gpu",
            "แรงดันไฟฟ้า 3.3V": "vcgencmd measure_volts 3.3v",
            "แรงดันไฟฟ้า 5V": "vcgencmd measure_volts 5v",
        }
        info = {}
        for key, cmd in commands.items():
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            info[key] = result.stdout.strip()
        return info
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return {}

def get_device_info():
    """ดึงข้อมูลระบบของอุปกรณ์ต่าง ๆ"""
    device = platform.system()

    if device == "Linux":
        # สำหรับ Android หรือ Raspberry Pi
        return get_android_device_info() if platform.system().find('Android') != -1 else get_raspberry_pi_info()
    elif device == "Darwin":
        # Mac OS (Macbook)
        return get_macbook_info()
    elif device == "Windows":
        # PC (Windows)
        return get_pc_info()
    elif device == "iOS":
        # iOS
        return get_ios_device_info()
    else:
        print("ไม่รองรับอุปกรณ์นี้")
        return {}

def main():
    print("ข้อมูลอุปกรณ์ของคุณ:")
    info = get_device_info()
    if info:
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("ไม่สามารถดึงข้อมูลได้")

if __name__ == "__main__":
    main()