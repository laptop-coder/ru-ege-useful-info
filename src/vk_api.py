import requests
import config


def wall_post(message: str):
    requests.post(
        "https://api.vk.ru/method/wall.post",
        headers={"Authorization": f"Bearer {config.VK_AUTH_TOKEN}"},
        data={
            "owner_id": config.GROUP_ID,
            "message": message,
            "from_group": "1",
            "signed": "0",
            "v": "5.199",
        },
    )
