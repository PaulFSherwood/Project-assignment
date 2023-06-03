# import Evtx.Evtx as evtx

# filename = "Security.evtx"
# log = evtx.Evtx(filename)
# record = 4624



# # with evtx.Evtx(filename) as log:
# #     for record in log.records():
# #         if record.event_num() == record:
# #             print(record)


# def get_record_by_num(log, record_num):
#     for record in log.records():
#         if record.record_num() == record_num:
#             print(record)
#             return record
#     raise KeyError(record_num)


# with evtx.Evtx(filename) as log:
#     try:
#         record = get_record_by_num(log, record)

#     except KeyError as e:
#         print(f"Record number {e.args[0]} not found in the log")



import subprocess
import getpass

user_name = 'Administrator'
computer_name = "192.168.56.109"
last_events = 30

# print('password:')
password = getpass.getpass()

    # ssh {user_name}@{computer_name} "powershell.exe Get-WinEvent -FilterHashtable @{logname='security'; id=4624}"
cmd = "sshpass -p password ssh {user_name}@{computer_name} \"powershell.exe Get-WinEvent -FilterHashtable @{logname='security'; id=4624}\""

result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

logon_events = result.stdout


print("Output from stdout:")
print(result.stdout.read().decode())
print("Output from stderr:")
print(result.stderr.read().decode())


print(logon_events)
