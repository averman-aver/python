from sys import argv

script_name, work_time, rate, premium = argv

print('Заработная плата, $: ', int(work_time) * float(rate) + float(premium))

# скрипт для MacOS -  python3 1_task.py 8 10.2 50