import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy.sql.expression import func, select
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def pagination(questions, request):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * 10
    end = start + 10
    formatted_questions = [question.format() for question in questions]
    paginated_questions = formatted_questions[start:end]
    return paginated_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    # Set up CORS. Allow '*' for origins.
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow_Headers', 'ContentTyp , Authorization')
        response.headers.add('Access-Control-Allow_Methods', 'GET, POST , PATCH, DELETE ,OPTIONS')
        return response

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        categoriesDictionary = {}
        for category in categories:
            categoriesDictionary[category.id] = category.type
        return jsonify({'success': True, 'categories': categoriesDictionary})

    @app.route('/questions', methods=['GET'])
    def get_questions():
        questions = Question.query.all()
        finalquestions = pagination(questions, request)
        if len(finalquestions) == 0:
            abort(404)
        categories = Category.query.all()
        categoriesDictionary = {}
        for category in categories:
            categoriesDictionary[category.id] = category.type
        return jsonify({'success': True, 'questions': finalquestions, 'total_questions': len(questions), 'categories': categoriesDictionary})

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            question.delete()
            return jsonify({'success': True, 'question_id': question_id})
        except:
            abort(422)

    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category(category_id):
        questions = Question.query.filter(Question.category == category_id)
        paginated_questions = pagination(questions, request)
        total_questions = len(paginated_questions)
        if total_questions == 0:
            abort(404)
        return jsonify({'success': True, 'questions': paginated_questions, 'total_questions': total_questions})

    @app.route('/questions', methods=['POST'])
    def search_questions():
        body = request.get_json()
        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_difficulty = body.get("difficulty", None)
        new_category = body.get("category", None)
        searchterm = body.get('searchTerm')
        if searchterm:
            questions = Question.query.filter(Question.question.ilike('%{}%'.format(searchterm))).all()
            results = pagination(questions, request)
            total_questions = len(results)
            return jsonify({'success': True, 'questions': results, 'total_questions': total_questions})
        else:
            if not(new_question or new_answer):
                abort(400)
            else:
                try:
                    question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
                    question.insert()
                    questions = Question.query.order_by(Question.id).all()
                    paginated_questions = pagination(questions, request)
                    return jsonify({'success': True, 'question': question.format()})
                except:
                    abort(405)

    @app.route('/quizzes', methods=['POST'])
    def play_quize():
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions')
            quiz_category = body.get('quiz_category')
            if quiz_category['id'] == 0:
                questions = Question.query.filter(Question.id.notin_(previous_questions)).order_by(func.random())
            else:
                questions = Question.query.filter(Question.id.notin_(previous_questions), Question.category == quiz_category['id']).order_by(func.random())
            quiz_question = questions.first()
            if quiz_question is None:
                return jsonify({'success': True, 'question':False })
            else:
                question = quiz_question.format()
                return jsonify({'success': True, 'question': question})
        except:
            abort(400)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": 404, "message": "Resourse is not found"}), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({"success": False, "error": 422, "message": "Unprocessable"}), 422

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({"success": False, "error": 400, "message": "Bad request"}), 400

    @app.errorhandler(405)
    def methodnotallowed(error):
        return jsonify({"success": False, "error": 405, "message": "Method is not allowed"}), 405

    @app.errorhandler(500)
    def internalServerErrror(error):
        return jsonify({"success": False,  "error": 500, "message": "Internal server error"}), 500

    return app
