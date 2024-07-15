# import os
# import subprocess
# import time
# import logging
# import threading
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# # Global variables
# stop_execution = False
# script_status = {}
# script_output = {}
# SCRIPTS_DIRECTORY = r'C:\Users\G6\PycharmProjects\WebScrappingWebPage'
#
#
# def run_script(script_name):
#     global stop_execution, script_status, script_output
#     script_path = os.path.join(SCRIPTS_DIRECTORY, script_name)
#     script_status[script_name] = 'Running'
#     url_count = 0
#
#     try:
#         logging.debug(f"Starting script: {script_name}")
#         process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                    universal_newlines=True)
#
#         while True:
#             if stop_execution or script_status[script_name] == 'Stopping':
#                 logging.debug(f"Stopping script: {script_name}")
#                 process.terminate()
#                 process.wait(timeout=5)
#                 if process.poll() is None:
#                     process.kill()
#                 script_status[script_name] = f'Stopped (Data scraped: {url_count})'
#                 break
#
#             try:
#                 output = process.stdout.readline()
#                 if output == '' and process.poll() is not None:
#                     break
#                 if output:
#                     logging.debug(f'Script {script_name} output: {output.strip()}')
#                     script_output[script_name] = script_output.get(script_name, '') + output
#                     if output.strip().startswith('https://'):  # Count URLs
#                         url_count += 1
#                         script_status[script_name] = f'Running)'
#             except subprocess.TimeoutExpired:
#                 continue
#
#         stdout, stderr = process.communicate()
#         script_output[script_name] = script_output.get(script_name, '') + stdout + stderr
#         rc = process.poll()
#
#         if script_status[script_name] != f'Stopped':
#             script_status[script_name] = f'Completed' if rc == 0 else f'Error: {stderr.strip()}'
#             time.sleep(5)
#
#     except Exception as e:
#         logging.error(f"Exception running script {script_name}: {e}")
#         script_status[script_name] = f'Error: {str(e)}'
#     finally:
#         if script_name in script_status and 'Running' in script_status[script_name]:
#             script_status[script_name] = f'Completed (Data scraped: {url_count})'
#
#
# def run_all_scripts(scripts):
#     for script_name in scripts:
#         run_script(script_name)
#         print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
#         time.sleep(5)
#
# def run_export_csv(scripts):
#     for script_name in scripts:
#         run_script(script_name)
#         print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
#
#
# def run_scripts_in_threads(scripts):
#     threads = []
#     for script_name in scripts:
#         thread = threading.Thread(target=run_script, args=(script_name,))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#
#     parallel_scripts = ['Flinn_vs_Fisher.py',]
#
#     all_scripts = [
#         'Fisher_Consolidate_matches_All_Products.py',
#         'Merge_CSV.py',
#         'Cleaning_process.py',
#         'Overall_Compare_Script.py',
#         'Matched_push_script.py'
#     ]
#
#     run_scripts_in_threads(parallel_scripts)
#
#     run_all_scripts(all_scripts)

