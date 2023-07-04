import subprocess

print(subprocess.getoutput("date -u"))
print(subprocess.check_output(["date", "-u"]).decode("utf-8"), end="")
print(subprocess.getstatusoutput("date"))
print(subprocess.call("date", shell=True))
