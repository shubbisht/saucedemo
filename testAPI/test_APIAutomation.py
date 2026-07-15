from playwright.sync_api import APIRequestContext
from test_Data.api_data import CREATE_USER_PAYLOAD

def test_get_all_users(api_request, api_base_url, api_headers):
    response = api_request.get(f"{api_base_url}/users?page=2", headers=api_headers)

    assert response.status == 200
    response_body = response.json()
    assert "data" in response_body
    for user in response_body["data"]:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user

def test_create_user(api_request, api_base_url, api_headers):
    response = api_request.post(f"{api_base_url}/users",headers=api_headers,data=CREATE_USER_PAYLOAD)
    assert response.status == 201
    response_body = response.json()
    assert response_body["name"] == CREATE_USER_PAYLOAD["name"]
    assert response_body["job"] == CREATE_USER_PAYLOAD["job"]
    assert "id" in response_body
    assert "createdAt" in response_body

def test_create_user_flow(api_request, api_base_url, api_headers):
    
    # Step 1 - Create User
    response = api_request.post(f"{api_base_url}/users",headers=api_headers,data=CREATE_USER_PAYLOAD)

    # Step 2 - Verify Status Code
    assert response.status == 201

    # Step 3 - Convert Response to JSON
    response_body = response.json()

    # Step 4 - Capture Generated User ID
    created_user_id = response_body["id"]

    # Step 5 - Verify ID is generated
    assert created_user_id is not None
    assert created_user_id != ""

    # Step 6 - Verify Response Data
    assert response_body["name"] == CREATE_USER_PAYLOAD["name"]
    assert response_body["job"] == CREATE_USER_PAYLOAD["job"]

    # Step 7 - Verify Timestamp
    assert "createdAt" in response_body

    # Step 8 - Example of follow-up verification
    print(f"User created successfully with ID: {created_user_id}")