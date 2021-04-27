import pytube
import time
import sys


readPath = ""
savePath = ""
startDownloadFrom=""
print(sys.argv)
print(len(sys.argv))
for i, arg in enumerate(sys.argv):
    if i == 1:
        readPath = arg
    if i == 2:
        savePath = arg
    if i == 3:
        startDownloadFrom = arg
if len(sys.argv)!=4:
    print("Not Enought args")
    exit(200);
print("from"+readPath)
print("to"+savePath)
print("startingfrom "+startDownloadFrom);
i=input("stop")
file1 = open('/Users/jim/Desktop/urls.txt', 'r')
urls = file1.readlines()

count = 0
#42
startDownloadFrom = int(input(f"Where to start from ,{len(urls)} videos found ?type 0 is the first:"))
for i in range(startDownloadFrom, len(urls)):
    try:
        start = time.time()
        count += 1
        youtube = pytube.YouTube(urls[i].strip().replace("https", "http"))
        video = youtube.streams.get_highest_resolution()
        video.download('/Users/jim/Desktop/Eutixismenoi Mazi')
        end = time.time()
        print(f"downloaded {count}/{len(urls)-startDownloadFrom} took {end-start}sec estimated time {(end-start)*(len(urls)-count-startDownloadFrom)/60}mis to finish")
    except Exception:
        print("Something Went Wrong")
