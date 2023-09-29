#!/usr/bin/env python3
"""This is just a simple authentication example.

Please see the `OAuth2 example at FastAPI <https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/>`_  or
use the great `Authlib package <https://docs.authlib.org/en/v0.13/client/starlette.html#using-fastapi>`_ to implement a classing real authentication system.
Here we just demonstrate the NiceGUI integration.
"""
from typing import Optional

from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

import nicegui.globals
from nicegui import app, ui, events
import aiomysql
import asyncio

import mysql.connector

grid = ui.grid()


# Function to fetch users to be able to log in
def db():
    # Connect to database
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='project'
    )

    # Create a cursor object to interact with the database
    cursor = cnx.cursor()

    # Execute an SQL query to fetch data
    query = "SELECT username, password FROM users"
    cursor.execute(query)

    # Fetch the column names (assuming they are in the same order as the data)
    column_names = [desc[0] for desc in cursor.description]

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Create a dictionary to store the data
    db.user_data = {}

    # Populate the dictionary with username as the key and password as the value
    for row in rows:
        username, password = row
        db.user_data[username] = password

    cursor.close()
    cnx.close()


# Function to create new blog
def blog_bd(title, body, author):
    # Connect to database
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='project'
    )

    # Create a cursor object to interact with the database
    cursor = cnx.cursor()

    # Execute an SQL query to fetch data
    query = "INSERT INTO blog (title, body, author) VALUES (%s, %s, %s)"
    val = (title, body, author)
    cursor.execute(query, val)

    cnx.commit()

    cursor.close()
    cnx.close()

    ui.notify("Data Successfully Inserted!")


def course_db(title, body, author, video):
    # Connect to database
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='project'
    )

    # Create a cursor object to interact with the database
    cursor = cnx.cursor()

    # Execute an SQL query to fetch data
    query = "INSERT INTO course (title, description, author, video) VALUES (%s, %s, %s, %s)"
    val = (title, body, author, video)

    cursor.execute(query, val)

    cnx.commit()

    cursor.close()
    cnx.close()

    ui.notify("Data Successfully Inserted!")


def history(title, author):
    # Connect to database
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='project'
    )

    # Create a cursor object to interact with the database
    cursor = cnx.cursor()

    # Execute an SQL query to fetch data
    query = "INSERT INTO history (title, author) VALUES (%s, %s)"
    data = (title, author)

    cursor.execute(query, data)

    cnx.commit()

    cursor.close()
    cnx.close()


# Define a closure to capture title and author
def on_expand_click(title, author):
    def print_info():
        # Connect to database
        cnx = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='project'
        )

        # Create a cursor object to interact with the database
        cursor = cnx.cursor()

        print(title, author)
        # Execute an SQL query to fetch data
        query = "INSERT INTO history (title, author) VALUES (%s, %s)"
        data = (title, author)

        cursor.execute(query, data)

        cnx.commit()

        cursor.close()
        cnx.close()

    return print_info


def fetch_blog_data():
    # Connect to database
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='project'
    )

    # Create a cursor object to interact with the database
    cursor = cnx.cursor()

    # Execute an SQL query to fetch data
    query = "SELECT title, body, author FROM blog ORDER BY dateCreated DESC"
    cursor.execute(query)

    # Fetch all the rows as a list of tuples
    data = cursor.fetchall()

    for record in data:
        title, body, author = record

        with ui.dialog() as blog_dialog, ui.card().classes('w-full'):
            with ui.row().classes('w-full justify-center font-bold text-lg'):
                ui.label(title)
            with ui.row().classes('w-full justify-center'):
                ui.label(author)
            with ui.scroll_area():
                with ui.row().classes('text-justify'):
                    ui.label(body)
            with ui.row().classes('w-full'):
                ui.separator()
                ui.button(text='Close', on_click=blog_dialog.close)

        with ui.card().classes('m-10 justify-center'):
            with ui.row().classes('w-full justify-center font-bold text-lg'):
                ui.label(title)
            with ui.row().classes('w-full justify-center'):
                ui.label(author)
            with ui.scroll_area():
                with ui.row().classes('text-justify'):
                    ui.label(body)
            with ui.row().classes('w-full text-left'):
                ui.separator()
                ui.button(text='Expand Blog', on_click=blog_dialog.open).on('click').on('click',
                                                                                        on_expand_click(title, author))

    cursor.close()
    cnx.close()


def activities():
    # Connect to database
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='project'
    )

    # Create a cursor object to interact with the database
    cursor = cnx.cursor()

    # Execute an SQL query to fetch data
    query = "SELECT title, author FROM history ORDER BY dateCreated DESC"
    cursor.execute(query)

    # Fetch all the rows as a list of tuples
    data = cursor.fetchall()[:30]

    with ui.grid(columns=3).classes('m-5'):
        for record in data:
            title, author = record
            with ui.card():
                ui.label('Title: ' + title).classes('font-bold')
                ui.label('Author: ' + author)
                ui.separator()
                ui.button('View', on_click=lambda: ui.open(learner_page))

    cursor.close()
    cnx.close()


