#!/usr/bin/env python3
import asyncio
from typing import Optional

import aiomysql

from nicegui import events, ui

# Database configuration
db_config = {
    'host': 'localhost',
    'port': 3306,  # Change to your MySQL port if different
    'user': 'root',
    'password': '',
    'db': 'project',
    'autocommit': True,
}

running_query: Optional[asyncio.Task] = None

async def search(e: events.ValueChangeEventArguments) -> None:
    global running_query
    if running_query:
        running_query.cancel()

    # Connect to the MySQL database
    async with aiomysql.create_pool(**db_config) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                # Execute a MySQL query to search for cocktails
                query = f"SELECT title, body, author FROM blog WHERE title LIKE '%{e.value}%'"
                await cursor.execute(query)

                for blog in await cursor.fetchall():
                    with ui.card().classes('m-1 justify-center'):
                        ui.label(blog['title'])
                        ui.label(blog['body'])
                        ui.label(blog['author'])

    running_query = None


search_field = ui.input(on_change=search) \
    .props('autofocus outlined rounded item-aligned input-class="ml-3"') \
    .classes('w-96 self-center mt-24 transition-all')

ui.run()