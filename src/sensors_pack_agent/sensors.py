import serial
import rospy

class SEN0233:
    def __init__(self):
        physicalPort = '/dev/ttyS0'

        self.serialPort = serial.Serial(physicalPort)

    def data(self) -> dict:
        rospy.loginfo("In waiting data: {}".format(self.serialPort.in_waiting))
        if self.serialPort.in_waiting >= 40:
            # Check that we are reading the payload from the correct place (i.e. the start bits)
            data = self.serialPort.read(40)

            CR1 =(data[38]<<8) + data[39];
            CR2 = 0;
            for i in range(38):
                CR2 += data[i]

            if CR1 == CR2:
                PMSa=data[12]         #Read PM2.5 High 8-bit
                PMSb=data[13]         #Read PM2.5 Low 8-bit
                PMS=(PMSa<<8)+PMSb          #PM2.5 value
                FMHDSa=data[28]         #Read Formaldehyde High 8-bit
                FMHDSb=data[29]         #Read Formaldehyde Low 8-bit
                FMHDS=(FMHDSa<<8)+FMHDSb     #Formaldehyde value
                TPSa=data[30]          #Read Temperature High 8-bit
                TPSb=data[31]          #Read Temperature Low 8-bit
                TPS=(TPSa<<8)+TPSb        #Temperature value
                HDSa=data[32]          #Read Humidity High 8-bit
                HDSb=data[33]          #Read Humidity Low 8-bit
                HDS=(HDSa<<8)+HDSb      #Humidity value
            else:
                PMS = 0
                FMHDS = 0
                TPS = 0
                HDS = 0

            res = {
                    "temp_c": round(TPS/10, 2),
                    "humidity": round(HDS/10, 2),
                    "formaldehyde": FMHDS,
                    "pm2.5": PMS
                    }
            rospy.loginfo(res)
            return res

