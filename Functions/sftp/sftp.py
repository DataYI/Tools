# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:06:19 2018

@author: DataAnt
"""
import paramiko
from pathlib import Path, PurePosixPath


def create_sftp(ip, port, username, key_file):
    key = paramiko.RSAKey.from_private_key_file(key_file)
    t = paramiko.Transport(ip, port)
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    return sftp

def create_ssh(ip, port, username, key_file):
    key = paramiko.RSAKey.from_private_key_file(key_file)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, port=port, pkey=key)
    return ssh


def put_dir(sftp, ssh, l_dir, r_dir):
    ssh.exec_command('mkdir -p %s' % str(r_dir))
    for p in l_dir.iterdir():
        if p.is_file():
            sftp.put(p, str(r_dir / p.relative_to(l_dir)))
            print(r_dir / p.relative_to(l_dir))
        elif p.is_dir():
            r_path = r_dir / p.relative_to(l_dir)
            ssh.exec_command('mkdir -p %s' % str(r_path))
            put_dir(sftp, ssh, p, r_path)


def main(l_dir, r_dir):
    key_file = Path(r'D:\Tools\ssh-key\my_ali')
    ip = '192.37.24.135'
    port = 1022
    username = 'root'
    with create_sftp(ip, port, username, key_file) as sftp, \
         create_ssh(ip, port, username, key_file) as ssh:
        put_dir(sftp, ssh, l_dir, r_dir)


if __name__ == '__main__':
    # 本地文件夹路径
    l_dir = Path(r'E:\Parkings\clean_up_api')
    # 远程文件夹路径
#    r_dir = PurePosixPath('/root/my_vol')
    r_dir = PurePosixPath('/root/flask_api')
#    l_dir = Path(r'E:\PythonData\flask\uwsgi')
#    r_dir = PurePosixPath('/root/my_vol/uwsgi')
    main(l_dir, r_dir)