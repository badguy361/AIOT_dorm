import serial

class logger:
        def __init__(self):
            self.logger = serial.Serial(
                port = '/dev/ttyAMA0',
                baudrate = 57600,
                timeout = 1)
            self.buffer =[]
        def logger(self):
            pass
            # while True:
            #     oneByte = clas_logger.logger.read(1)
        


            #     if oneByte == b'\xed':
            #         dummy = int.from_bytes(oneByte,byteorder='little')
            #         self.buffer.append(dummy)
            #         for i,val in enumerate(sebuffer):
            #             if val == 85:
            #                 startbyte = i
            #                 buffer = buffer[i:-1]
            #         print(self.buffer)
            #         return self.buffer
            #         self.buffer = []
            #     else:
            #         dummy = int.from_bytes(oneByte,byteorder='little')
            #         buffer.append(dummy)
            #print(buffer)
        #val = wind.logger.read(77)
if __name__ == "__main__": # 不會用到
    clas_logger = logger()
    buffer = []
    while True:
        oneByte = clas_logger.logger.read(1)
        if oneByte == b'\xed':
            dummy = int.from_bytes(oneByte,byteorder='little')
            buffer.append(dummy)
            for i,val in enumerate(sebuffer):
                if val == 85:
                    startbyte = i
                    buffer = buffer[i:-1]
            print (buffer)

            #print (buffer.split())
            buffer = []
        else:
            dummy = int.from_bytes(oneByte,byteorder='little')
            #print(dummy)
            buffer.append(dummy)
            #print(buffer)
        #val = wind.logger.read(77)
