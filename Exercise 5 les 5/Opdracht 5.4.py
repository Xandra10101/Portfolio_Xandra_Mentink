import time
import datetime
outfile = open('hardlopers.txt', 'w')
vandaag = datetime.datetime.today()
s = vandaag.strftime('%a %d %b %Y')
# outfile.write(time.strftime('%A %b/%d/%y %H:%M %p', time.gmtime()))
outfile.write('Thu 10 Mar 2016, 10:45:52, Miranda\n')
outfile.write('Thu 10 Mar 2016, 10:46:04, Piet\n')
outfile.write('Thu 10 Mar 2016, 10:47:27, Sacha\n')
outfile.write('Thu 10 Mar 2016, 10:48:33, Karel\n')
outfile.write('Thu 10 Mar 2016, 10:48:42, Kemal\n')
outfile.close()

print(s)
