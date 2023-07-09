import requests

# 设置 GitHub 用户名、仓库名和认证信息
username = 'Si-Xiaoming'
repository = 'YourRepositoryName'
auth_token = 'YourPersonalAccessToken'

# 设置新 Wiki 页面的标题和内容
title = 'New Wiki Page'
content = '''# New Wiki Page

This is the content of the new Wiki page.
'''

# 构建 API 请求的 URL
url = f'https://api.github.com/repos/{username}/{repository}/wikis'

# 设置请求头部，包括认证信息和内容类型
headers = {
    'Authorization': f'token {auth_token}',
    'Accept': 'application/vnd.github.v3+json'
}

# 设置请求体，包括标题和内容
data = {
    'title': title,
    'body': content
}

# 发送 POST 请求来创建新的 Wiki 页面
response = requests.post(url, headers=headers, json=data)

# 检查响应状态码，确认是否创建成功
if response.status_code == 201:
    print('New Wiki page created successfully.')
else:
    print('Failed to create Wiki page.')
    print(f'Response: {response.text}')
