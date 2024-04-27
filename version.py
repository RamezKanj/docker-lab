import os
import requests

def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    
    if patch < 9:
        patch += 1
    else:
        patch = 0
        if minor < 9:
            minor += 1
        else:
            minor = 0
            major += 1
    
    return f"{major}.{minor}.{patch}"

# Fetch current version from GitLab project variable
project_id = "55120314"
access_token = os.getenv('ACCESS_TOKEN')
variable_name = "VERSION"
url = f"https://gitlab.com/api/v4/projects/{project_id}/variables/{variable_name}"
headers = {"PRIVATE-TOKEN": access_token}
response = requests.get(url, headers=headers)
current_version = response.json()["value"]

# Increment version
new_version = increment_version(current_version)

# Update GitLab project variable with new version
data = {"value": new_version}
response = requests.put(url, headers=headers, data=data)

def create_git_tag(project_id, access_token, tag_name, ref):
    url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/tags"
    headers = {"PRIVATE-TOKEN": access_token}
    data = {"tag_name": tag_name, "ref": ref}
    response = requests.post(url, headers=headers, data=data)
    return response.status_code

ref = "main"

create_git_tag(project_id, access_token, new_version, ref)

print(new_version) 