unrestricted_page_routes = {'/login'}


class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if request.url.path in nicegui.globals.page_routes.values() and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
        return await call_next(request)


app.add_middleware(AuthMiddleware)


@ui.page('/')
def main_page() -> None:
    # MAIN CONTENT
    # Blogs and Courses Tab
    with ui.tabs().classes('w-full') as tabs:
        blog_tab = ui.tab('Blogs')
        course_tab = ui.tab('Courses')
    with ui.tab_panels(tabs, value=blog_tab).classes('w-full'):
        with ui.tab_panel(blog_tab):
            # Populate page with texts from database
            fetch_blog_data()
        with ui.tab_panel(course_tab):
            with ui.card():
                with ui.row().classes('w-full justify-left font-bold text-lg'):
                    ui.video('vid1.mp4').classes('aspect-auto')
                    ui.label('What is Lorem Ipsum?')
                with ui.row().classes('w-full justify-left'):
                    ui.label('user1')
                    ui.label(
                        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('justify-between'):
        with ui.grid(columns=2).classes('items-left'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').tooltip('Menu')
            ui.button(text='Creator Mode', on_click=lambda: ui.open(main_page)).props('flat color=white').tooltip(
                'Home')

        with ui.grid(columns=2).classes('items-right'):
            ui.switch(on_change=lambda: ui.open(learner_page)).classes('item-right').tooltip('Toggled to Creator Mode')
            with ui.button(icon='account_circle').props('flat color=white').tooltip('Account'):
                with ui.menu():
                    ui.menu_item(f'Logged in as: {app.storage.user["username"]}')
                    ui.separator()
                    ui.menu_item('Logout', lambda: (app.storage.user.clear(), ui.open('/login')))

    # LEFT DRAWER
    with ui.left_drawer(fixed=True).style('background-color: #d7e3f4').props('bordered') as left_drawer:
        with ui.grid(rows=2):
            ui.button('Create a Course', on_click=lambda: ui.open(course))
            ui.button('Write a Blog', on_click=lambda: ui.open(blog))


# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'project',
}

running_query: Optional[asyncio.Task] = None


@ui.page('/subpage')
def learner_page() -> None:
    with ui.tabs().classes('w-full') as tabs:
        forYou_tab = ui.tab('For You')
        activities_tab = ui.tab('Recent Activities')

    with ui.tab_panels(tabs, value=forYou_tab).classes('w-full'):
        with ui.tab_panel(forYou_tab):
            async def search(e: events.ValueChangeEventArguments) -> None:
                global running_query
                if running_query:
                    running_query.cancel()

                grid.clear()

                # Connect to the MySQL database
                async with aiomysql.create_pool(**db_config) as pool:
                    async with pool.acquire() as conn:
                        async with conn.cursor(aiomysql.DictCursor) as cursor:
                            text = e.value
                            query = f"SELECT title, body, author FROM blog WHERE title LIKE '%{text}%' OR author LIKE '%{text}%'"
                            await cursor.execute(query)

                            if len(e.value) == 0:
                                grid.clear()
                                return

                            elif len(e.value) >= 1:
                                with grid:
                                    with ui.card().classes('m-1 justify-center'):
                                        with ui.row().classes('w-full justify-center font-bold text-lg'):
                                            ui.label(f'Search Results for "{e.value}"')
                                    for blog in await cursor.fetchall():
                                        with ui.dialog() as blog_dialog, ui.card().classes('w-full'):
                                            with ui.row().classes('w-full justify-center font-bold text-lg'):
                                                ui.label(blog['title'])
                                            with ui.row().classes('w-full justify-center'):
                                                ui.label(blog['author'])
                                            with ui.scroll_area():
                                                with ui.row().classes('text-justify'):
                                                    ui.label(blog['body'])
                                            with ui.row().classes('w-full'):
                                                ui.separator()
                                                ui.button(text='Close', on_click=blog_dialog.close)

                                        with ui.card().classes('m-1 justify-center'):
                                            with ui.row().classes('w-full justify-center font-bold text-lg'):
                                                a = ui.label(blog['title'])
                                            with ui.row().classes('w-full justify-center'):
                                                ui.label(blog['author'])
                                            with ui.scroll_area():
                                                with ui.row().classes('w-full justify-center'):
                                                    ui.label(blog['body'])
                                            with ui.row().classes('w-full text-left'):
                                                ui.separator()
                                                ui.button(text='Expand Blog', on_click=blog_dialog.open).on('click',
                                                                                                            on_expand_click(
                                                                                                                blog[
                                                                                                                    'title'],
                                                                                                                blog[
                                                                                                                    'author']))
                running_query = None

            search_field = ui.input(placeholder='Search for title or author...', on_change=search) \
                .props('autofocus outlined rounded item-aligned input-class="ml-3"') \
                .classes('self-center transition-all')
            grid = ui.grid()

            if len(search_field.value) == 0:
                ui.separator().classes('mt-10 h-50')
                fetch_blog_data()

        with ui.tab_panel(activities_tab):
            activities()

    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('justify-between'):
        with ui.grid(columns=2).classes('items-left'):
            ui.button(text='Learner Mode', on_click=lambda: ui.open(learner_page)).props('flat color=white').tooltip(
                'Home')

        with ui.grid(columns=2).classes('items-right'):
            ui.switch(value=True, on_change=lambda: ui.open(main_page)).classes('item-right').tooltip(
                'Toggled to Learner Mode')
            with ui.button(icon='account_circle').props('flat color=white').tooltip('Account'):
                with ui.menu():
                    ui.menu_item(f'Logged in as: {app.storage.user["username"]}')
                    ui.separator()
                    ui.menu_item('Logout', lambda: (app.storage.user.clear(), ui.open('/login')))


@ui.page('/blog')
def blog() -> None:
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full justify-center font-bold text-lg'):
            ui.label('Create a Blog')
            ui.separator()
        with ui.grid().classes('w-full justify-left'):
            blog_title = ui.input(label='Title')
            blog_body = ui.textarea(label='Body').props('clearable')

            author = {app.storage.user["username"]}
            author = str(author).replace('{', '').replace('}', '').replace("'", '')

            ui.button('Publish', on_click=lambda: blog_bd(blog_title.value, blog_body.value, author))

    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('justify-between'):
        with ui.grid(columns=2).classes('items-left'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').tooltip('Menu')
            ui.button(text='Creator Mode', on_click=lambda: ui.open(main_page)).props('flat color=white').tooltip(
                'Home')

        with ui.grid(columns=2).classes('items-right'):
            ui.switch(on_change=lambda: ui.open(learner_page)).classes('item-right').tooltip('Toggled to Creator Mode')
            with ui.button(icon='account_circle').props('flat color=white').tooltip('Account'):
                with ui.menu():
                    ui.menu_item(f'Logged in as: {app.storage.user["username"]}')
                    ui.separator()
                    ui.menu_item('Logout', lambda: (app.storage.user.clear(), ui.open('/login')))

        # LEFT DRAWER
        with ui.left_drawer(fixed=True).style('background-color: #d7e3f4').props('bordered') as left_drawer:
            with ui.grid(rows=2):
                ui.button('Create a Course', on_click=lambda: ui.open(course))
                ui.button('Write a Blog', on_click=lambda: ui.open(blog))


@ui.page('/course')
def course() -> None:
    with ui.card().classes('w-full'):
        with ui.row().classes('w-full justify-center font-bold text-lg'):
            ui.label('Create a Course')
            ui.separator()
        with ui.grid().classes('w-full justify-left'):
            course_title = ui.input(label='Title')
            course_video_desc = ui.input(label='Video Description')
            course_video = ui.upload(auto_upload=True, max_files=1,
                                     on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('w-full')

            author = {app.storage.user["username"]}
            author = str(author).replace('{', '').replace('}', '').replace("'", '')
            ui.button('Publish',
                      on_click=lambda: course_db(course_title.value, course_video_desc.value, author, course_video))

    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('justify-between'):
        with ui.grid(columns=2).classes('items-left'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').tooltip('Menu')
            ui.button(text='Creator Mode', on_click=lambda: ui.open(main_page)).props('flat color=white').tooltip(
                'Home')

        with ui.grid(columns=2).classes('items-right'):
            ui.switch(on_change=lambda: ui.open(learner_page)).classes('item-right').tooltip('Toggled to Creator Mode')
            with ui.button(icon='account_circle').props('flat color=white').tooltip('Account'):
                with ui.menu():
                    ui.menu_item(f'Logged in as: {app.storage.user["username"]}')
                    ui.separator()
                    ui.menu_item('Logout', lambda: (app.storage.user.clear(), ui.open('/login')))

        # LEFT DRAWER
        with ui.left_drawer(fixed=True).style('background-color: #d7e3f4').props('bordered') as left_drawer:
            with ui.grid(rows=2):
                ui.button('Create a Course', on_click=lambda: ui.open(course))
                ui.button('Write a Blog', on_click=lambda: ui.open(blog))


@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        db()
        if db.user_data.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.open(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)


ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED', title='Project', on_air=True)