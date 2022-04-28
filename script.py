import psutil
import time

# Get the initial data.
last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent

while True:

    # Get the current data.
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent

    # Substract the previous from the current we get how much was received/sent in between.
    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent

    print(f'Received {new_received} bytes and sent {new_sent} bytes.')

    # Update both receive and sent.
    last_received = bytes_received
    last_sent = bytes_sent

    time.sleep(1)


    

