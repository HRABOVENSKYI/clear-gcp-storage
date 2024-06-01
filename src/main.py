import os
from concurrent.futures import ThreadPoolExecutor

import dotenv
from google.cloud import storage

from src.logger import logger


def delete_obj(obj):
    try:
        logger.info(f'Deleting {obj.name}...')
        obj.delete()
    except Exception as e:
        logger.error(f'Failed to delete {obj.name}: {e}')


if __name__ == '__main__':
    dotenv.load_dotenv()
    bucket_name = os.getenv("BUCKET_NAME")
    folder_path = os.getenv("FOLDER_PATH")

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_path)

    pool = ThreadPoolExecutor(max_workers=100)
    threads = []
    for blob in blobs:
        thread = pool.submit(delete_obj, blob)
        threads.append(thread)
    for thread in threads:
        thread.result()
    logger.info(f'All objects in folder "{folder_path}" have been deleted.')
