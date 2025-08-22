# API Documentation

---

## Table of Contents

---

## Base URL

**Local**:
http://localhost:5000

**Deployment**:
<paste deployment address here>

---

## Authentication

Most routes require JWT token in Authorization header:
'Authorization: Bearer <your_token>'

---

## Endpoint List

| Endpoint | Methods | Rule |
| :--- | :--- | :--- |
| `attempt.add_an_attempt` | POST | `/attempts/add-attempt/` |
| `attempt.get_a_single_attempt` | GET | `/attempts/<int:attempt_id>/` |
| `attempt.get_all_attempts` | GET | `/attempts/admin/all/` |
| `attempt.get_user_attempts` | GET | `/attempts/` |
| `attempt.remove_an_attempt` | DELETE | `/attempts/admin/remove/<int:attempt_id>/` |
| `auth.register_user` | POST | `/register` |
| `auth.user_delete_profile` | GET | `/delete-my-profile/` |
| `auth.user_login` | POST | `/login` |
| `auth.user_logout` | GET | `/logout` |
| `climb.get_climbs` | GET | `/climbs/` |
| `climb.new_climb` | POST | `/climbs/add-climb/` |
| `climb.new_climbs` | POST | `/climbs/add-climbs/` |
| `climb.remove_a_climb` | DELETE | `/climbs/remove-climb/<int:climb_id>/` |
| `climb.update_a_climb_record` | PATCH, PUT | `/climbs/update/<int:climb_id>/` |
| `company.add_a_company` | POST | `/companies/admin/add/` |
| `company.get_a_company` | GET | `/companies/<int:company_id>` |
| `company.get_companies` | GET | `/companies/` |
| `company.remove_a_company` | DELETE | `/companies/admin/remove/<int:company_id>` |
| `company.update_a_company_record` | PATCH, PUT | `/companies/admin/update/<int:company_id>/` |
| `gym.add_a_gym` | POST | `/gyms/admin/add/` |
| `gym.get_a_gym` | GET | `/gyms/<int:gym_id>/` |
| `gym.get_gym_climbs` | GET | `/gyms/climbs/` |
| `gym.get_gyms` | GET | `/gyms/` |
| `gym.remove_a_gym` | DELETE | `/gyms/admin/remove/<int:gym_id>` |
| `gym.update_a_gym_record` | PATCH, PUT | `/gyms/admin/update/<int:gym_id>/` |
| `gym_rating.add_rating` | POST | `/gym_ratings/add-rating/` |
| `gym_rating.get_a_gym_rating` | GET | `/gym_ratings/<int:rating_id>/` |
| `gym_rating.get_a_gyms_reviews` | GET | `/gym_ratings/by-gym/<int:gym_id>/` |
| `gym_rating.get_a_users_reviews` | GET | `/gym_ratings/by-user/<int:user_id>/` |
| `gym_rating.get_gym_info` | GET | `/gym_ratings/` |
| `gym_rating.get_gym_ratings` | GET | `/gym_ratings/all/` |
| `gym_rating.remove_a_gym_rating` | DELETE | `/gym_ratings/remove-rating/<int:gym_rating_id>/` |
| `gym_rating.remove_any_rating` | DELETE | `/gym_ratings/admin/remove/<int:gym_rating_id>/` |
| `gym_rating.update_a_gym_rating_record` | PATCH, PUT | `/gym_ratings/update/<int:gym_rating_id>/` |
| `info.add_skill` | POST | `/learn/admin/add-skill/` |
| `info.add_style` | POST | `/learn/admin/add-style/` |
| `info.api_info` | GET | `/learn/about-api/` |
| `info.get_skill_levels` | GET | `/learn/skill-levels/` |
| `info.get_styles` | GET | `/learn/styles/` |
| `info.remove_skill` | DELETE | `/learn/admin/remove-skill/<int:skill_level_id>` |
| `info.remove_style` | DELETE | `/learn/admin/remove-style/<int:style_id>` |
| `info.update_skill` | PATCH, PUT | `/learn/admin/update-skill/<int:skill_level_id>` |
| `info.update_style` | PATCH, PUT | `/learn/admin/update-style/<int:style_id>` |
| `static` | GET | `/static/<path:filename>` |
| `user.add_new_user` | POST | `/users/admin/add/` |
| `user.delete_user` | DELETE | `/users/admin/remove/<int:user_id>` |
| `user.get_user_profile` | GET | `/users/profile/` |
| `user.get_users` | GET | `/users/` |
| `user.make_user_admin` | PATCH | `/users/admin/grant-admin/<int:user_id>` |
| `user.revoke_user_admin` | PATCH | `/users/admin/revoke-admin/<int:user_id>` |
| `user.update_user_profile` | PATCH, PUT | `/users/update-profile/` |

