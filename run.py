from encryptease import create_app
from dotenv import load_dotenv
import os

load_dotenv()


app = create_app(configs_dictionary_key='development')

if __name__ == "__main__":
    port = os.getenv("PORT", 3000)
    app.run(host='0.0.0.0', port=port)
