from flask import Flask, request, render_template, send_file
import yt_dlp as youtube_dl
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download_video():
    video_url = request.form.get("videoURL")
    download_path = request.form.get("downloadPath")
    options = {
        "format": "best",
        "outtmpl": os.path.join(download_path, "video.%(ext)s"),
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_url])
    return send_file(os.path.join(download_path, "video.mp4"), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