# import os
# import subprocess
# import time
# import logging
# import threading
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# # Global variables
# stop_execution = False
# script_status = {}
# script_output = {}
# SCRIPTS_DIRECTORY = r'C:\Users\G6\PycharmProjects\WebScrappingWebPage'
#
#
# def run_script(script_name):
#     global stop_execution, script_status, script_output
#     script_path = os.path.join(SCRIPTS_DIRECTORY, script_name)
#     script_status[script_name] = 'Running'
#     url_count = 0
#
#     try:
#         logging.debug(f"Starting script: {script_name}")
#         process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                    universal_newlines=True)
#
#         while True:
#             if stop_execution or script_status[script_name] == 'Stopping':
#                 logging.debug(f"Stopping script: {script_name}")
#                 process.terminate()
#                 process.wait(timeout=5)
#                 if process.poll() is None:
#                     process.kill()
#                 script_status[script_name] = f'Stopped (Data scraped: {url_count})'
#                 break
#
#             try:
#                 output = process.stdout.readline()
#                 if output == '' and process.poll() is not None:
#                     break
#                 if output:
#                     logging.debug(f'Script {script_name} output: {output.strip()}')
#                     script_output[script_name] = script_output.get(script_name, '') + output
#                     if output.strip().startswith('https://'):  # Count URLs
#                         url_count += 1
#                         script_status[script_name] = f'Running)'
#             except subprocess.TimeoutExpired:
#                 continue
#
#         stdout, stderr = process.communicate()
#         script_output[script_name] = script_output.get(script_name, '') + stdout + stderr
#         rc = process.poll()
#
#         if script_status[script_name] != f'Stopped':
#             script_status[script_name] = f'Completed' if rc == 0 else f'Error: {stderr.strip()}'
#             time.sleep(5)
#
#     except Exception as e:
#         logging.error(f"Exception running script {script_name}: {e}")
#         script_status[script_name] = f'Error: {str(e)}'
#     finally:
#         if script_name in script_status and 'Running' in script_status[script_name]:
#             script_status[script_name] = f'Completed (Data scraped: {url_count})'
#
#
# def run_all_scripts(scripts):
#     for script_name in scripts:
#         run_script(script_name)
#         print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
#         time.sleep(5)
#
# def run_export_csv(scripts):
#     for script_name in scripts:
#         run_script(script_name)
#         print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
#
#
# def run_scripts_in_threads(scripts):
#     threads = []
#     for script_name in scripts:
#         thread = threading.Thread(target=run_script, args=(script_name,))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#
#     # export_csv = ['export_csv.py']
#
#     parallel_scripts = [
#         'Flinn_vs_Frey.py',
#         'Flinn_vs_Nasco.py',
#         'Flinn_vs_Carolina.py',
#         'Flinn_vs_VWR.py',
#         'Flinn_vs_Wardsci.py'
#     ]
#
#     all_scripts = [
#
#         'Consolidate_matches_All_Products.py',
#         'Cleaning_process.py',
#         'Overall_Compare_Script.py',
#         'Matched_push_script.py'
#     ]
#
#     # run_export_csv(export_csv)
#
#     run_scripts_in_threads(parallel_scripts)
#
#     run_all_scripts(all_scripts)
#
#


import os
import subprocess
import time
import logging
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variables
stop_execution = False
script_status = {}
script_output = {}
SCRIPTS_DIRECTORY = r'C:\Users\G6\PycharmProjects\WebScrappingWebPage'

def run_script(script_name):
    global stop_execution, script_status, script_output
    script_path = os.path.join(SCRIPTS_DIRECTORY, script_name)
    script_status[script_name] = 'Running'
    url_count = 0

    try:
        logging.debug(f"Starting script: {script_name}")
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        while True:
            if stop_execution or script_status[script_name] == 'Stopping':
                logging.debug(f"Stopping script: {script_name}")
                process.terminate()
                process.wait(timeout=5)
                if process.poll() is None:
                    process.kill()
                script_status[script_name] = f'Stopped (Data scraped: {url_count})'
                break

            try:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    logging.debug(f'Script {script_name} output: {output.strip()}')
                    script_output[script_name] = script_output.get(script_name, '') + output
                    if output.strip().startswith('https://'):  # Count URLs
                        url_count += 1
                        script_status[script_name] = f'Running)'
            except subprocess.TimeoutExpired:
                continue

        stdout, stderr = process.communicate()
        script_output[script_name] = script_output.get(script_name, '') + stdout + stderr
        rc = process.poll()

        if script_status[script_name] != f'Stopped':
            script_status[script_name] = f'Completed' if rc == 0 else f'Error: {stderr.strip()}'
            time.sleep(5)

    except Exception as e:
        logging.error(f"Exception running script {script_name}: {e}")
        script_status[script_name] = f'Error: {str(e)}'
    finally:
        if script_name in script_status and 'Running' in script_status[script_name]:
            script_status[script_name] = f'Completed (Data scraped: {url_count})'


def run_sequence_scripts(scripts):
    for script_name in scripts:
        run_script(script_name)
        print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
        time.sleep(2)


def flinn_vs_competitors_scripts():
    run_sequence_scripts(['Flinn_vs_Fisher.py'])


def consolidate_scripts():
    run_sequence_scripts(['Fisher_Consolidate_matches_All_Products.py'])


def merge_script():
    run_sequence_scripts(['Merge_CSV.py'])


def cleaning_scripts():
    run_sequence_scripts(['Cleaning_process.py'])


def overall_compared_scripts():
    run_sequence_scripts(['Overall_Compare_Script.py'])


def matched_push_scripts():
    run_sequence_scripts(['Matched_push_script.py'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    flinn_vs_competitors_scripts()
    time.sleep(2)
    consolidate_scripts()
    time.sleep(2)
    merge_script()
    time.sleep(2)
    cleaning_scripts()
    time.sleep(2)
    overall_compared_scripts()
    time.sleep(2)
    matched_push_scripts()


