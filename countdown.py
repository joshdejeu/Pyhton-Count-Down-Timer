import sys
import time

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()
def delay():
  time.sleep(.3)
def flush():
  sys.stdout.flush()

def restart_delay_flush():
  flush()
  restart_line()
  delay()

def Timer():
  g='\033[92m'
  y='\033[93m'
  r='\033[91m'
  color_gallery=[g,y,r]
  timer=float(input("Time: "))
  signal=0
  while timer>timer-timer:
    if timer>6:
      signal=0
    elif timer<6 and timer>3:
      signal=1
    elif timer<=3:
      signal=2
    print(color_gallery[signal],round(timer,1))
    timer=timer-0.1
    restart_line()
    time.sleep(.1)

  print("""                 
                  TIME IS UP!!!!!!!""")
  flushed()

def replay():
  sys.stdout.write('Ready?')
  sys.stdout.flush()
  time.sleep(2) # wait 2 seconds...
  restart_line()
  sys.stdout.write('GOOOO!')
  sys.stdout.flush()

def flushed():
  sys.stdout.write('\033[92m.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*')
  restart_delay_flush()
  sys.stdout.write('\033[93m*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.')
  restart_delay_flush()
  flushed()

print("\t\t\tWelcome to the Stop Watch!\nEnter a number you would like to count down from, the color will change when there is 6 seconds and 3 seconds left. It will stop at 0")
Timer()