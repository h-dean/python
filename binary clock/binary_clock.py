import datetime

def dec_to_bin(num):
    return "{0:06b}".format(num)      

def format_bin(bnum):
    return bnum.replace("1", "X\t").replace("0", "\t")

timestamp = datetime.datetime.now()
time = [timestamp.hour, timestamp.minute, timestamp.second]

print("\t3\t1\t8\t4\t2\t1")
print("\t2\t6\n")
print("Hour\t" +
      format_bin(dec_to_bin(time[0])) +
      "\n")
print("Minute\t" +
      format_bin(dec_to_bin(time[1])) +
      "\n")
print("Second\t" +
      format_bin(dec_to_bin(time[2])) +
      "\n")
