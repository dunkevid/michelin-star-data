import sys
import getopt

from main import main

argv = sys.argv
arg_star = 1
arg_start_page = 1
arg_end_page = -1
arg_is_continue = True
arg_help = '{0} -st <star> -s <start-page> -e <end-page> -ic <is-continue>'.format(argv[0])

try:
  opts, args = getopt.getopt(
    argv[1:],
    'hi:st:s:e:ic',
    ['help', 'star=', 'start-page=', 'end-page=', 'is-continue=']
  )
except:
  print(arg_help)
  sys.exit(2)

for opt, arg in opts:
  if opt in ('-h', '--help'):
    print(arg_help)  # print the help message
    sys.exit(2)
  elif opt in ('-st', '--star'):
    arg_star = arg
  elif opt in ('-s', '--start-page'):
    arg_start_page = arg
  elif opt in ('-e', '--end-page'):
    arg_end_page = arg
  elif opt in ('-ic', '--is-continue'):
    arg_is_continue = arg

print('Star:', arg_star)
print('Start page:', arg_start_page)
print('End page:', arg_end_page)
print('Is continue crawling next star:', arg_is_continue)
print('\n')

main(
  int(arg_star),
  int(arg_start_page),
  int(arg_end_page),
  bool(arg_is_continue)
)
