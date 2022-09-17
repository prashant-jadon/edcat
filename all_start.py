import os
os.system("python3 req_down.py| tee -a files_to_download.txt")
os.system("python3 json_cov.py")
os.system("python3 names.py | tee -a names_new.html")

