import subprocess

# 调用Shell脚本
try:
    result = subprocess.run(['DJI_V2_RT_train.sh'], check=True, text=True, capture_output=True)
    print("脚本运行完毕，输出如下：")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"脚本运行失败，错误如下：{e.stderr}")