import threading
from main import main

# 20 restaurants per page
# 1 star ~2800 restaurants -> ~140 pages
# 2 stars ~500 restaurants -> ~25 pages
# 3 stars ~140 restaurants -> ~7 pages

try:
  # 1 star thread
  s1_t1 = threading.Thread(target=main, args=(1, 1, 30, False))
  s1_t2 = threading.Thread(target=main, args=(1, 30, 60, False))
  s1_t3 = threading.Thread(target=main, args=(1, 60, 90, False))
  s1_t4 = threading.Thread(target=main, args=(1, 90, -1, False))

  # 2 stars thread
  s2_t1 = threading.Thread(target=main, args=(2, 1, 20, False))
  s2_t2 = threading.Thread(target=main, args=(2, 20, -1, False))

  # 3 stars thread
  s3_t1 = threading.Thread(target=main, args=(3, 1, -1, False))

  s1_t1.start()
  s1_t2.start()
  s1_t3.start()
  s1_t4.start()
  s2_t1.start()
  s2_t2.start()
  s3_t1.start()

except:
  print('Error')
