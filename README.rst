.. image:: https://img.shields.io/pypi/v/aiowowapi.svg
   :target: https://pypi.python.org/pypi/aiowowapi
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/aiowowapi.svg
   :target: https://pypi.python.org/pypi/aiowowapi
   :alt: PyPI supported Python versions

aiowowapi docs
=====================================

An asynchronous client library for interacting with the World of Warcraft API endpoints using the ``async`` / ``await`` syntax.


Installing
-----------
.. code:: sh

    # Linux/OSX
    python3 -m pip install -U aiowowapi

    # Windows
    python -m pip install -U aiowowapi


Current Features
---------------------
* Retail Game Data API Support
* Retail Profile API Support
* Rate limiting
* Request retries
* QoL WoW-Specific functions (Money -> Gold/Silver/Copper, Armoury link parser, etc)

TODO
-----
* Add support for World of Warcraft: Classic/TBC API endpoints
* Add caching for certain requests
* Less janky error handling

Requirements
-------------
* `aiohttp <https://docs.aiohttp.org/en/stable/>`_
* Python 3.8+

Example
--------
.. code-block:: python

    from aiowowapi import WowApi

    async def main():
        # Create WoWApi client object
        Client = WowApi('<CLIENT_ID>','<CLIENT_SECRET>', 'us')
        
        # Retrieve user's Mythic+ Profile
        data = await Client.Retail.Profile.getCharMythicKeystoneProfileIndex('adalyia', 'illidan')
        
        # Print user's Mythic+ Rating
        print(data['current_mythic_rating']['rating'])


    asyncio.get_event_loop().run_until_complete(main())

Links
------
* `aiowowapi's Documentation <https://docs.adalyia.com/wowapi>`_
* `Blizzard's API Documentation <https://develop.battle.net/documentation>`_
* `Register a Blizzard API Client <https://develop.battle.net/access/clients>`_
* `Blizzard's API Forums <https://us.forums.blizzard.com/en/blizzard/c/api-discussion/18>`_


IMPORTANT
----------
This project is not affiliated with or endorsed by `Blizzard Entertainment <https://www.blizzard.com/>`_ & all data is retrieved from official Blizzard / World of Warcraft APIs. `Terms found here <https://www.blizzard.com/en-us/legal/a2989b50-5f16-43b1-abec-2ae17cc09dd6/blizzard-developer-api-terms-of-use>`_. Additionally this project was created primarily for use with Discord Bots & other async applications with inspiration from `this project <https://github.com/lockwooddev/python-wowapi>`_ by `lockwooddev <https://github.com/lockwooddev/>`_.
