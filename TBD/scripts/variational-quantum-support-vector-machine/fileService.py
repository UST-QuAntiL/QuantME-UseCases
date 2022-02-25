import aiohttp


class FileService:

    @classmethod
    async def fetch_data_as_text(cls, session, url):
        async with session.get(url) as response:
            if response.content_type == 'application/python-pickle':
                return await response.content.read()
            return await response.text()

    @classmethod
    async def download_to_file(cls, url, file_path):
        async with aiohttp.ClientSession() as session:
            file = open(file_path, "w")
            content_as_text = await cls.fetch_data_as_text(session, url)
            file.write(content_as_text)
