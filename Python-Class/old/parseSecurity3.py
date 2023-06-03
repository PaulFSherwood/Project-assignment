import paramiko
import getpass

hostname = '192.168.56.109'
username = 'Administrator'
password = getpass.getpass()
input_value = 10
id_name = 4624

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname, username=username, password=password)

command = "powershell.exe Get-WinEvent -FilterHashtable @{{logname='security'; id={}}} -MaxEvents {}".format(id_name, input_value)
stdin, stdout, stderr = ssh.exec_command(command)

# stdin, stdout, stderr = ssh.exec_command("powershell.exe Get-WinEvent -FilterHashtable @{{logname='security'; id=4624}}")
# stdin, stdout, stderr = ssh.exec_command("powershell.exe Get-WinEvent -FilterHashtable @{logname='security';Id=4624} -MaxEvents 30")
# stdin, stdout, stderr = ssh.exec_command("powershell.exe Get-WinEvent -FilterHashtable @{logname='security';Id=4624} -MaxEvents 30")

return_code = stdout.channel.recv_exit_status()
if return_code == 0:
    print("Command executed successfully")
else:
    print("Command failed with return code:", return_code)

print("Output from stderr:")
print(stderr.read().decode())

result = stdout.read().decode()
lines = result.split("\n")
for line in lines:
    if line.strip():
        line_split = line.strip().split(" ", maxsplit=1)
        print(line_split[-1])


ssh.close()
