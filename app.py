import json
from flask import Flask, request
import face_recognition

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome Noushad'


@app.route('/face_match', methods=['POST'])
def face_match():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('file1' in request.files) and ('file2' in request.files):
            file1 = request.files.get('file1')
            file2 = request.files.get('file2')
            ret = compare_faces(file1, file2)
            resp_data = {"match": bool(ret)}
            return json.dumps(resp_data)
        return "Invalid request", 422


def compare_faces(userNidImageFile, userImageFile):
    # nidImage = face_recognition.load_image_file(userNidImageFile)
    # userImage = face_recognition.load_image_file(userImageFile)
    #
    # nidImageEncoding = face_recognition.face_encodings(nidImage)[0]
    # userImageEncoding = face_recognition.face_encodings(userImage)[0]
    #
    # results = face_recognition.compare_faces([nidImageEncoding], userImageEncoding)
    # return results[0]
    return True


if __name__ == '__main__':
    app.run()
