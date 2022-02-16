import os
from typing import Tuple

from PIL import Image  # type: ignore

from tasks import celery


@celery.app.task
def resize_image_at_path(path: str, output_size: Tuple[int, int]) -> bool:
    if not os.path.isfile(path):
        return False
    image = Image.open(path)
    image.thumbnail(output_size)
    image.save(path)
    return True
