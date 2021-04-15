"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import os
import aiohttp


class FileService:
    """
    A service class for all kind of file access like downloads,
    file deletion, folder deletion, ...
    """

    @classmethod
    def delete_if_exist(cls, *file_paths):
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)

    @classmethod
    def create_folder_if_not_exist(cls, folder_path):
        os.makedirs(folder_path, exist_ok=True)

    @classmethod
    async def fetch_data_as_text(cls, session, url):
        async with session.get(url) as response:
            return await response.text()

    @classmethod
    async def download_to_file(cls, url, file_path):
        async with aiohttp.ClientSession() as session:
            content_as_text = await cls.fetch_data_as_text(session, url)
            text_file = open(file_path, 'w')
            text_file.write(content_as_text)
            text_file.close()