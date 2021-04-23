"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import os
import aiohttp
import csv
from entity import Entity


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
    async def download_to_file(cls, url, file_path):
        async with aiohttp.ClientSession() as session:
            print('Downloading data to file: ' + str(file_path))
            content_as_text = await cls.fetch_data_as_text(session, url)
            text_file = open(file_path, 'w')
            text_file.write(content_as_text)
            text_file.close()

    @classmethod
    async def fetch_data_as_text(cls, session, url):
        async with session.get(url) as response:
            return await response.text()

    @classmethod
    def load_entities(cls, file_path):
        """
        Load all entities from the given csv file.
        We always load all attributes we find in the file.
        We return a list of entity objects.
        """

        print('Loading entities from file: ' + str(file_path))
        entities = []
        with open(file_path) as file:
            print('Loaded file to extract entities...')
            reader = csv.reader(file)

            # read first row to get attributes
            attributes = next(reader)
            print('Attributes: ' + str(attributes))

            # read the data and add entities
            index = 0
            for row in reader:
                entity = Entity(index)
                for i in range(0, len(attributes)):
                    entity.attributes[attributes[i]] = row[i]
                entities.append(entity)
                index += 1

        print('Retrieved entities: ' + str(len(entities)))
        return entities
