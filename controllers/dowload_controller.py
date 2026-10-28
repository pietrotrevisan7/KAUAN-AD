from flask import jsonify, send-from_directory

UPLOAD_FOLDER = 'uploads'

class DownloadController:

    @staticmethod
    def download_file(filename):
        try:
            return send_from_directory(UPLOAD_FOLDER, as_attachment=True)
        except FileNotFoundError:
            return jsonify({"error": "Arquivo não necontrado"}), 404
