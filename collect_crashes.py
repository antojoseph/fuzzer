from adb_android import adb_android

def pull_log_from_device():
    adb_android.pull("/data/local/tmp/logcat.txt",'.')

def analyze():
    pass