from django.shortcuts import render
import datetime
from dateutil import tz

def datetime_offsets(request):
    # Get the current time in UTC
    now_utc = datetime.datetime.now(tz=tz.UTC)
    
    # Define the local timezone (you can change this to your desired timezone)
    local_tz = tz.gettz('America/New_York')
    
    # Convert the current time to the local timezone
    now_local = now_utc.astimezone(local_tz)
    
    # Calculate the offsets
    four_hours_ahead = now_local + datetime.timedelta(hours=4)
    four_hours_before = now_local - datetime.timedelta(hours=4)
    
    # Prepare the context for rendering the template
    context = {
        'current_datetime': now_local,
        'four_hours_ahead': four_hours_ahead,
        'four_hours_before': four_hours_before,
    }
    
    return render(request, 'datetime_offsets.html', context)
