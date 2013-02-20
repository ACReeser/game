import curses

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

def center(x):
   screen.addstr(12, 40 - (len(x) * 1/2), x)

center("PRESS A BUTTON, MOTHERFUCKER!")

while True:
   event = screen.getch()
   if event == ord("q"): break
   elif event == ord("p"):
      screen.clear()
      center("The User Pressed Lower Case p")
   elif event == ord("P"):
      screen.clear()
      center("The User Pressed Upper Case P")
   elif event == ord("3"):
      screen.clear()
      center("The User Pressed 3")
   elif event == ord(" "):
      screen.clear()
      center("The User Pressed The Space Bar")
 #  elif event == ord("^^A"):
 #     screen.clear()
 #     center("The User pressed the up key.")   

curses.endwin()

