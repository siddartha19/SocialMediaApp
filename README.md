# SocialMediaApp

#### A Simple Social Media app built by using Django and FireBase.

## Features

1. User Register

   - Description: This API allows user to register an account in the app. Use the example data or similar structured to try it out. All the given attributes in the below example are required, try by eliminating one attribute and see the result.
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

   - Description: This API allows user to login into his account in the app. Use the example data or similar structured data to try it out. All the given attributes in the below example are required, try by eliminating one attribute and see the result.
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

   - Description: This API allows user to create a new post in the app. Use the example data or similar structured data to try it out. The email is attribute in the below example is required and you can give posttext or postimage or both, try by eliminating one attribute and see the result.
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

   - Description: This API allows user to like or dislike on post in the app i.e if users sends request for first time it counts as like and if he sends again then his like is deleted on post. Use the example data or similar structured data to try it out. All the given attributes in the below example are required, try by eliminating one attribute and see the result.
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

   - Description: This API allows user to comment on post in the app. Use the example data or similar structured data to try it out. All the given attributes in the below example are required, try by eliminating one attribute and see the result.
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

   - Description: This API shows the list of available posts in the app. Use the example data or similar structured data to try it out.
   - API: http://127.0.0.1:8000/posts/
   - Request: GET

7. Sort Posts

   - Description: This API shows the posts in descending order based on count of likes on each post in the app. Use the example data or similar structured data to try it out.
   - API: http://127.0.0.1:8000/sortposts/
   - Request: GET

8. Filter Posts

   - Description: This API shows the posts of a user based on the user email provided to the app. Use the API or similar structured API to try it out.
   - API: http://127.0.0.1:8000/filterposts/?email=sam@gmail.com
   - Request: GET

9. Search on Posts

   - Description: This API shows the posts based on the search keyword provided to the app. Use the API or similar structured API to try it out.
   - API: http://127.0.0.1:8000/searchposts/
   - Request: GET
