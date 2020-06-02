from urllib.request import FancyURLopener
import bs4 as bs
import os
import subprocess
import random
import youtube_dl

# emotion=['angry','disgust','fear','happy','sad','surprise','neutral']
# selectedEmot = 0;
class Songs:
    def songs_scrapping(emot):
#         selectedEmot=emot
        a2=[]
        word2 = emot + " songs"
        word2 = word2+' lyrics'
        url2 = 'https://www.youtube.com/results?search_query=+'+word2
        yt2='https://www.youtube.com'
        #webbrowser.open_new_tab(url)
        class MyOpener2(FancyURLopener):
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'   # Set this to a string you want for your user agent

        myopener2 = MyOpener2()
        page2 = myopener2.open(url2).read()
        webpage2 = page2.decode('utf-8')

        soup2 = bs.BeautifulSoup(webpage2,'lxml')

        div2 = soup2.body
        for data2 in div2.find_all(href=True):
            x = data2.get('href')
            if x.startswith('/watch?'):
                a2.append(x)
            #a2.append(data2.get('href'))


        matching2 = [s2 for s2 in a2 if '/watch?' in s2]

        for s in range(1,5):
            print(s)
            asa2 =matching2[s]
            asa2 = asa2.replace('/watch?v=','')
            print(asa2)

            ytplaylink2 = yt2+matching2[0]
            # print(ytplaylink2)
            word2 = word2.replace(" ","_")
            word2 = '1_'+word2
            os.system("cd C:\\Users\\ZEE\\Documents\\emosic\\songs\\" + emot + " && youtube-dl -x --audio-format mp3 "+asa2)
        #   os.system("cd C:\\Users\\hasib\\Desktop\\DLLL && py -3 -m youtube_dl --restrict-filenames --ignore-errors -x --audio-format mp3 "+asa2)
        print("Finish")
        for root, dirs,files in os.walk("C:\\Users\\ZEE\\Documents\\emosic\\songs\\"+ emot):
            next_song=str(random.choice(os.listdir("C:\\Users\\ZEE\\Documents\\emosic\\songs\\"+ emot)))
            print(next_song)
            path = "C:\\Users\\ZEE\\Documents\\emosic\\songs\\"+ emot+"\\"+ next_song
            os.system('"'+path+'"')
obj = Songs
emotion = 'sad'
obj.songs_scrapping(emotion)