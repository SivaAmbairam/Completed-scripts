
# from flask import Flask
# import os
# import subprocess
# import logging
# import threading
# import time
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
#         process = subprocess.Popen(
#             ['python', script_path],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             bufsize=1,
#             universal_newlines=True
#         )
#
#         while True:
#             if stop_execution or script_status[script_name] == 'Stopping':
#                 logging.debug(f"Stopping script: {script_name}")
#                 process.terminate()
#                 process.wait(timeout=5)
#                 if process.poll() is None:
#                     process.kill()
#                 script_status[script_name] = f'Stopped (URLs scraped: {url_count})'
#                 break
#
#             output = process.stdout.readline()
#             if output == '' and process.poll() is not None:
#                 break
#             if output:
#                 logging.debug(f'Script {script_name} output: {output.strip()}')
#                 script_output[script_name] = script_output.get(script_name, '') + output
#                 if output.strip().startswith('https://'):  # Count URLs
#                     url_count += 1
#                     script_status[script_name] = f'Running (URLs scraped: {url_count})'
#                 # Flush output to ensure it appears in real-time
#                 print(output.strip(), flush=True)
#
#         stdout, stderr = process.communicate()
#         script_output[script_name] = script_output.get(script_name, '') + stdout + stderr
#         rc = process.poll()
#
#         if rc == 0:
#             script_status[script_name] = f'Completed (URLs scraped: {url_count})'
#         else:
#             script_status[script_name] = f'Error: {stderr.strip()}'
#
#     except Exception as e:
#         logging.error(f"Exception running script {script_name}: {e}")
#         script_status[script_name] = f'Error: {str(e)}'
#
#     finally:
#         if script_status[script_name].startswith('Running'):
#             script_status[script_name] = f'Completed (URLs scraped: {url_count})'
#
#     return script_status[script_name].startswith('Completed')
#
#
# def run_sequence_scripts(scripts):
#     threads = []
#     for script in scripts:
#         thread = threading.Thread(target=run_script, args=(script,))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
#
# def flinn_vs_competitors_scripts():
#     run_sequence_scripts([
#         'Flinn_vs_Frey.py',
#         'Flinn_vs_Nasco.py',
#         'Flinn_vs_Carolina.py',
#         'Flinn_vs_VWR.py',
#         'Flinn_vs_Wardsci.py'
#     ])
#
#
# def export_csv_scripts():
#     run_sequence_scripts(['export_csv.py'])
#
#
# def push_scripts():
#     run_sequence_scripts(['push_script.py'])
#
#
# # def flinn_vs_competitors_scripts():
# #     scripts = [
# #         'Flinn_vs_Frey.py',
# #         'Flinn_vs_Nasco.py',
# #         'Flinn_vs_Carolina.py',
# #         'Flinn_vs_VWR.py',
# #         'Flinn_vs_Wardsci.py'
# #     ]
# #
# #     threads = []
# #     for script in scripts:
# #         thread = threading.Thread(target=run_script, args=(script,))
# #         threads.append(thread)
# #         thread.start()
# #
# #     for thread in threads:
# #         thread.join()
# #
# #     print("Initial scripts have been completed.")
# #
# #     fisher_thread = threading.Thread(target=run_script, args=('Flinn_vs_Fisher.py',))
# #     fisher_thread.start()
# #     fisher_thread.join()
# #
# #     print("Flinn_vs_Fisher.py script has been completed.")
#
#
# def consolidate_scripts():
#     run_sequence_scripts(['Consolidate_matches_All_Products.py'])
#
#
# def cleaning_scripts():
#     run_sequence_scripts(['Cleaning_process.py'])
#
#
# def overall_compared_scripts():
#     run_sequence_scripts(['Overall_Compare_Script.py'])
#
#
# def matched_push_scripts():
#     run_sequence_scripts(['Matched_push_script.py'])
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#     # push_scripts()
#     # time.sleep(2)
#     # export_csv_scripts()
#     # time.sleep(2)
#     flinn_vs_competitors_scripts()
#     # time.sleep(2)
#     # consolidate_scripts()
#     # time.sleep(2)
#     # cleaning_scripts()
#     # time.sleep(2)
#     # overall_compared_scripts()
#     # time.sleep(2)
#     # matched_push_scripts()
#
#
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
#                 return False
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
#                         script_status[script_name] = f'Running'
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
#         return rc == 0
#
#     except Exception as e:
#         logging.error(f"Exception running script {script_name}: {e}")
#         script_status[script_name] = f'Error: {str(e)}'
#         return False
#     finally:
#         if script_name in script_status and 'Running' in script_status[script_name]:
#             script_status[script_name] = f'Completed (Data scraped: {url_count})'
#
# def run_sequence_scripts(scripts):
#     for script_name in scripts:
#         success = run_script(script_name)
#         print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
#         if not success:
#             print(f"Script {script_name} failed. Stopping sequence.")
#             return False
#         time.sleep(5)
#     return True
#
# def export_csv_scripts():
#     return run_sequence_scripts(['export_csv.py'])
#
#
# def flinn_vs_competitors_scripts():
#     scripts = [
#         'Flinn_vs_Frey.py',
#         'Flinn_vs_Nasco.py',
#         'Flinn_vs_Carolina.py',
#         'Flinn_vs_VWR.py',
#         'Flinn_vs_Wardsci.py'
#     ]
#
#     threads = []
#     for script in scripts:
#         thread = threading.Thread(target=run_script, args=(script,))
#         threads.append(thread)
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#     print("Initial scripts have been completed.")
#     return True
#
# def consolidate_scripts():
#     return run_sequence_scripts(['Consolidate_matches_All_Products.py'])
#
#
# def cleaning_scripts():
#     return run_sequence_scripts(['Cleaning_process.py'])
#
#
# def overall_compared_scripts():
#     return run_sequence_scripts(['Overall_Compare_Script.py'])
#
#
# def matched_push_scripts():
#     return run_sequence_scripts(['Matched_push_script.py'])
#
#
# def wait_for_completion(script_name):
#     while script_status.get(script_name, '').startswith('Running'):
#         time.sleep(1)
#     return script_status.get(script_name, '').startswith('Completed')
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#
#     # print("Starting push_scripts...")
#     # if export_csv_scripts() and wait_for_completion('export_csv_scripts.py'):
#     #     print("export_csv_scripts completed successfully.")
#     #
#     #     print("Starting flinn_vs_competitors_scripts...")
#     #     print("Starting flinn_vs_competitors_scripts...")
#     if flinn_vs_competitors_scripts():
#         competitor_scripts = ['Flinn_vs_Frey.py', 'Flinn_vs_Nasco.py', 'Flinn_vs_Carolina.py', 'Flinn_vs_VWR.py', 'Flinn_vs_Wardsci.py']
#         all_completed = all(wait_for_completion(script) for script in competitor_scripts)
#         if all_completed:
#             print("flinn_vs_competitors_scripts completed successfully.")

                # print("Starting consolidate_scripts...")
                # if consolidate_scripts() and wait_for_completion('Consolidate_matches_All_Products.py'):
                #     print("consolidate_scripts completed successfully.")
                #
                #     print("Starting cleaning_scripts...")
                #     if cleaning_scripts() and wait_for_completion('Cleaning_process.py'):
                #         print("cleaning_scripts completed successfully.")
                #
                #         print("Starting overall_compared_scripts...")
                #         if overall_compared_scripts() and wait_for_completion('Overall_Compare_Script.py'):
                #             print("overall_compared_scripts completed successfully.")
                #
                #             print("Starting matched_push_scripts...")
                #             if matched_push_scripts() and wait_for_completion('Matched_push_script.py'):
                #                 print("matched_push_scripts completed successfully.")
                #                 print("All scripts have been executed sequentially and successfully.")


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
# def run_script(script_name):
#     global stop_execution, script_status, script_output
#     script_path = os.path.join(SCRIPTS_DIRECTORY, script_name)
#     script_status[script_name] = 'Running'
#     url_count = 0
#
#     try:
#         logging.debug(f"Starting script: {script_name}")
#         process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
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
# def run_sequence_scripts(scripts):
#     for script_name in scripts:
#         run_script(script_name)
#         print(f"Output of {script_name}:\n{script_output.get(script_name, '')}")
#         time.sleep(5)
#
#
# def export_csv_scripts():
#     run_sequence_scripts(['export_csv.py'])
#
# def flinn_vs_competitors_scripts():
#     scripts = [
#         'Flinn_vs_Frey.py',
#         'Flinn_vs_Nasco.py',
#         'Flinn_vs_Carolina.py',
#         'Flinn_vs_VWR.py',
#         'Flinn_vs_Wardsci.py'
#     ]
#
#     threads = []
#     for script in scripts:
#         thread = threading.Thread(target=run_script, args=(script,))
#         threads.append(thread)
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#     print("Initial scripts have been completed.")
#
#
# def consolidate_scripts():
#     run_sequence_scripts(['Consolidate_matches_All_Products.py'])
#
#
# def cleaning_scripts():
#     run_sequence_scripts(['Cleaning_process.py'])
#
#
# def overall_compared_scripts():
#     run_sequence_scripts(['Overall_Compare_Script.py'])
#
#
# def matched_push_scripts():
#     run_sequence_scripts(['Matched_push_script.py'])
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#     # export_csv_scripts()
#     # time.sleep(2)
#     flinn_vs_competitors_scripts()
#     time.sleep(2)
#     consolidate_scripts()
#     time.sleep(2)
#     # cleaning_scripts()
#     # time.sleep(2)
#     # overall_compared_scripts()
#     # time.sleep(2)
#     # matched_push_scripts()

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
        time.sleep(5)


def flinn_vs_competitors_scripts():
    run_sequence_scripts(['Flinn_vs_Frey.py'])


def consolidate_scripts():
    return run_sequence_scripts(['Fisher_Consolidate_matches_All_Products.py'])


def merge_script():
    return run_sequence_scripts(['Merge_script.py'])


def cleaning_scripts():
    return run_sequence_scripts(['Cleaning_process.py'])


def overall_compared_scripts():
    return run_sequence_scripts(['Overall_Compare_Script.py'])


def matched_push_scripts():
    return run_sequence_scripts(['Matched_push_script.py'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    flinn_vs_competitors_scripts()
    # time.sleep(2)
    # consolidate_scripts()
    # time.sleep(2)
    # cleaning_scripts()
    # time.sleep(2)
    # overall_compared_scripts()
    # time.sleep(2)
    # matched_push_scripts()

