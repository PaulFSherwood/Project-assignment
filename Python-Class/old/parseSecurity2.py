# import paramiko

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='hostname', username='username', password='password')

# stdin, stdout, stderr = ssh.exec_command('powershell.exe Get-WinEvent -FilterHashtable @{logname='security'; id=4624}')


import paramiko
import getpass

hostname = '192.168.56.109'
username = 'Administrator'
password = getpass.getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# ssh {user_name}@{computer_name} "powershell.exe Get-WinEvent -FilterHashtable @{logname='security'; id=4624}"
# stdin, stdout, stderr = client.exec_command('powershell.exe Get-WinEvent -FilterHashtable @{logname='security'; id=4624}')
# stdin, stdout, stderr = client.exec_command("powershell.exe Get-WinEvent -FilterHashtable @{{logname='security'; id=4624}}")
stdin, stdout, stderr = client.exec_command('ssh {username}@{hostname} powershell.exe Get-WinEvent -FilterHashtable @{{logname="security"; id=4624}}')


print("Output from stdout:")
print(stdout.read().decode())
print("Output from stderr:")
print(stderr.read().decode())

client.close()