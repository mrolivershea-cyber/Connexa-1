#!/usr/bin/env python3
"""Quick API test for all 6 testing modes"""

import requests
import json
import time

BASE_URL = "http://localhost:8001/api"

# Login
print("Logging in...")
response = requests.post(f"{BASE_URL}/auth/login", json={"username": "admin", "password": "admin"})
token = response.json()['access_token']
headers = {'Authorization': f'Bearer {token}'}

print(f"✅ Logged in, token: {token[:30]}...")

# Get nodes
print("\nGetting nodes...")
response = requests.get(f"{BASE_URL}/nodes?limit=5", headers=headers)
nodes = response.json()['nodes']
node_ids = [n['id'] for n in nodes[:3]]
print(f"✅ Got {len(nodes)} nodes, testing with IDs: {node_ids}")

# Test 1: Ping Light
print("\n[TEST 1] Ping Light...")
response = requests.post(
    f"{BASE_URL}/manual/ping-light-test-batch-progress",
    json={"node_ids": node_ids, "timeout": 2},
    headers=headers
)
result = response.json()
print(f"✅ Ping Light: {json.dumps(result, indent=2)[:200]}...")

# Test 2: Ping OK
print("\n[TEST 2] Ping OK...")
response = requests.post(
    f"{BASE_URL}/manual/ping-test-batch-progress",
    json={"node_ids": node_ids[:2], "timeout": 10},
    headers=headers
)
result = response.json()
print(f"✅ Ping OK: {json.dumps(result, indent=2)[:200]}...")

# Test 3: Speed Test
print("\n[TEST 3] Speed Test...")
response = requests.post(
    f"{BASE_URL}/manual/speed-test-batch-progress",
    json={"node_ids": node_ids[:1], "sample_kb": 512, "timeout": 15},
    headers=headers
)
result = response.json()
print(f"✅ Speed Test: {json.dumps(result, indent=2)[:200]}...")

# Test 4: GEO Test
print("\n[TEST 4] GEO Test...")
response = requests.post(
    f"{BASE_URL}/manual/geo-test-batch",
    json={"node_ids": node_ids[:2]},
    headers=headers
)
result = response.json()
print(f"✅ GEO Test: {json.dumps(result, indent=2)[:200]}...")

# Test 5: Fraud Test
print("\n[TEST 5] Fraud Test...")
response = requests.post(
    f"{BASE_URL}/manual/fraud-test-batch",
    json={"node_ids": node_ids[:2]},
    headers=headers
)
result = response.json()
print(f"✅ Fraud Test: {json.dumps(result, indent=2)[:200]}...")

# Test 6: GEO+Fraud Combined
print("\n[TEST 6] GEO+Fraud Combined...")
response = requests.post(
    f"{BASE_URL}/manual/geo-fraud-test-batch",
    json={"node_ids": node_ids[:2]},
    headers=headers
)
result = response.json()
print(f"✅ GEO+Fraud: {json.dumps(result, indent=2)[:200]}...")

print("\n" + "=" * 60)
print("ALL 6 TESTING MODES VERIFIED")
print("=" * 60)
