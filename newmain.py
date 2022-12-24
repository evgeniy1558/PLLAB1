import sys
import math
import requests
import time



print ("Hello, please wait a few seconds")

def human_format(size:int):
    pwr = math.floor(math.log(size, 1024))
    suff = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    if size > 1024 ** (len(suff) - 1):
        return "don't know how to call this format"
    return f"{size / 1024 ** pwr:.0f}{suff[pwr]}"


def WgetFunc(url: str):
    response = requests.get(url)
    NewDownloadFile = url.split('/')[-1]
    NewDownloadFile_size = int(response.headers.get('content-length'))
    with open(NewDownloadFile,'wb') as file:
        print("Download")
        download_size = 0
        for size in response.iter_content(1000000):
            download_size = download_size + len(size)
            file.write(size)
            time.sleep(1)
            print("%s/%s" % (human_format(download_size), human_format(NewDownloadFile_size)))
            if human_format(download_size) == human_format(NewDownloadFile_size):
                print("Download success")
                break




if __name__ == "__main__":
    if len(sys.argv) > 1:
        WgetFunc(sys.argv[1])