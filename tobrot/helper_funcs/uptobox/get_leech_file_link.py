import aiohttp
import json


async def upto_box_get_file_link(token: str, ubid: str):
    async with aiohttp.ClientSession() as session:
        api_url = f"https://uptobox.com/api/link?token={token}&file_code={ubid}"
        one_response = await session.get(api_url)
        response = json.loads(await one_response.text())
        return response
