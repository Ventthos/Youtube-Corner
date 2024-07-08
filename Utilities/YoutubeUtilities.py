import eyed3
import pytube
from moviepy.editor import *
import os
import requests


class YoutubeUtilities:
    @staticmethod
    def downloadMP4File(link: str, directory: str, onlyAudio: bool):
        obj = pytube.YouTube(link)
        if onlyAudio:
            direccionMP4 = obj.streams.get_audio_only().download(output_path=directory)
        else:
            direccionMP4 = obj.streams.get_highest_resolution().download(output_path=directory)
        return direccionMP4

    @staticmethod
    def MP4ToMP3(mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()
        print("termine el mp4")
        os.remove(mp4)
        return mp3

    @staticmethod
    def changeAtributesToMP3(mp3, title, artist, album, img_route) -> None:
        audio = eyed3.load(mp3)
        audio.initTag()
        audio.tag.title = u"{}".format(title)
        audio.tag.artist = u"{}".format(artist)
        audio.tag.album = u"{}".format(album)
        audio.tag.images.set(3, open(f"{img_route}", 'rb').read(), 'image/png')
        audio.tag.save(version=eyed3.id3.ID3_V2_3)

    @staticmethod
    def getVideoInfo(link):
        obj = pytube.YouTube(link)

        return obj.title, obj.author, obj.length

    @staticmethod
    def download_thumb(link, destinationRoute):
        obj = pytube.YouTube(link)
        if "sddefault.jpg" in obj.thumbnail_url or "hq720.jpg" in obj.thumbnail_url:
            if "sddefault.jpg" in obj.thumbnail_url:
                print("tenia default")
                splitter = "sddefault.jpg"
            else:
                splitter = "hq720.jpg"
            rutaModificada = obj.thumbnail_url.split(splitter)[0]
            rutaModificada = f"{rutaModificada}hq720.jpg"
        else:
            rutaModificada = obj.thumbnail_url

        with open(destinationRoute, 'wb') as handle:
            response = requests.get(rutaModificada, stream=True)
            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
