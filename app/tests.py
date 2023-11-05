import pytest
from httpx import AsyncClient
from app.main import app 


# test for registering user 
@pytest.mark.asyncio
async def test_register_user():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/users/register", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}



# test for login 
@pytest.mark.asyncio
async def test_login_user():
    user_credentials = {
        "email": "test@example.com",
        "password": "test_password"
    }
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/users/login", data=user_credentials)
    assert response.status_code == 200  
    assert "user_id" in response.json()  



# test for getting user profile 
@pytest.mark.asyncio
async def test_get_user_profile():
    user_id = "user_id_to_test"  
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get(f"/users/profile?user_id={user_id}")
    assert response.status_code in [200, 404]  



# test for updating user profile 
@pytest.mark.asyncio
async def test_update_user_profile():
    user_id = "user_id_to_test" 
    user_data = {
        "username": "updated_username",
        "email": "updated_email@example.com",
        "full_name": "Updated Full Name"
    }
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.put(f"/users/profile?user_id={user_id}", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User profile updated successfully"}



# test for deleting account
@pytest.mark.asyncio
async def test_delete_user_account():
    user_id = "user_id_to_test"  
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.delete(f"/users/profile?user_id={user_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "User account deleted successfully"}



# test for reset password
@pytest.mark.asyncio
async def test_reset_password():
    user_email = "user_email_to_test@example.com" 
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/users/reset-password", data={"email": user_email})
    assert response.status_code == 200
    assert response.json() == {"message": "Password reset link sent to email"}