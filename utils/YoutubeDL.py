import yt_dlp

class YouTubeDL:
    def __init__(self, url):
        self.url = url
        self.info = self.getVideoInfo()

    def getVideoInfo(self):
        ydl = yt_dlp.YoutubeDL()
        info = ydl.extract_info(self.url, download=False)
        
        return info

    def getVideoTitle(self):
        return self.info["title"]
    
    def getVideoThumbnail(self):
        return self.info["thumbnail"]
    
    def getVideoFormats(self):
        return self.info["formats"]
    

if __name__ == "__main__":
    ytdl = YouTubeDL("https://www.youtube.com/watch?v=8Qn_spdM5Zg")
    print(ytdl.getVideoTitle())
    print(ytdl.getVideoThumbnail())
    print(ytdl.getVideoFormats())