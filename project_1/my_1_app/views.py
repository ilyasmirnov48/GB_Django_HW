from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My first app</title>
    </head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                color: #333;
            }

            p {
                color: #777;
            }
        </style>    
        <body>
            <h1>Welcome!</h1>
            
            <h2>Description</h2>
            
            <p>Cайт разработан в учебных целях, с использованием фреймворка Django.</p>
                   
            <footer>
                <div>
                    <p>All Rights Reserved.</p>
                </div>
            </footer>
        </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>About my</title>
    </head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                color: black;
            }

            p {
                color: #777;
            }
        </style>
        <body>

            <h1>Hello!</h1>
            
            <p>Меня зовут Илья, я разработал этот сайт.</p>
                             
            <footer>
                <div>
                    <p>All Rights Reserved.</p>
                </div>
            </footer>
        </body>
    </html>
"""
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)
