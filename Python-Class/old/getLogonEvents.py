import paramiko
import sys
import getpass

# get the command-line arguments
# filename = sys.argv[1]
# username = sys.argv[2]
# hostname = sys.argv[3]
# remote_folder = sys.argv[4]
# remote_file = remote_folder + '/' + filename


username = 'Administrator'
hostname = '192.168.56.109'
filename = 'Security.evtx'
log_location = 'C:/Windows/System32/winevt/Logs/'

# prompt for the password
password = getpass.getpass(prompt='Password: ')
print("pass done.")

# create an SSH client
client = paramiko.SSHClient()
print("ssh")
# add the remote server's host key
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("paramiko")

try:
    # connect to the remote server
    client.connect(hostname=hostname, username=username, password=password, timeout=30)
    print("connect")
except Exception as e:
    print("connection failed")
    sys.exit(1)

# use the SCP client to copy the file
scp = client.open_sftp()
print("scp")
# scp.get(remote_file, filename)
scp.get(log_location + filename, filename)
print("scp.get")
scp.close()
print("scp.close")

# close the SSH client
client.close()




# import subprocess

# remote_computer = "WIN-6RTHQD6ABVF"
# remote_computer = "192.168.56.109"

# result = subprocess.run(f"powershell.exe -File getUserLogonWindows.ps1 -computer {remote_computer}",
#                         stdout = subprocess.PIPE,
#                         stderr = subprocess.PIPE,
#                         shell=True)

# print("running\n")
# print(result.stdout.decode("utf-8"))

# from winrm.protocol import Protocol

# remote_computer = "your_remote_computer_name"
# username = "your_username"
# password = "your_password"

# p = Protocol(
#     endpoint=f"http://{remote_computer}:5985/wsman",
#     transport="ntlm",
#     username=username,
#     password=password,
#     server_cert_validation="ignore",
# )

# shell_id = p.open_shell()
# command_id = p.run_command(shell_id, "powershell.exe", [
#     "-File", "script.ps1",
#     "-computer", remote_computer
# ])
# std_out, std_err, return_code = p.get_command_output(shell_id, command_id)
# p.cleanup_command(shell_id, command_id)
# p.close_shell(shell_id)

# print(std_out.decode("utf-8"))
