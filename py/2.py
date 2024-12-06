from yt_dlp import YoutubeDL
 
video_url = "https://www.youtube.com/watch?v=Ndh-kpmngE0"
opts = dict()
 
with YoutubeDL(opts) as yt:
    info = yt.extract_info(video_url, download=False)
    video_title = info.get("title")
    width = info.get("width")
    height = info.get("height")
    language = info.get("language")
    channel = info.get("channel")
    likes = info.get("like_count")
     
    data = {
        "URL": video_url,
        "Title": video_title,
        "Width": width,
        "Height": height,
        "Language": language,
        "Channel": channel,
        "Likes": likes
    }
    print(data)