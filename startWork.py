import webbrowser
import subprocess
import time

def open_apps_and_urls():
    # Define the URLs to be opened in Google Chrome
    urls = [
        'https://gitlab.com/dashboard/merge_requests?assignee_username=petervillaroman',
        'https://clickup.com',
        'https://chat.openai.com',
        'https://bit.ly/clockNellis'
    ]

    # Open the URLs in the default browser (in separate tabs)
    first_url = urls.pop(0)
    webbrowser.open_new(first_url)
    time.sleep(1)  # to make sure the first browser window has time to open
    for url in urls:
        webbrowser.open_new_tab(url)
        
    applications = [ 
        'Slack', 
        'GitHub Desktop',
    ]

    # Define the directories to be opened in Visual Studio Code
    directories = [
        # '/users/Peter/documents/nellis-files/buyer', disabled for now bc I'm not working on buyer atm
        '/users/Peter/documents/nellis-files/cargo',
        '/users/Peter/documents/nellis-files/cargo-api',
        # Add more directories as needed
    ]


    for application in applications:
        subprocess.Popen(['open', '-na', application])

    # Open the directories in new Visual Studio Code windows
    for directory in directories:
        subprocess.Popen(['open', '-na', 'Visual Studio Code', '--args', directory])




# Call the function to open Google Chrome with the specified URLs and applications
open_apps_and_urls()
