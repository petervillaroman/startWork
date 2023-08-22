import webbrowser
import subprocess
import time
import questionary

# Define the user name to be used in the directories
userName = 'Peter'

def open_apps_and_urls():
    # Define the URLs to be opened in Google Chrome
    urls = [
        'https://gitlab.com/dashboard/merge_requests?assignee_username=petervillaroman',
        'https://app.clickup.com/?_ga=2.67863057.140528526.1661975994-1432757507.1661975994&_gl=1*1t9phd1*_gcl_au*MTY3NzI1Njk0Ni4xNjg1NTY0Mjc1',
        'https://chat.openai.com',
        'https://bit.ly/clockNellis'
    ]
    # Defining the applications to be opened
    
    applications = [ 
        'Slack', 
        'GitHub Desktop',
    ]

    # Define the directories to be opened in Visual Studio Code
    directories = [
        # '/users/Peter/documents/nellis-files/buyer', disabled for now bc I'm not working on buyer atm
        f'/users/{userName}/documents/nellis-files/cargo',
        f'/users/{userName}/documents/nellis-files/cargo-api',
    ]

    ide_choice = questionary.select(
        "Which IDE would you like to use?",
        choices=[
            "VSCode",
            "IntelliJ"
        ]
    ).ask()

        
    # Open the VSCode directories
    for directory in directories:
        if ide_choice == "IntelliJ":
            subprocess.Popen(['idea', directory])
        else:
            subprocess.Popen(['open', '-na', 'Visual Studio Code', '--args', directory])

    # Open the URLs in the default browser (in separate tabs)
    first_url = urls.pop(0)
    webbrowser.open_new(first_url)
    time.sleep(1)  # to make sure the first browser window has time to open
    for url in urls:
        webbrowser.open_new_tab(url)   

    # Open the applications
    for application in applications:
        subprocess.Popen(['open', '-na', application])



# Call the function to open Google Chrome with the specified URLs and applications
open_apps_and_urls()
