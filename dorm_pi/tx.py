
from serial import Serial as s
from threading import Thread
import time
from sencor import rx, postdata
from threading import Thread as th
from tx_test import logger

header = b"\x55\x44\x09\x01\x01"
vol = b"\xfa" * 16
status = b"\xff" * 2
cks = b"\xfe"
end = b"\xed"
#port=s(port="/dev/ttyUSB0",baudrate=57600,timeout=1)
clas_logger = logger()
# def tx_job(): # 似乎沒用到
#     while True:
#         print((sum(list(header + vol + status))-85)%255)
#         port.write(header + vol + status + cks + end)
#         print("send {}".format(header + vol + status + cks + end))
#         time.sleep(3)

#th(target=tx_job).start()
th(target=postdata).start()
#th(target=mysql).start()

rx(clas_logger.logger) # 傳輸資料->存logger
