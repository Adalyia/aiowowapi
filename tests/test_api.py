from aiowowapi import API
import pytest


@pytest.mark.asyncio
async def test_get_resource():
    client: API = API("<client_id>", "<client_secret>", "us")
    params: dict = {
        "region": "us",
        "locale": "en"
    }
    assert isinstance(
        await client.get_resource("https://raider.io{api_endpoint}", "/api/v1/mythic-plus/affixes", params),
        dict
    )