---

## Endpoint Details

Detailed description of all routes below!

---

## Authentication Routes

### `POST /login`

**Authenticates a user and returns a JWT access token.**

- Content-Type: `application/json`

### Request

```json
{
    "username": "testuser",
    "password": "SecurePassword123!"
}
```

### Responses

**200 OK**

```json
{
    "token": "<jwt_token_here>"
}
```

**400 Bad Request**

```json
{
    "message": "Username and password are required"
}
```

**401 Unauthorized**

```json
{
    "message": "Invalid username or password"
}
```

### `POST /register`

**Registers a new user and returns a JWT access token.**

- Content-Type: `application/json`

### Request

```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePassword123!",
    "first_name": "Test",
    "last_name": "User",
    "skill_level_id": 1
}
```

### Responses

**201 Created**

```json
{
    "message": "User created successfully.",
    "access_token": "<jwt_token_here>",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "skill_level": {
            "id": 1,
            "name": "Beginner"
        },
        "is_admin": false
    }
}
```

**409 Conflict** (email already exists)

```json
{
    "message": "An account with this email already exists, please login or enter a different email."
}
```

**409 Conflict** (username already exists)

```json
{
    "message": "An account with the username testuser already exists. Please choose a different username."
}
```

### `GET /logout`

**Logs out a user (JWT token will expire shortly).**

- Requires: `Authorization: Bearer <token>`

### Responses

**200 OK**

```json
{
    "message": "Successfully logged out, access token will expire shortly."
}
```

### `DELETE /delete-my-profile/`

**Deletes the current authenticated user's profile.**

- Requires: `Authorization: Bearer <token>`

### Responses

**200 OK**


{
    "message": "Your user account and all associated data has been deleted. Please join us again sometime."
}


---

### Info Routes

## `GET /styles/`

**Retrieves all style records from the styles table and displays to visitor.**

### Response

**200 OK**  

```json
[
  {
    "name": "Slab",
    "description": "A style of climb usually on a flat vertical wall, focussing on balance, footwork and precision."
  },
  {
    "name": "Dyno",
    "description": "A style of climb focussing on powerful dynamic movement, often including jumping or running actions."
  },
  {
    "name": "Overhang",
    "description": "A style of climb where the wall is angled towards the climber, focusses on technique and stamina."
  },
  {
    "name": "Vertical",
    "description": "A style of climb at a variety of angles, where the majority of moves take the climber directly upward."
  }
...]
```

**404 Not Found**  

```json
{
  "message": "No styles found"
}
```

## `GET /skill-levels/`

### Responses

**200 OK**  

```json
[
  {
    "level": "Beginner",
    "description": "Just starting your climbing journey, you might know a few terms and styles. Climbing the lowest few difficulty grades."
  },
  {
    "level": "Intermediate",
    "description": "You've learned most of the terms, you've climbed a lot! Climbing the middle difficulty grades, maybe hitting the plateau!"
  },
  {
    "level": "Advanced",
    "description": "You climb regularly, you know how to visualise your beta, you know that everyone loves slopers and the moonboard is the G.O.A.T! Climbing the advanced grades!"
  }
]
```

**404 Not Found**  

```json
{
  "message": "No styles found"
}
```



### User Routes

### Attempt Routes

### Climb Routes

### Company Routes

### Gym Routes

### Gym Ratings Routes