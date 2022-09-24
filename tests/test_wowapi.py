from aiowowapi import WowApi
import pytest
import asyncio


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_parse_armory_link() -> None:
    assert await WowApi.parse_armory_link(
        'https://worldofwarcraft.com/en-us/character/us/illidan/adalyia'
    ) == {
               'name': 'adalyia',
               'realm': 'illidan',
               'region': 'us'
           }
    assert await WowApi.parse_armory_link(
        'https://worldofwarcraft.com/en-us/character/us/illidan/emilým'
    ) == {
               'name': 'emilým',
               'realm': 'illidan',
               'region': 'us'
           }


@pytest.mark.asyncio
async def test_format_wow_gold() -> None:
    assert await WowApi.format_wow_gold(9999999) == '999g 99s 99c'
    assert await WowApi.format_wow_gold(9999998) == '999g 99s 98c'
    assert await WowApi.format_wow_gold(8999999) == '899g 99s 99c'
