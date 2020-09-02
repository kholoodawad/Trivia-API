Full Stack Trivia API
 Trivia API is a game that involves asking questions in different fields to test your knowledge. Any user can add and delete questions; play a quiz consists of five questions and list the questions according to its category. To achieve that, this project includes a list of endpoints that provide the following functionalities:
•	Display questions in pages, each page includes 10 questions.
•	Display all available categories.
•	Delete question using a question ID.
•	Create new question, including: question, answer text, category, and difficulty score.
•	Display questions by category.
•	Search the questions by a search term.
•	Play the quiz.


Getting Started
•	Installing Dependencies:
o	Python 3.7
o	pip
o	npm
o	node
o	Flask
o	SQLAlchemy
o	Flask_CORS
o	in the `/backend` directory and run: pip install -r requirements.txt
•	Database Setup:
Create a database trivia and restore it as following:

psql trivia < trivia.psql
•	Running the server
From within the `backend` directory execute:
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

API Reference
•	Base URL: This project is hosted locally. The backend is hosted at http://127.0.0.1:5000/
•	Authentication: This api does not require authentication or API keys.
•	Error Handling: This api uses conventional HTTP response codes to indicate the success or failure of an API request. The error response is returned in the following format:
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}

The errors included in this API are:
400 – Bad request
404 – Resource is not found
405 – Method is not allowed
422 – Unprocessable
500 – Internal server error

Endpoints
•	GET '/categories'
- Request Arguments: None
- Returns: all the available categories.
{
"categories” :{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"},
“success”: True}


•	GET . '/questions'
- Request Arguments: None
- Returns: all the available questions paginated in groups of 10.
- example of the response:
{
        'success': True,
        'questions':  [
          {
              "answer": "Colorado, New Mexico, Arizona, Utah",
              "category": 3,
              "difficulty": 3,
              "id": 164,
              "question": "Which four states make up the 4 Corners region of the US?"
          },
          {
              "answer": "Muhammad Ali",
              "category": 4,
              "difficulty": 1,
              "id": 9,
              "question": "What boxer's original name is Cassius Clay?"
          },
          {
              "answer": "Apollo 13",
              "category": 5,
              "difficulty": 4,
              "id": 2,
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          },
          {
              "answer": "Tom Cruise",
              "category": 5,
              "difficulty": 4,
              "id": 4,
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }
      ],
        'total_questions': 4,
        'categories': :{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
        }

POST ...
DELETE '/questions/<int:question_id>'
- Request Arguments: question id
- Returns: True if the question successfully deleted.
- Example:
{'success': True}

POST '/categories/<int:category_id>/questions'
- Request Arguments: category id
- Returns: all questions belong to that category
- Example: http://127.0.0.1:5000/categories/2/questions
returns all the questions in the Art category.
{
          'success':True,
          'questions':[{
“question”: “ Which Dutch graphic artist–initials M C was a creator of optical illusions?”,
“answer”: “Escher”,
“difficulty”:1 ,
“category”:2},
{
“question”: “Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?”,
“answer”: “Jackson Pollock”,
“difficulty”:2 ,
“category”:2},
{
“question”: “How many paintings did Van Gogh sell in his lifetime?”,
“answer”: “One”,
“difficulty”:4 ,
“category”:2},
{
“question”: “La Giaconda is better known as what?”,
“answer”: “Mona Lisa”,
“difficulty”:3 ,
“category”:2}

          'total_questions':4
            }
POST  '/questions'
•	If the search term is posted:

- Request Arguments: search term
- Returns: all questions contain the search term
- Example: http://127.0.0.1:5000/ questions
search term=”tom”
returns all the questions that contain the word “tom”.
The response is in the following format:
{“success”: True,,
“questions”:[{
 "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
              "answer": "Apollo 13",
              "category": 5,
              "difficulty": 4,
              "id": 2}],
“total_questions”:1}
•	If the new question form is posted:
- Request Arguments: new_question, new_answer, difficulty, category
- Returns: True indicating that question is added successfully.
- Example: http://127.0.0.1:5000/ questions
search term=”tom”
returns all the questions that contain the word “tom”.

The response is in the following format:
{“success”: True,,
“questions”:[{
 "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
              "answer": "Apollo 13",
              "category": 5,
              "difficulty": 4,
              "id": 2}],
“total_questions”:1}




POST  '/quizzes'
- Request Arguments: previous_questions and  quiz_category
- Returns: a question belongs to the quiz category and not in the previous questions.
- Example: http://127.0.0.1:5000/quizzes
with previous_questions=[ 2, 4] quiz_category=” Entertainment”
returns a question in the “Entertainment’ category other than questions with id 2 and 4.
{"success": True,
"question":{
“question”:"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
“answer”:” Edward Scissorhands”,
“difficulty”:3,
“category”: ”Entertainment”,
“id”:6}



Testing
To run the tests, run
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py



Authors
The API app file (__init__.py), test file (test_flaskr.py), and this README were authored by Kholood Awad. models.py and frontend files, were created by Udacity as a project template for the Full Stack Web Developer Nanodegree.

