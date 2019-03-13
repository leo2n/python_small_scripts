"""
backup small script, from dir1 to dir2.zip(dir2 is time when backup)
"""
import os
import time

# 预备备份的目录, 和备份文件准备存储的目录
source = ['/home/leo/sexQ']
target_dir = '/home/leo/backup'

# 备份文件准备存储的目录的路径完整名称
target = target_dir + os.sep + time.strftime("%Y%m%d%H%M%S")+".zip"

# 如果存放备份文件的目录名不存在, 那就创建它
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 准备在shell里面执行的系统命令
zip_command = "zip -r {0} {1}".format(target, ''.join(source))

print("zip command is:", zip_command)
print("Running...")
if os.system(zip_command) == 0:
    print("Successfully backup :)")
else:
    print("backup FAILED")
