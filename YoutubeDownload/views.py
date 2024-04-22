from django.shortcuts import render
from pytube import *
from pytube.exceptions import RegexMatchError

def index(request):
    error_message = None
    if request.method == 'POST':
        link = request.POST.get('link')
        download_path = r'C:\Users\Millennium_006\Downloads'
        try:
            video = YouTube(link)
            stream = video.streams.filter(res='2160p').first()
            if stream:
                stream.download(output_path=download_path)
                return render(request, 'Downloaded.html')
            else:
                error_message = "No streams found for the video."
        except RegexMatchError:
            error_message = "Invalid YouTube URL. Please enter a valid YouTube video URL."
    return render(request, 'index.html', {'error_message': error_message})


def downloaded(request):
    return render(request, 'Downloaded.html')