# Counter

使用FastAPI + Sqlite

## API

![GET](https://img.shields.io/badge//get-GET-dark_green)  
获取计数器

![POST](https://img.shields.io/badge//add-POST-yellow)  
计数器+1

![POST](https://img.shields.io/badge//clear-POST-yellow)  
计数器清零

## 使用

安装依赖
```bash
# 如果你使用的是Windows系统
pip install -r requirements.txt
# 如果你使用的是macOS系统
pip3 install -r requirements.txt
# 如果你使用的是Linux系统
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

使用uvicorn运行
```bash
uvicorn app:app --host 0.0.0.0 --port 8080 --log-level critical
```

## 使用Docker

1. 复制文件至服务器
2. 使用命令生成镜像：
   ```bash
   sudo docker build -t counter <项目位置>
   ```
3. 使用命令生成容器
   ```bash
   sudo docker run -d \
   --restart always \
   -p <主机端口>:8000 \
   -v <主机数据库路径>:/app/db \
   --name counter counter
   ```