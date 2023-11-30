#!/usr/bin/env python3

import requests

def jfrogUpload():
    #Define the URL, file path, and authentication credentials
    url = "http://100.25.221.141:8082//artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    file_path = "/var/lib/jenkins/workspace/assign2/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    username = 'admin'
    password = 'United@2023'

        #   send the PUT request with authentication and file upload
    with open(file_path,'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
        # check the response status code
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print(f"PUT reuquest failed with status code(response.status_code)")
        print("Response content:")
        print(response.text)

def main():

    jfrogUpload()

if __name__=="__main__":
    main()
