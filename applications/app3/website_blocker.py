import time
from datetime import datetime, time as t, timedelta as dt

filename = '/private/etc/hosts'
local_host = '127.0.0.1'
website_list = ["www.facebook.com", "facebook.com", "login.facebook.com", "www.youtube.com","youtube.com" , "www.willow.tv", "www.espn.com"]

begin_time = t(18,00)
end_time = t(21,00)

while(True):
    # Add the websites to be blocked when in the time range
    if begin_time <= datetime.now().time() <= end_time:
        file = open(filename, 'r+')
        data=file.read()
        for website in website_list:
            if website in data:
                pass
            else:
                file.write(local_host+'\t'+website+'\n')
        file.close()
    # Remove the websites if not in the time range
    else:
        file = open(filename, 'r+')
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
        file.close()

    time.sleep(10)
