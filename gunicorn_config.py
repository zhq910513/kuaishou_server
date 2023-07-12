workers = 4
# 监听内网端口5000【按需要更改】
bind = '0.0.0.0:5001'
# 设置守护进程【关闭连接时，程序仍在运行】
daemon = True

# 工作模式协程
# worker_class = 'gevent'
worker_class = "sync"
# worker_class = "egg:meinheld#gunicorn_worker"  #

# 设置最大并发量
worker_connections = 1200  # 单个进程的最大连接数

# 设置超时时间120s，默认为30s。按自己的需求进行设置
timeout = 120
# 设置访问日志和错误信息日志路径
accesslog = './logs/acess.log'
errorlog = './logs/error.log'

# forwarded_allow_ips = '*' # 允许哪些ip地址来访问
