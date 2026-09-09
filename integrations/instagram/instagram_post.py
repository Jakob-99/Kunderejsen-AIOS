"""Publish an image post to an Instagram Business account via the Meta Graph API.

Usage:
    python instagram_post.py --image-url "https://example.com/photo.jpg" --caption "Hello!"

The image must already be hosted at a public URL — Meta fetches it from there.
"""

import argparse
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

GRAPH_API_VERSION = "v21.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"
POLL_INTERVAL_SECONDS = 2
MAX_POLL_ATTEMPTS = 30


def create_media_container(ig_user_id: str, access_token: str, image_url: str, caption: str) -> str:
    response = requests.post(
        f"{GRAPH_API_BASE}/{ig_user_id}/media",
        data={"image_url": image_url, "caption": caption, "access_token": access_token},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["id"]


def wait_until_ready(container_id: str, access_token: str) -> None:
    for _ in range(MAX_POLL_ATTEMPTS):
        response = requests.get(
            f"{GRAPH_API_BASE}/{container_id}",
            params={"fields": "status_code", "access_token": access_token},
            timeout=30,
        )
        response.raise_for_status()
        status = response.json()["status_code"]
        if status == "FINISHED":
            return
        if status == "ERROR":
            raise RuntimeError(f"Media container {container_id} failed to process")
        time.sleep(POLL_INTERVAL_SECONDS)
    raise TimeoutError(f"Media container {container_id} did not finish processing in time")


def publish_media(ig_user_id: str, access_token: str, container_id: str) -> str:
    response = requests.post(
        f"{GRAPH_API_BASE}/{ig_user_id}/media_publish",
        data={"creation_id": container_id, "access_token": access_token},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["id"]


def post_image(ig_user_id: str, access_token: str, image_url: str, caption: str) -> str:
    container_id = create_media_container(ig_user_id, access_token, image_url, caption)
    wait_until_ready(container_id, access_token)
    return publish_media(ig_user_id, access_token, container_id)


def main() -> None:
    parser = argparse.ArgumentParser(description="Post an image to Instagram")
    parser.add_argument("--image-url", required=True, help="Public URL of the image to post")
    parser.add_argument("--caption", default="", help="Caption text for the post")
    args = parser.parse_args()

    ig_user_id = os.environ["IG_USER_ID"]
    access_token = os.environ["IG_ACCESS_TOKEN"]

    media_id = post_image(ig_user_id, access_token, args.image_url, args.caption)
    print(f"Published post: {media_id}")


if __name__ == "__main__":
    main()
