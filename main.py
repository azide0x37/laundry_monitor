import os
import sys
import pync
import asyncio

from os import getpid
from time import sleep
from subprocess import run
from kasa import SmartPlug

def generate_power_table(device='Test', power='69'):
  # Calculate Length
  fill_device = max( 8, len(device) + 2)
  fill_power_usage = 13 #
  
  # Set Up Headers
  device_title = ' Device '
  device_name = ''.join([' ', device, ' '])

  # Print table
  print(f'╔{fill_device * "═"}╦{fill_power_usage * "═"}╗')
  print(f'║{device_title}{(fill_device - len (device_title)) * " "}║ Power Usage ║')
  print(f'╠{fill_device * "═"}╬{fill_power_usage * "═"}╣')
  print(f'║{device_name}{ 0 * " "}║{(fill_power_usage - len(str(power)) - 2 ) * " "}{power}W ║')
  print(f'╚{fill_device * "═"}╩{fill_power_usage * "═"}╝')

async def main(ip: str="127.0.0.2"):
  plug = SmartPlug(ip)  # We create the instance inside the main loop
  running = False
  
  while True:
    await plug.update()  # Request an update

    power = await plug.get_emeter_realtime()

    if (not running and power.power > 5.0):
      pync.notify('Started a load of laundry...', title='Laundry Monitor', subtitle='Starting Wash')
      #run(['say', '-v', 'Samantha', f'Washing machine has started. Current power usage is {round(power.power, 1)} watts.'])
      running = True

    if (running):
      # Clear Console
      os.system('cls' if os.name == 'nt' else 'clear')  
      generate_power_table()
      generate_power_table(device='Washing Machine', power=round(power.power, 2))

    if (power.power < 2.0 and running):
      pync.notify('Done washing!', title='Laundry Monitor', subtitle='Completed')
      run(['say', '-v', 'Samantha', 'Washing machine has finished the cycle! Rotate laundry now for optimal performance.'])
      running = False

    await asyncio.sleep(0.5)  # Sleep some time between updates

if __name__ == "__main__":
  try:
    asyncio.run(main(sys.argv[1]))
  except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('See ya!')
    sys.exit()
