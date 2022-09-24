from aiowowapi import API
import pytest
import asyncio


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


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
