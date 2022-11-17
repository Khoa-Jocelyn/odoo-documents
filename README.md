<div align="center">
  <img src="https://badgen.net/github/stars/Mountant2021/document?icon=github&color=4ab8a1">&emsp;<img src="https://badgen.net/github/forks/Mountant2021/document?icon=github&color=4ab8a1">&emsp;<a href="https://github.com/Mountant2021/document/releases"><img src=https://img.shields.io/github/downloads/Mountant2021/document/total></a>&emsp;<a href="https://github.com/HypoX64/DeepMosaics/releases"><img src=https://img.shields.io/github/v/release/hypox64/DeepMosaics></a>&emsp;<img src=https://img.shields.io/github/license/Mountant2021/document>
</div>

<h1>Setup Development Environment</h1>

<b>The following article is a guide for Ubuntu Operating System.


## Update OS

```sh
sudo add-apt-repository universe
sudo add-apt-repository "deb http://mirrors.kernel.org/ubuntu/ xenial main"
sudo apt-get update
sudo apt-get upgrade -y
```

## Install Python

- Install Python 3.6

```sh
sudo apt install python3.6-dev python3.6-venv
python3.6 --version (check version)
```
- Install Python 3.7

```sh
sudo apt install python3.7-dev python3.7-venv
python3.7 --version (check version)
```
- Install Python 3.8

```sh
sudo apt install python3.8-dev python3.8-venv
python3.8 --version (check version)
```
- Install Python 3.9
```sh
sudo apt install python3.9-dev python3.9-venv
python3.9 --version (check version)
```
## Install Virtual Environments

- Create a directory containing python venv by convention located in the Home directory

- Python 3.6 Environment
```sh
python3.6 -m venv ~/python3.6-venv/odoo13
python3.6 -m venv ~/python3.6-venv/odoo14
```
- Python 3.7 Environment
```sh
python3.7 -m venv ~/python3.7-venv/odoo13
python3.7 -m venv ~/python3.7-venv/odoo14
```
- Python 3.8 Environment
```sh
python3.8 -m venv ~/python3.8-venv/odoo13
python3.8 -m venv ~/python3.8-venv/odoo14
```

- Python 3.9 Environment
```sh
python3.9 -m venv ~/python3.9-venv/odoo13
python3.9 -m venv ~/python3.9-venv/odoo14
```
## Git

- Install Git

```sh
sudo apt update
sudo apt install git
git --version (check version)
```

- Connecting to GitHub with SSH

[Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- <b>Go to Home > Ctrl H to show hidden files and find the .ssh folder, inside there are id_rsa and id_rsa.pub files. Note: Do not share the file id_rsa.

## Install dependencies, Environment Other

- Nodejs, npm, python-pip,...

```sh
sudo apt-get install python3 python3-pip python3-venv python-dev python3-dev python3-wheel python-setuptools libxslt-dev libxml2-dev libxslt1-dev libzip-dev zlib1g-dev libjpeg-dev libldap2-dev libssl-dev libsasl2-dev libpq-dev python3-setuptools build-essential wget node-less gdebi -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install nodejs npm -y
sudo npm install -g rtlcss
sudo npm install -g npm
sudo -H pip3 install --upgrade pip
```

## Install Wkhtmltopdf

```sh
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb
wkhtmltopdf --version (check version)
```

## Install PostgreSQL Server

```sh
sudo apt-get install postgresql postgresql-server-dev-all -y
sudo su - postgres -c "createuser -s user_dang_nhap_vao_may"
```

## Install PgAdmin 4

```sh
wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v5.7/pip/pgadmin4-5.7-py3-none-any.whl
pip3 install pgadmin4-5.7-py3-none-any.whl
sudo apt install curl
sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4-desktop
```

## Create Role In PgAdmin 4

```sh
sudo service postgresql start
sudo -u postgres psql
```
## Postgres window appears

```sh
CREATE USER <username> WITH LOGIN SUPERUSER CREATEDB CREATEROLE INHERIT REPLICATION CONNECTION LIMIT -1;
ALTER USER postgres PASSWORD '<password>';
```
## Install Eclipse

```sh
sudo snap install --classic eclipse
sudo apt install default-jre
```
## Clone odoo to git

```sh
 git clone <SSH_repository_odoo_link> --depth 1 -b 14.0.
 source activate
 pip install -r /home/khoa-jocelyn/git-clone/odoo14/requirements.txt
```
## Create odoo module new

```sh
./odoo-bin scaffold <module-name> <folder-path-to-save-module>
```
