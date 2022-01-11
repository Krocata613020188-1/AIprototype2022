import subprocess #สำหรับ รัน terminal command

if __name__=="__main__":
    subprocess.run(["ls","-l"])
    for i in [2,5,6,8]:
     subprocess.run(["python",".\python_script_101.py", "9", "--x", f'{i}', "--yval", "2"])