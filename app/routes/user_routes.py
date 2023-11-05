from fastapi import APIRouter, HTTPException, Depends
from app.models.validation_models import UserInfo
from app.firebase_auth import auth, db
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

router = APIRouter()
limiter = RateLimiter(store="memory", key_func=lambda: "global", rate="5/minute")


# register endpoint 
@router.post("/register")
@limiter.limit("5/minute")
async def register_user(user_info: UserInfo):
    try:
        user = auth.create_user(
            email=user_info.email,
            password='random_password'
        )
        
        user_ref = db.collection('users').document(user.uid)
        user_ref.set({
            'username': user_info.username,
            'email': user_info.email,
            'full_name': user_info.full_name,
            'created_at': firestore.SERVER_TIMESTAMP
        })
        
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# login endpoint
@router.post("/login")
@limiter.limit("5/minute")
async def login_user(email: str, password: str):
    try:
        user = auth.get_user_by_email(email)  
        user = auth.sign_in_with_email_and_password(email, password)
        return {"user_id": user['localId']}  
        
    except HTTPError as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")




# view profile 
@router.get("/profile")
@limiter.limit("5/minute")
async def get_user_profile(user_id: str):
    try:
        user_ref = db.collection('users').document(user_id)
        user_data = user_ref.get()
        if user_data.exists:
            return user_data.to_dict()
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")



# update profile 
@router.put("/profile")
@limiter.limit("5/minute")
async def update_user_profile(user_id: str, user_info: UserInfo, current_user=Depends(get_current_user)):
    if current_user.uid != user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to update this user's profile")
    try:
        user_ref = db.collection('users').document(user_id)
        user_ref.update({
            'username': user_info.username,
            'email': user_info.email,
            'full_name': user_info.full_name
        })
        return {"message": "User profile updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")



# delete profile 
@router.delete("/profile")
@limiter.limit("5/minute")
async def delete_user_account(user_id: str, current_user=Depends(get_current_user)):
    if current_user.uid != user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to delete this user account")
    try:
        auth.delete_user(user_id)
        db.collection('users').document(user_id).delete()
        return {"message": "User account deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")



# reset password 
@router.post("/reset-password")
@limiter.limit("5/minute")
async def reset_password(email: str):
    try:
        auth.generate_password_reset_link(email)
        return {"message": "Password reset link sent to email"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")
