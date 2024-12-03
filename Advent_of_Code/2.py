import requests

url = 'https://adventofcode.com/2024/day/2/input'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Cookie': 'session=53616c7465645f5f973c0bf3d6ac0a69d3ad6357155af73e2b548962aa94f9e16bbfdbc02c4418086fb2f2ff35934fab67b398ed89514d02afc78a0b2e0a1af3'
}

response = requests.get(url, headers=headers)


def check_safety(nums: list[int]) -> bool:
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        correctness = 0
        for x, y in zip(nums, nums[1:]):
            if abs(x - y) in [1, 2, 3]:
                correctness += 1
        return correctness == len(nums) - 1
    return False


if response.status_code == 200:
    data = response.text
    data_lines = data.strip().split('\n')
    safe_reports = 0
    for i, line in enumerate(data_lines):
        nums = list(map(int, line.split()))
        if check_safety(nums):
            safe_reports += 1
    print("Safe reports:", safe_reports)
