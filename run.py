from encryptease import create_app

app = create_app(configs_dictionary_key='production')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
