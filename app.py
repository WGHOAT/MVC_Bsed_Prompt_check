from flask import request, Flask, jsonify
from services.prompt_validate import prompt_check , prompt_validation


app = Flask(__name__)


@app.route('/prompt_get', methods=['POST'])
def prompt_get():
    try:
        input_data = request.json
        prompt_validation(input_data)
        prompt = prompt_check(input_data)
        return jsonify({prompt:'prompt'})
    except ValueError as a:
        return jsonify({'error':str(a)}), 400
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

