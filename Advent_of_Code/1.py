import requests

url = 'https://adventofcode.com/2024/day/1/input'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Cookie': 'session=53616c7465645f5f973c0bf3d6ac0a69d3ad6357155af73e2b548962aa94f9e16bbfdbc02c4418086fb2f2ff35934fab67b398ed89514d02afc78a0b2e0a1af3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.text
    data_lines = data.strip().split('\n')
    col_1, col_2 = [], []
    for i, line in enumerate(data_lines):
        nums = line.split()
        col_1.append(int(nums[0]))
        col_2.append(int(nums[1]))
    col_1.sort()
    col_2.sort()
    result = sum(col_1[i] * col_2.count(col_1[i]) for i in range(len(col_1)))
    print(f"Result: {result}")
