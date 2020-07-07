# Environment setting #

Outline:  
I'm using Windows 10 Home edition as my workstation.  
I use WSL(Windows Subsystem Linux) on my Windows 10 OS as my programming development environment.  
If you are interested in WSL, you can find the manual [here][SetUpVSCodeSetUpWSL].

## Install Pyenv and Python interpreter ##

I really love the development tool -- [Pyenv][Pyenv].  
Pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

## Install IPython for Scrapy Shell ##

Jupyter Notebook is a powerful and must-learn modern IDE for Python programmers.  
And Scrapy recommends to run Scrapy Shell with IPython, so I also [installed IPthon][InstallIpthon].  

For guys who already installed Python 3+:  
```shell
pip install -i https://mirrors.aliyun.com/pypi/simple/ ipython
```

## Workspace dir ##

`cd /mnt/c/GOOGLE~1/works/sunvalley/PycharmProjects/geekbangtrain_scrapy`

# Scrapy project #

## Create Scrapy project and a spider ##

```shell
mkdir -pv randproxy
scrapy startproject myproject randproxy
cd randproxy
scrapy genspider httpbin httpbin.org
```


## Get free proxy server ##

```shell
curl "http://pubproxy.com/api/proxy?limit=10&format=json&type=http&level=anonymous&speed=10"
```

## Launch the Scrapy Shell ##

```shell
cd /mnt/c/GOOGLE~1/works/sunvalley/PycharmProjects/geekbangtrain
scrapy shell http://httpbin.org/ip
```

## Debug the spiders ##

```shell
# debug parse method
scrapy parse http://httpbin.org/ip -c parse --nolog
```

## Connect to mysql database ##

I am using [Bitnami's MariaDB][BitnamiMariadb] repository to run my MariaDB docker container.  
You can find the Docker Compose file [here][MariadbDockerCompose].

-   First, find the IP of my WSL host

    ```shell
    DEFAULT_INF=`ip route show | grep default | awk '{print $5}'` && \
        ip addr show $DEFAULT_INF | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
    ```

-   Connect to the MariaDB with client...

-   Create database and table for geekbangtrain homework

    ```sql
    -- Create database
    CREATE DATABASE `geekbangtrain_homework` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';
    ```

    ```sql
    -- Create table for Maoyan movie
    CREATE TABLE `maoyan_movie` (
      `movie_no` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT COMMENT 'movie number, primary key',
      `title` varchar(255) NOT NULL COMMENT 'movie title',
      `genre` varchar(255) NOT NULL DEFAULT '' COMMENT 'movie genre',
      `release_date` date NOT NULL COMMENT 'movie release date',
      PRIMARY KEY (`movie_no`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
    ```

-   Try insert some entries into the table

    Because I forgot most of the knowledge of SQL, and I'm going to finish the homework with [pymysql][pymysql], so I have to know how would the SQL be like.  
    So I use the Navicat client to insert some entries and show the SQL for me.

    The insert SQL DML is like below:  
    ```sql
    INSERT INTO `geekbangtrain_homework`.`maoyan_movie`(`movie_no`, `title`, `genre`, `release_date`) VALUES (NULL, '[\'天气之子\']', '爱情／动画／奇幻', '2019-11-01');
    ```
    **Please ignore the data format, I'm lazy...**

[SetUpVSCodeSetUpWSL]: https://code.visualstudio.com/docs/remote/wsl#_getting-started
[Pyenv]: https://github.com/pyenv/pyenv
[InstallIpthon]: https://ipython.org/install.html
[BitnamiMariadb]: https://hub.docker.com/r/bitnami/mariadb/
[MariadbDockerCompose]: ./docker/docker-compose_files/docker-compose-mariadb.yml
[pymysql]: https://github.com/PyMySQL/PyMySQL
