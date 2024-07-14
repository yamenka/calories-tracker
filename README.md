# Calories tracking service
# Overview
The Calories tracking service allows users to upload images via a web interface. The uploaded images are stored in an AWS S3 bucket, and then analyzed using the OpenAI API. The results of the analysis are returned to the user.

# Features
- Upload images through a web interface.
- Store uploaded images in an AWS S3 bucket.
- Analyze images using the OpenAI API.
- Return analysis results to the user.
  
# Architecture
The service is built using a microservices architecture with the following components:

- Frontend Service: Provides the user interface for uploading images and displaying analysis results.
- Backend Service: Handles requests from the frontend, manages image storage and retrieval, and interacts with the OpenAI API for analysis.
- S3 Service: Manages image storage in an AWS S3 bucket.
- OpenAI Service: Interacts with the OpenAI API to analyze images.

# Technologies Used
- Python
- FastAPI
- AWS S3 (Boto3)
- OpenAI API

## Design : 
- Sequence Digram :
  
<img width="785" alt="Screenshot 2024-07-14 at 11 03 19 PM" src="https://github.com/user-attachments/assets/e6c9bbec-4ac2-48c7-92d7-a059a07fd7c4">

- UseCase Diagram :
  
<img width="585" alt="Screenshot 2024-07-14 at 10 56 21 PM" src="https://github.com/user-attachments/assets/383aec3e-30be-4f3c-ba06-41ab81afd685">

- Class Diagram :
  
<img width="593" alt="Screenshot 2024-07-14 at 11 41 58 PM" src="https://github.com/user-attachments/assets/ed5a026e-752b-4cd5-ab94-d4062acf86d4">
