import time

print("                                                 I N I S I A T I N G    S Y S T E M")
print("                                               ------------------------------------")
time.sleep(0.3)
print("                                          Checking system resources ...")
time.sleep(0.3)
print("                                          Starting all the services ..")
time.sleep(0.3)
print("                                          Connecting the Database ...")
time.sleep(0.3)
print("                                          Getting user profile ...")
time.sleep(0.3)
print("                                          Connecting to the Server ...")
time.sleep(0.3)
print("                                          All Set! System load completed.")
time.sleep(0.3)
print("                                          Launching the Machine ...")
time.sleep(0.5)

print("       W E L C O M E     G E N I U S ...")
print("     ---------------------------------------    ")

from rich.progress import Progress
from rich import align

 
with Progress() as progress:

  

    task1 = progress.add_task("[#fff]ACTIVATING MACHINE PROFILE...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)


    while not progress.finished:
     
        progress.update(task1, advance=7)
        progress.update(task2, advance=2.5)
        progress.update(task3, advance=2)
        time.sleep(0.02)