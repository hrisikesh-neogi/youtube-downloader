from pytube import YouTube
from fastapi import FastAPI
from fastapi import FastAPI, Request
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from uvicorn import run as app_run
from starlette.responses import FileResponse

import os


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/download_video')
async def download_video(youtube_video_url):

    try:
        download_dir = 'downloads'
        video_file_name = 'video.mp4'

        youtubeObject = YouTube(youtube_video_url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        file_path = os.path.join(download_dir,video_file_name)
        youtubeObject.download(filename=file_path)

        return FileResponse(file_path,media_type='application/octet-stream', filename=video_file_name)


    except Exception as e:
        print("error while downloading the video. \n",e)



if __name__ == "__main__":
    app_run(app)

