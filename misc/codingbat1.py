def date_fashion1(you, date):
  if you <= 2 or date <= 2:
     return 0
  elif you >= 8 or date >= 8:
     return 2 
  else:
     return 1

date_fashion1(5,10)
date_fashion1(5,2)
date_fashion1(5,5)


def date_fashion2(you, date):
    answer = 0
    either_unstylish = you<=2 or date<=2
    either_verystylish = you>=8 or date>=8
    answer = 2*int(either_verystylish and not either_unstylish) + \
                     1*int(not either_verystylish and not either_unstylish)
    return answer

date_fashion2(5,10)
date_fashion2(5,2)
date_fashion2(5,5)

