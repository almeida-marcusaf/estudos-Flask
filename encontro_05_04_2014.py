from factory import create_app

app = create_app('CONFIG_DEV', 'app')

if __name__ == '__main__':
    app.run(port=app.config['PORT'])
