from loop import tl
import time

def main():
    tl.start()
    
    while True:
      try:
         time.sleep(1)
      except Exception as e:
         tl.stop()
         break

if __name__ == '__main__':
    main()
    