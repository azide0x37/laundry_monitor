import sys
import pync
import asyncio

from os import getpid
from time import sleep
from subprocess import run
from kasa import SmartPlug

async def main(ip: str="127.0.0.2"):
  plug = SmartPlug(ip)  # We create the instance inside the main loop
  running = False
  
  while True:
    await plug.update()  # Request an update

    power = await plug.get_emeter_realtime()

    if (not running and power.power > 5.0):
      pync.notify('Started a load of laundry...', title='Laundry Monitor', subtitle='Starting Wash')
      run(['say', '-v', 'Samantha', f'Washing machine has started. Current power usage is {round(power.power, 1)} watts.'])
      running = True

    if (running):
      print(f'Current power usage is {round(power.power, 2)} watts.', end='\r')

    if (power.power < 2.0 and running):
      pync.notify('Done washing!', title='Laundry Monitor', subtitle='Completed')
      run(['say', '-v', 'Samantha', 'Washing machine has finished the cycle! Rotate laundry now for optimal performance.'])
      running = False

    await asyncio.sleep(0.5)  # Sleep some time between updates

if __name__ == "__main__":
  asyncio.run(main(sys.argv[1]))
