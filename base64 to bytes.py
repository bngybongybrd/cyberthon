import base64

# Base64 encoded string
base64_str = "JGxhfjpAZwqUj5RKV1ysmQBn6Cx2YWGe2oDy4NSrkSJfkR9A8xgyYa53ncfaPlG6aWu011VDX0k5GbbIiZee1v5TCDjUPbbE2BaqrQh8TmWBEQvYkEX3H8HUBTZqaABF1H78dqAZJt+3RdUwhEoR9+lUbFoly1bZIKsYrZMMDZ+2OAYE4nBbXxFF+dbpIxILBlEfCKCNOjeg+BN2VBQExtowR84Ac/qcvDlohDoUkJIhexF9hUPHrI05JB/p1g5vuxd9reEPRWPH0fy4Ven7Vc1ebCxwBDYxhLvifq6/2E/c+YfaDjAyX2i74T2dbAoWIj8qq3nsRN50BgB829rJJA=="

# Decode the string to bytes
bytes_data = base64.b64decode(base64_str)

# Print the bytes data
print(bytes_data)

'''# Convert bytes data to string
str_data = bytes_data.decode("utf-8")

# Print the string data
print(str_data)'''
