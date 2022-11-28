import instagrapi.exceptions
import requests.exceptions
from instagrapi import Client

INSTAGRAM_USERNAME = "your_instagram_username"
INSTAGRAM_PASSWORD = "your_instagram_password"
INSTAGRAM_2FA_CODE = "2fa_code"


def download_video() -> None:
    link = input("Link video:")
    try:
        media_pk = cl.media_pk_from_url(link)
        media_path = cl.video_download(media_pk)
        print(media_path)
        print(f"Media saved in:{media_path}")
    except instagrapi.exceptions.MediaNotFound:
        print(f"Media not found. Check url:\"{link}\"")


def get_info_username() -> None:
    username = input("Username:")
    try:
        user = cl.user_info_by_username(username)
        print(f"Fulla name:{user.full_name}\n"
              f"Follower:{user.follower_count}\n"
              f"Following:{user.following_count}\n"
              f"Total posts:{user.media_count}\n"
              f"Biography:{user.biography}"
              f"Link profile pic:{user.profile_pic_url_hd}")
    except requests.exceptions.HTTPError or \
           instagrapi.exceptions.ClientNotFoundError or \
           instagrapi.exceptions.UserNotFound:
        print(f"User doesn't exist. Check username: \"{username}\"")


def engine():
    menu = True
    while menu:
        choise = int(input("1- Get info by username\n"
                           "2- Download video\n"
                           "0- Exit\n\n"
                           "Choise:"))
        if choise == 1:
            get_info_username()
        elif choise == 2:
            download_video()
        else:
            menu = False


print("Starting")
cl = Client()
cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, verification_code=INSTAGRAM_2FA_CODE)
engine()