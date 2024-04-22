import speedtest
from tabulate import tabulate
import time
from pandas import DataFrame
import os
clear = lambda: os.system('cls')

table_headers = ["Datetime", "Server ID", "Server Name", "Latency", "Download Speed", "Upload Speed"]
table_data = []
is_loading = False

clear()

while True:
    if is_loading:
        continue
    
    is_loading = True
    
    st = speedtest.Speedtest(secure=True)

    # Get the best server based on ping
    st.get_best_server()

    # Perform download and upload speed tests
    download_speed = st.download()
    upload_speed = st.upload()

    # Convert speeds to Mbps
    date_time = time.strftime("%Y-%m-%d %H:%M:%S")
    server_name = st.results.server["name"]
    server_id = st.results.server["id"]
    latency = st.results.ping
    download_speed_mbps = round(download_speed / 1_000_000, 2)
    upload_speed_mbps = round(upload_speed / 1_000_000, 2)
    
    table_data.append([date_time, server_id, server_name, latency, download_speed_mbps, upload_speed_mbps])
    
    is_loading = False
    
    # Save the data to a CSV file
    df = DataFrame(table_data, columns=table_headers)
    df.to_csv("speedtest.csv", index=False)
    
    clear()
    
    print(tabulate(table_data, headers=table_headers, tablefmt="pretty"))
    
    time.sleep(60)
