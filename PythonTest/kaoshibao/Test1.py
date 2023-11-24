import json
import re

jsondata = {
    "code": "200",
    "data": {
        "rows": [
            {
                "id": "843857233",
                "uid": "5351165",
                "paperid": "9151365",
                "question": "yum -y install <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span>-server <span style=\"color:#ff664b;\">MySQL</span>-python的作用是？",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"<p>&nbsp;\\u521b\\u5efaMySQL\\u6570\\u636e\\u5e93 <\\/p>\"},{\"Key\":\"B\",\"Value\":\"<p>\\u5b89\\u88c5IaaS\\u73af\\u5883 <\\/p>\"},{\"Key\":\"C\",\"Value\":\"<p>\\u5b89\\u88c5MySQL\\u6570\\u636e\\u5e93 <\\/p>\"},{\"Key\":\"D\",\"Value\":\"<p>\\u521b\\u5efa\\u8868 <\\/p>\"}]",
                "answer": "C",
                "analysis": "",
                "updated_at": "2022-12-21 13:34:38",
                "question.raw": "yum -y install mysql mysql-server MySQL-python的作用是？",
                "paper": {
                    "uid": "5351165",
                    "name": "云计算",
                    "question_total": "201",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1149322765",
                "uid": "3805254",
                "paperid": "10595361",
                "question": "对与以下代码说法不正确的是（）\njdbc.<span style=\"color:#ff664b;\">mysql</span>.driver = com.<span style=\"color:#ff664b;\">mysql</span>.jdbc.Driver\njdbc.<span style=\"color:#ff664b;\">mysql</span>.url = jdbc:<span style=\"color:#ff664b;\">mysql</span>://localhost:3306",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"jdbc.mysql.user和jdbc.mysql.password\"},{\"Key\":\"B\",\"Value\":\"jdbc:mysql:\\/\\/localhost:3306\\/的后面接的是项目的发布路径\"},{\"Key\":\"C\",\"Value\":\"这是一个properties文件里面关于数据库的连接的配置\"},{\"Key\":\"D\",\"Value\":\"jdbc.mysql.drive是数据库驱动\"}]",
                "answer": "B",
                "analysis": "",
                "updated_at": "2023-06-08 16:32:57",
                "question.raw": "对与以下代码说法不正确的是（）\njdbc.mysql.driver = com.mysql.jdbc.Driver\njdbc.mysql.url = jdbc:mysql://localhost:3306/\njdbc.mysql.user = root\njdbc.mysql.password = 1234",
                "paper": {
                    "uid": "3805254",
                    "name": "aaa",
                    "question_total": "120",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1149322765",
                "uid": "3805254",
                "paperid": "10595361",
                "question": "对与以下代码说法不正确的是（）\njdbc.<span style=\"color:#ff664b;\">mysql</span>.driver = com.<span style=\"color:#ff664b;\">mysql</span>.jdbc.Driver\njdbc.<span style=\"color:#ff664b;\">mysql</span>.url = jdbc:<span style=\"color:#ff664b;\">mysql</span>://localhost:3306",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"jdbc.mysql.user和jdbc.mysql.password\"},{\"Key\":\"B\",\"Value\":\"jdbc:mysql:\\/\\/localhost:3306\\/的后面接的是项目的发布路径\"},{\"Key\":\"C\",\"Value\":\"这是一个properties文件里面关于数据库的连接的配置\"},{\"Key\":\"D\",\"Value\":\"jdbc.mysql.drive是数据库驱动\"}]",
                "answer": "B",
                "analysis": "",
                "updated_at": "2023-06-08 16:32:57",
                "question.raw": "对与以下代码说法不正确的是（）\njdbc.<span style=\"color:#ff664b;\">mysql</span>.driver = com.<span style=\"color:#ff664b;\">mysql</span>.jdbc.Driver\njdbc.<span style=\"color:#ff664b;\">mysql</span>.url = jdbc:<span style=\"color:#ff664b;\">mysql</span>://localhost:3306",
                "paper": {
                    "uid": "3805254",
                    "name": "aaa",
                    "question_total": "120",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "562849935",
                "uid": "4860309",
                "paperid": "7194026",
                "question": "<span style=\"color:#ff664b;\">mysql</span>模块通过（）方法创建<span style=\"color:#ff664b;\">MySQL</span>连接。",
                "qtype": "4",
                "parentid": "0",
                "options": "[]",
                "answer": "createConnection()",
                "analysis": "",
                "updated_at": "2022-06-28 23:47:15",
                "question.raw": "mysql模块通过（）方法创建MySQL连接。",
                "paper": {
                    "uid": "4860309",
                    "name": "node",
                    "question_total": "333",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1228316612",
                "uid": "4132892",
                "paperid": "11041034",
                "question": "创建并启动<span style=\"color:#ff664b;\">MySQL</span>容器docker   (          )   -d --name <span style=\"color:#ff664b;\">mysql</span>5.7-3306 -p 3306:3306 -e <span style=\"color:#ff664b;\">MYSQL</span>_ROOT_PASSWORD='123456",
                "qtype": "4",
                "parentid": "0",
                "options": "[]",
                "answer": "run",
                "analysis": "",
                "updated_at": "2023-07-01 11:21:10",
                "question.raw": "创建并启动MySQL容器docker   (          )   -d --name mysql5.7-3306 -p 3306:3306 -e MYSQL_ROOT_PASSWORD='123456' mysql:5.7",
                "paper": {
                    "uid": "4132892",
                    "name": "KVM虚拟机",
                    "question_total": "82",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1176112897",
                "uid": "11005909",
                "paperid": "10698761",
                "question": "如果<span style=\"color:#ff664b;\">MySQL</span>服务名为<span style=\"color:#ff664b;\">MySQL</span>，则在Windows的命令窗口中，启动<span style=\"color:#ff664b;\">MySQL</span>服务的指令是（ ），关闭<span style=\"color:#ff664b;\">MySQL</span>服务的指令是（ ）。",
                "qtype": "4",
                "parentid": "0",
                "options": "[]",
                "answer": "net start mysql|net stop mysql",
                "analysis": "",
                "updated_at": "2023-06-16 09:20:04",
                "question.raw": "如果MySQL服务名为MySQL，则在Windows的命令窗口中，启动MySQL服务的指令是（ ），关闭MySQL服务的指令是（ ）。",
                "paper": {
                    "uid": "11005909",
                    "name": "22大一下计算机",
                    "question_total": "338",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "319512346",
                "uid": "2868747",
                "paperid": "4182084",
                "question": "<span style=\"color:#ff664b;\">MySQL</span>服务名称为“<span style=\"color:#ff664b;\">MySQL</span>80”，停止<span style=\"color:#ff664b;\">MySQL</span>80服务的指令是（）",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"<p>mysql stop MySQL80&nbsp;<\\/p>\"},{\"Key\":\"B\",\"Value\":\"<p>stop MySQL80&nbsp;<\\/p>\"},{\"Key\":\"C\",\"Value\":\"<p>quit MySQL80&nbsp;<\\/p>\"},{\"Key\":\"D\",\"Value\":\"<p>net stop&nbsp;MySQL80&nbsp;<\\/p>\"}]",
                "answer": "D",
                "analysis": "",
                "updated_at": "2021-12-21 16:19:47",
                "question.raw": "MySQL服务名称为“MySQL80”，停止MySQL80服务的指令是（）",
                "paper": {
                    "uid": "2868747",
                    "name": "mysql",
                    "question_total": "41",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "109616583",
                "uid": "843886",
                "paperid": "1314637",
                "question": "<span style=\"color:#ff664b;\">Mysql</span>集群告警，进入<span style=\"color:#ff664b;\">Mysql</span>后使用以下哪个命令检查<span style=\"color:#ff664b;\">Mysql</span>集群状态？",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"show status like 'wsrep_local_state_comment';\"},{\"Key\":\"B\",\"Value\":\"show status like 'wsrep_local_state_command';\"},{\"Key\":\"C\",\"Value\":\"show state like 'wsrep_local_status_comment';\"},{\"Key\":\"D\",\"Value\":\"show state like 'wsrep_local_status_command';\"}]",
                "answer": "A",
                "analysis": "",
                "updated_at": "2021-07-03 19:37:44",
                "question.raw": "Mysql集群告警，进入Mysql后使用以下哪个命令检查Mysql集群状态？",
                "paper": {
                    "uid": "843886",
                    "name": "会计从业资格",
                    "question_total": "745",
                    "price": "0",
                    "password": "1",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "319512351",
                "uid": "2868747",
                "paperid": "4182084",
                "question": "若<span style=\"color:#ff664b;\">MySQL</span>服务名称为“<span style=\"color:#ff664b;\">MySQL</span>80”，启动<span style=\"color:#ff664b;\">MySQL</span>数据库服务器的指令为net start <span style=\"color:#ff664b;\">MySQL</span>80（）",
                "qtype": "3",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"正确\"},{\"Key\":\"B\",\"Value\":\"错误\"}]",
                "answer": "A",
                "analysis": "",
                "updated_at": "2021-12-21 16:09:47",
                "question.raw": "若MySQL服务名称为“MySQL80”，启动MySQL数据库服务器的指令为net start MySQL80（）",
                "paper": {
                    "uid": "2868747",
                    "name": "mysql",
                    "question_total": "41",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "450668413",
                "uid": "3858572",
                "paperid": "5815706",
                "question": "<span style=\"color:#ff664b;\">MySQL</span>数据库文件默认存放路径是C:\\ProgramData\\<span style=\"color:#ff664b;\">MySQL</span>\\<span style=\"color:#ff664b;\">MySQL</span> Server 5.5\\（）",
                "qtype": "3",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"正确\"},{\"Key\":\"B\",\"Value\":\"错误\"}]",
                "answer": "A",
                "analysis": "",
                "updated_at": "2022-06-23 20:59:41",
                "question.raw": "MySQL数据库文件默认存放路径是C:\\ProgramData\\MySQL\\MySQL Server 5.5\\（）",
                "paper": {
                    "uid": "3858572",
                    "name": "计算机维修工3级理论",
                    "question_total": "125",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "487402099",
                "uid": "2281438",
                "paperid": "6280191",
                "question": "在<span style=\"color:#ff664b;\">MySQL</span>中，<span style=\"color:#ff664b;\">MySQL</span>安装完成后，默认管理<span style=\"color:#ff664b;\">MySQL</span>数据库用户是（     ）。",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"nobay\"},{\"Key\":\"B\",\"Value\":\"root\"},{\"Key\":\"C\",\"Value\":\"guest\"},{\"Key\":\"D\",\"Value\":\"ad\"},{\"Key\":\"H\",\"Value\":\"2\"}]",
                "answer": "B",
                "analysis": "概念理解",
                "updated_at": "2022-05-27 07:14:14",
                "question.raw": "在MySQL中，MySQL安装完成后，默认管理MySQL数据库用户是（     ）。",
                "paper": {
                    "uid": "2281438",
                    "name": "MySQL",
                    "question_total": "170",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1162102838",
                "uid": "2695595",
                "paperid": "10661385",
                "question": "<span style=\"color:#ff664b;\">MySQL</span>数据库图像化管理和开发工具，有<span style=\"color:#ff664b;\">MySQL</span> Workbench（ ）、（ ）、<span style=\"color:#ff664b;\">MySQL</span> Workbench,phpMyAdmin。",
                "qtype": "2",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"mysql\"},{\"Key\":\"B\",\"Value\":\"Navicat for MySQL\"},{\"Key\":\"C\",\"Value\":\"SQLyog\"},{\"Key\":\"D\",\"Value\":\"orecal\"}]",
                "answer": "BC",
                "analysis": "",
                "updated_at": "2023-06-12 16:38:45",
                "question.raw": "MySQL数据库图像化管理和开发工具，有MySQL Workbench（ ）、（ ）、MySQL Workbench,phpMyAdmin。",
                "paper": {
                    "uid": "2695595",
                    "name": "数据库",
                    "question_total": "96",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "109616584",
                "uid": "843886",
                "paperid": "1314637",
                "question": "<span style=\"color:#ff664b;\">Mysql</span>集群告警，进入<span style=\"color:#ff664b;\">Mysql</span>后使用以下哪个命令检查<span style=\"color:#ff664b;\">Mysql</span>集群当前节点数？",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"show status like 'wsrep_cluster_size';\"},{\"Key\":\"B\",\"Value\":\"show state like 'wsrep_cluster_size';\"},{\"Key\":\"C\",\"Value\":\"show status like 'wsrep_node_size';\"},{\"Key\":\"D\",\"Value\":\"show state like 'wsrep_node_size';\"}]",
                "answer": "A",
                "analysis": "",
                "updated_at": "2021-07-03 19:37:44",
                "question.raw": "Mysql集群告警，进入Mysql后使用以下哪个命令检查Mysql集群当前节点数？",
                "paper": {
                    "uid": "843886",
                    "name": "会计从业资格",
                    "question_total": "745",
                    "price": "0",
                    "password": "1",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1162102838",
                "uid": "2695595",
                "paperid": "10661385",
                "question": "<span style=\"color:#ff664b;\">MySQL</span>数据库图像化管理和开发工具，有<span style=\"color:#ff664b;\">MySQL</span> Workbench（ ）、（ ）、<span style=\"color:#ff664b;\">MySQL</span> Workbench,phpMyAdmin。",
                "qtype": "2",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"mysql\"},{\"Key\":\"B\",\"Value\":\"Navicat for MySQL\"},{\"Key\":\"C\",\"Value\":\"SQLyog\"},{\"Key\":\"D\",\"Value\":\"orecal\"}]",
                "answer": "BC",
                "analysis": "",
                "updated_at": "2023-06-12 16:38:45",
                "question.raw": "<span style=\"color:#ff664b;\">MySQL</span>数据库图像化管理和开发工具，有<span style=\"color:#ff664b;\">MySQL</span> Workbench（ ）、（ ）、<span style=\"color:#ff664b;\">MySQL</span> Workbench,phpMyAdmin。",
                "paper": {
                    "uid": "2695595",
                    "name": "数据库",
                    "question_total": "96",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1423237157",
                "uid": "10527419",
                "paperid": "11783184",
                "question": "在<span style=\"color:#ff664b;\">MySQL</span>中，<span style=\"color:#ff664b;\">MySQL</span>安装完成后，默认管理<span style=\"color:#ff664b;\">MySQL</span>数据库用户是（     ）。",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"nobay\"},{\"Key\":\"B\",\"Value\":\"root\"},{\"Key\":\"C\",\"Value\":\"guest\"},{\"Key\":\"D\",\"Value\":\"ad\"}]",
                "answer": "B",
                "analysis": "",
                "updated_at": "2023-09-12 21:46:10",
                "question.raw": "在MySQL中，MySQL安装完成后，默认管理MySQL数据库用户是（     ）。",
                "paper": {
                    "uid": "10527419",
                    "name": "补考",
                    "question_total": "170",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1528994563",
                "uid": "13982884",
                "paperid": "12208606",
                "question": "Linux 上安装的 <span style=\"color:#ff664b;\">MySQL</span> 配置如下： [mysqld] user=<span style=\"color:#ff664b;\">mysql</span> datadir=/data/<span style=\"color:#ff664b;\">mysql</span>/ 然后你以 root 身份修改了 datadir 的路径和所有者信息： shell",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"MySQL\"},{\"Key\":\"B\",\"Value\":\"mysqld\"},{\"Key\":\"C\",\"Value\":\"MySQL\"},{\"Key\":\"D\",\"Value\":\"MySQL\"}]",
                "answer": "D",
                "analysis": "",
                "updated_at": "2023-10-28 16:52:51",
                "question.raw": "Linux 上安装的 MySQL 配置如下： [mysqld] user=mysql datadir=/data/mysql/ 然后你以 root 身份修改了 datadir 的路径和所有者信息： shell&gt; cp –R /var/lib/mysql /data/mysql/ shell&gt; chown –R mysql /data/mysql 上述操作中修改 datadir 目录的所有者信息为”mysql”的目的是什么？",
                "paper": {
                    "uid": "13982884",
                    "name": "系统",
                    "question_total": "101",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "790849752",
                "uid": "5774336",
                "paperid": "8865637",
                "question": "Linux 上安装的 <span style=\"color:#ff664b;\">MySQL</span> 配置如下： \n[mysqld] \nuser=<span style=\"color:#ff664b;\">mysql</span> \ndatadir=/data/<span style=\"color:#ff664b;\">mysql</span>/ \n然后你以 root 身份修改了 datadir 的路径和所有者信息",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"MySQL\"},{\"Key\":\"B\",\"Value\":\"mysqld\"},{\"Key\":\"C\",\"Value\":\"MySQL\"},{\"Key\":\"D\",\"Value\":\"MySQL\"}]",
                "answer": "D",
                "analysis": "",
                "updated_at": "2022-11-18 13:58:13",
                "question.raw": "Linux 上安装的 MySQL 配置如下： \n[mysqld] \nuser=mysql \ndatadir=/data/mysql/ \n然后你以 root 身份修改了 datadir 的路径和所有者信息： \nshell&gt; cp –R /var/lib/mysql /data/mysql/ \nshell&gt; chown –R mysql /data/mysql \n上述操作中修改 datadir 目录的所有者信息为”mysql”的目的是什么？",
                "paper": {
                    "uid": "5774336",
                    "name": "易通",
                    "question_total": "100",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1529011386",
                "uid": "13983102",
                "paperid": "12208701",
                "question": "Linux 上安装的 <span style=\"color:#ff664b;\">MySQL</span> 配置如下： [mysqld] user=<span style=\"color:#ff664b;\">mysql</span> datadir=/data/<span style=\"color:#ff664b;\">mysql</span>/ 然后你以 root 身份修改了 datadir 的路径和所有者信息： shell",
                "qtype": "1",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"MySQL \\u9700\\u8981\\u4ee5 root \\u8eab\\u4efd\\u8fd0\\u884c\\uff0c\\u4f46\\u662f\\u6587\\u4ef6\\u4e0d\\u80fd\\u5c5e\\u4e8e root\"},{\"Key\":\"B\",\"Value\":\"mysqld \\u8fdb\\u7a0b\\u9700\\u8981 datadir \\u76ee\\u5f55\\u4e0b\\u7684\\u6240\\u6709\\u6743\\u9650\"},{\"Key\":\"C\",\"Value\":\"MySQL \\u4e0d\\u80fd\\u4ee5 root \\u8eab\\u4efd\\u8fd0\\u884c\"},{\"Key\":\"D\",\"Value\":\"MySQL \\u9700\\u8981\\u6b63\\u786e\\u7684\\u6240\\u6709\\u8005\\u6765\\u786e\\u4fdd\\u5b89\\u5168\"}]",
                "answer": "D",
                "analysis": "",
                "updated_at": "2023-10-28 17:02:27",
                "question.raw": "Linux 上安装的 MySQL 配置如下： [mysqld] user=mysql datadir=/data/mysql/ 然后你以 root 身份修改了 datadir 的路径和所有者信息： shell&gt; cp –R /var/lib/mysql /data/mysql/ shell&gt; chown –R mysql /data/mysql 上述操作中修改 datadir 目录的所有者信息为”mysql”的目的是什么？",
                "paper": {
                    "uid": "13983102",
                    "name": "2",
                    "question_total": "101",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1366298744",
                "uid": "5982773",
                "paperid": "11558101",
                "question": "- - ---- 1 <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span> 56 Aug 20 13:58 auto. cnf drwxr-xr-x 1 <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span> 4096 Aug 21 10:28 accounting",
                "qtype": "2",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"<p>Remove group read\\/write privileges from the private_ key. pem file <\\/p>\"},{\"Key\":\"B\",\"Value\":\"<p>Remove world read privileges from the server-cert.pem certificate file<\\/p>\"},{\"Key\":\"C\",\"Value\":\"<p>&nbsp;Change the group ownership of the mysql directory to the mysql user group<\\/p>\"},{\"Key\":\"D\",\"Value\":\"<p>Remove world read privileges from the public_ key.pem file <\\/p>\"},{\"Key\":\"E\",\"Value\":\"<p>Change the parent directory owner and group to mysql<\\/p>\"},{\"Key\":\"F\",\"Value\":\"<p>Remove the world read\\/execute privilege from the accounting directory<\\/p>\"}]",
                "answer": "AF",
                "analysis": "",
                "updated_at": "2023-08-21 17:01:02",
                "question.raw": "Q164 Examine this command and output:<p> root@dbhost: /var/lib/mysql# ls -al </p><p>total 540 </p><p>drwxrwxr-x 1 mysql mysql 4096 Aug 22 14:07 </p><p>drwxr-xr-x 1 root root 4096 May 22 00:42 </p><p>-rw-r- - ---- 1 mysql mysql 56 Aug 20 13:58 auto. cnf </p><p>drwxr-xr-x 1 mysql mysql 4096 Aug 21 10:28 accounting </p><p>-rw-r--r-- 1 mysql mysql 1112 Aug 20 13:58 ca. Pem </p><p>-rw-r----- 1 mysql mysql 172040 Aug 22 14:07 ib_ buffer_ pool </p><p>-rw-r----- 1 mysql mysql 12582919 Aug 22 14:07 ibdata1 </p><p>-rw-r----- 1 mysql mysql 50331648 Aug 22 14:07 ib_ logfile0 </p><p>-rw-r----- 1 mysql mysql 50331648 Aug 20 13:47 ib_ logfile1 </p><p>-rw-r----- 1 mysql mysql 292292 Aug 22 14:07 ibtmp1 </p><p>drwxr-x--- 1 mysql users 4096 Aug 20 13:59 mysql </p><p>-rw-r----- 1 mysql mysql 64064 Aug 22 15:18 mysql -error .log d</p><p>rwxr-x--- 1 mysql mysql 4096 Aug 20 13:59 performance_ schema </p><p>-rw-rw---- 1 mysql mysql 1680 Aug 20 13:59 private_ key.pem </p><p>-rw-r--r-- 1 mysql mysql 452 Aug 20 13:59 public_ key.pem </p><p>-rw-r--r-- 1 mysql mysql 1112 Aug 20 13:58 server -cert.pem </p><p>-rw------- 1 mysql mysql 1680 Aug 20 13:58 server- key.pem </p><p>drwxr-x--- 1 mysql mysql 4096 Aug 20 13:59 sys </p><p>Which two options will improve the security of the MySQL instance? (Choose two.) </p>",
                "paper": {
                    "uid": "5982773",
                    "name": "MySQL5.8-多选1",
                    "question_total": "50",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            },
            {
                "id": "1366298744",
                "uid": "5982773",
                "paperid": "11558101",
                "question": "- - ---- 1 <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span> 56 Aug 20 13:58 auto. cnf drwxr-xr-x 1 <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span> 4096 Aug 21 10:28 accounting",
                "qtype": "2",
                "parentid": "0",
                "options": "[{\"Key\":\"A\",\"Value\":\"<p>Remove group read\\/write privileges from the private_ key. pem file <\\/p>\"},{\"Key\":\"B\",\"Value\":\"<p>Remove world read privileges from the server-cert.pem certificate file<\\/p>\"},{\"Key\":\"C\",\"Value\":\"<p>&nbsp;Change the group ownership of the mysql directory to the mysql user group<\\/p>\"},{\"Key\":\"D\",\"Value\":\"<p>Remove world read privileges from the public_ key.pem file <\\/p>\"},{\"Key\":\"E\",\"Value\":\"<p>Change the parent directory owner and group to mysql<\\/p>\"},{\"Key\":\"F\",\"Value\":\"<p>Remove the world read\\/execute privilege from the accounting directory<\\/p>\"}]",
                "answer": "AF",
                "analysis": "",
                "updated_at": "2023-08-21 17:01:02",
                "question.raw": "- - ---- 1 <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span> 56 Aug 20 13:58 auto. cnf </p><p>drwxr-xr-x 1 <span style=\"color:#ff664b;\">mysql</span> <span style=\"color:#ff664b;\">mysql</span> 4096 Aug 21 10:28 accounting",
                "paper": {
                    "uid": "5982773",
                    "name": "MySQL5.8-多选1",
                    "question_total": "50",
                    "price": "0",
                    "password": "0",
                    "is_collect": "0",
                    "author": "匿名用户"
                }
            }
        ],
        "pages": {
            "current": "1",
            "total": "500",
            "total_page": "25",
            "page_size": "20"
        }
    },
    "time": "1700806853",
    "encrypt": "yMciZXAtnTW9YJTacGmRrP=="
}


def clean_html(input):
    cleanr = re.compile('<.*?>')
    output = re.sub(cleanr, '', input)
    return output



for i in jsondata["data"]["rows"]:
    if i["qtype"] == "1":
        print("单选题：" + clean_html(i["question.raw"]))
        options_str = i["options"]
        options = json.loads(options_str)
        key = i["answer"]
        correctAnswer = next((option["Value"] for option in options if option["Key"] == key), None)
        correctAnswer = clean_html(correctAnswer)
        print("答案：" + correctAnswer)
    elif i["qtype"] == "2":
        print("多选题：" + clean_html(i["question.raw"]))
        options_str = i["options"]
        options = json.loads(options_str)
        key = i["answer"]
        correctAnswer = next((option["Value"] for option in options if option["Key"] == key), None)
        correctAnswer = clean_html(correctAnswer)
        print("答案：" + correctAnswer)
    elif i["qtype"] == "3":
        print("判断题：" + clean_html(i["question.raw"]))
        options_str = i["options"]
        options = json.loads(options_str)
        key = i["answer"]
        correctAnswer = next((option["Value"] for option in options if option["Key"] == key), None)
        correctAnswer = clean_html(correctAnswer)
        print("答案：" + correctAnswer)
    elif i["qtype"] == "4":
        print("填空题：" + clean_html(i["question.raw"]))
        print("答案：" + i["answer"])

    print()
