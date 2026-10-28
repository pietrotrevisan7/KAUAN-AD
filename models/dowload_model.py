from database.db import get_db_connetion

class DownloadModel:
    @staticmethod
    def find_by_filename(filename):
        conn = get_db_connetion()
        file = conn.execute('SELECT * FROM uploads WHERE filename - ?', (filename,)).fetchone()
        conn.close()
        return file