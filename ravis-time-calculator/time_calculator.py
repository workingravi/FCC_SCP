

dow = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", )

def add_time(start, duration, start_day=None):
  start_ampm = start.split()[1].strip()
  start_hrs, start_mins = map(int, start.split()[0].split(':'))
  dur_hrs, dur_mins = map(int, duration.split()[0].split(':'))
  
  new_hrs = 0
  new_mins = start_mins + dur_mins
  if new_mins > 59:
    new_hrs += 1
    new_mins %= 60
  
  days = 0
  new_hrs += start_hrs + dur_hrs
  while new_hrs > 24:
    days += 1
    new_hrs -= 24

  new_ampm = ""  
  if new_hrs >= 12:
    if start_ampm == "PM":
      new_ampm = "AM"        
      days += 1
    else:
      new_ampm = "PM"
    if new_hrs > 12:
      new_hrs -= 12
  else:
    new_ampm = start_ampm

  new_day = ""
  si = 0
  if start_day is not None:
    si = dow.index(start_day.lower())
    new_day = ", " + dow[(si+days)%7].capitalize()
  if days == 1:
    new_day += ' (next day)'
  elif days > 1:
    new_day += f' ({days:d} days later)'


  new_time = f'{new_hrs}:{new_mins:02} {new_ampm}{new_day}'

  return new_time