# SocialMediaApp

#### A Simple Social Media app built by using Django and FireBase.

## Features

1. User Register

   - API: http://127.0.0.1:8000/signup/
   - Request: POST
   - Example Data:
     ```json
     {
       "email": "sam@gmail.com",
       "password": "Admin@123",
       "confirmpassword": "Admin@123"
     }
     ```

2. User Login

   - API: http://127.0.0.1:8000/login/
   - Request: POST
   - Example Data:

     ```json
     {
       "email": "sam@gmail.com",
       "password": "Admin@123"
     }
     ```

3. Create Post

   - API: http://127.0.0.1:8000/newpost/
   - Request: POST
   - Example Data:
     ```json
     {
       "email": "sam@gmail.com",
       "posttext": "Sample post",
       "postimage": "/path to image"
     }
     ```

4. Like or Dislike Post

   - API: http://127.0.0.1:8000/likepost/
   - Request: POST
   - Example Data:
     ```json
     {
       "email": "admin@gmail.com",
       "post_id": "sam_2"
     }
     ```

5. Comment on Post

   - API: http://127.0.0.1:8000/commentpost/
   - Request: POST
   - Example Data:
     ```json
     {
       "email": "sam@gmail.com",
       "post_id": "sam_1",
       "comment": "All the best"
     }
     ```

6. Show all Posts

   - API: http://127.0.0.1:8000/posts/
   - Request: GET

7. Sort Posts

   - API: http://127.0.0.1:8000/sortposts/
   - Request: GET

8. Filter Posts

   - API: http://127.0.0.1:8000/filterposts/
   - Request: POST
   - Example Data:
     ```json
     {
       "email": "sam@gmail.com"
     }
     ```

9. Search on Posts

   - API: http://127.0.0.1:8000/searchposts/
   - Request: POST
   - Example Data:
     ```json
     {
       "email": "admin@gmail.com",
       "searchkey": "first"
     }
     ```
