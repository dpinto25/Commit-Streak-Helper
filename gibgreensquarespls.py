# Hey everyone! As I'm learning python, and I forgot to do a commit yesterday breaking my green square streak, I decided to solve this problem! 

# This is a simple script that will take a file, copy it a few times and commit the changes to github.

# In a perfect world, you can even run this on any server (No I'm not trying to steal your damn data, just read the source code)
# you alredy have in the cloud and you won't even need to have your computer on to keep the green squares coming.

# Feel free to use it, please no repost as if you made it :(

# OG Author: github.com/dpinto25

import subprocess
import shutil
import os
import random
import string
import schedule
import time

# Configuration
FILE_TO_COPY = 'copiablefile.py' # pretty self explanatory name no? jesus
DESTINATION_FOLDER = './' # self explanatory lol
NUMBER_OF_COPIES = 50 # 50 copies of the file, cuz why not? greener squares gonna green
COMMIT_MESSAGE = 'update' # self explanatory lol
LOG_FILE = 'log.txt' # self explanatory lol
REMOTE_NAME = 'origin'  # self explanatory lol
REMOTE_URL = 'https://github.com/YOUR_GITHUB/YOUR_REPO.git' # if your posting an issue and the issue is because you didn't change this line, you're getting blocked.
TIMER = 12 # do the shit every 12 hours 

# generate a random file name
def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase, k=20)) + '.txt'

# delete half of the .txt files if thers too many
def check_if_theres_more_than_105_and_if_so_just_delete_half_of_them_btw_do_you_like_this_function_name_lol(log):
    txt_files = [f for f in os.listdir(DESTINATION_FOLDER) if f.endswith('.txt') and f != 'log.txt'] # thanks chatgpt for fixing this line lol
    
    if len(txt_files) > 105:
        files_to_delete = len(txt_files) // 2
        log.write(f'Deleting half the txt files files.\n')
        print('Deleting half the txt files files.\n')
        
        for i in range(files_to_delete):
            file_to_delete = os.path.join(DESTINATION_FOLDER, txt_files[i])
            try:
                os.remove(file_to_delete)
            except Exception as e:
                log.write(f'Error removing file {file_to_delete}: {e}\n')
                print(f'Error removing file {file_to_delete}: {e}\n')

# copy the file NUMBER_OF_COPIES times
def copy_file(log):
    for _ in range(NUMBER_OF_COPIES):
        dest_file = os.path.join(DESTINATION_FOLDER, generate_random_filename())
        try:
            shutil.copy(FILE_TO_COPY, dest_file)
            log.write(f'Files copied successfully.\n')
            print(f'Files copied successfully.\n')
        except Exception as e:
            log.write(f'Error copying file: {e}\n')
            print(f'Error copying file: {e}\n')

# commit changes
def commit_togit(log):
    try:
        subprocess.run(['git', 'add', '.'], check=True, stdout=log, stderr=log) #leave logs here cuz if this shit goes wrong you won't know - same for lines below
        subprocess.run(['git', 'commit', '-m', COMMIT_MESSAGE], check=True, stdout=log, stderr=log)
        subprocess.run(['git', 'push', REMOTE_URL, 'main'], check=True, stdout=log, stderr=log)
        log.write('Changes committed and pushed to Git.\n')
        print('Changes committed and pushed to Git.\n')
    except subprocess.CalledProcessError as e:
        log.write(f'Error during Git operations: {e}\n')
        print(f'Error during Git operations: {e}\n')

# what do
def do_the_shit():
    with open(LOG_FILE, 'a') as log:  
        log.write('\nCopying files and comitting\n')
        check_if_theres_more_than_105_and_if_so_just_delete_half_of_them_btw_do_you_like_this_function_name_lol(log)
        copy_file(log)
        commit_togit(log)
        log.write('Completed.\n')
        print('Commit Completed')

#countdown timer
def countdown_timer(hours):
    for remaining in range(hours, 0, -1):
        print(f'{remaining} hours until the next commit.')
        time.sleep(3600) # goodnight mf

# main
def main():    schedule.every(TIMER).hours.do(do_the_shit)
    print('Changes commited and timer Started. 24 hours left for next commit')

    while True:
        schedule.run_pending()
        countdown_timer(TIMER)

if __name__ == "__main__":
    do_the_shit()  # remove to not do a commit on startup of the script
    main()
