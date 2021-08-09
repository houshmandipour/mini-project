import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(download)
print(upload)
print(f"Download speed : {download/8000000} MBps ")
print(f"Upload speed : {upload/8000000} MBps")
