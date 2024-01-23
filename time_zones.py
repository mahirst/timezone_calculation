#calculate time zone differences for meeting setups

import pytz
from datetime import datetime
from pytz import timezone

def time_difference_with_EST(target_timezone_str):
    try:
        # define the EST timezone (your location)
        est = timezone('US/Eastern')

        # define the target timezone
        target_timezone = timezone(target_timezone_str)

        # get the current time in EST
        est_time = datetime.now(est)

        # convert the current EST time to target timezone time
        target_time = est_time.astimezone(target_timezone)

        # calculate the difference
        time_difference = target_time - est_time

        # format the time difference in hours and minutes
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # adjust for days if necessary
        if time_difference.days < 0:
            hours = 24 - hours

        return f"Time difference between EST and {target_timezone_str}: {hours} hours and {minutes} minutes"
    except pytz.UnknownTimeZoneError:
        return "Unknown time zone: " + target_timezone_str

# example usage
print(time_difference_with_EST('Europe/London'))

