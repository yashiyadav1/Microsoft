from flask_frozen import Freezer
from app import app
import os

app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

@freezer.register_generator
def all_routes():
    # Yield the index route
    yield '/'
    
    # Yield routes for all other HTML files in the templates folder
    template_dir = app.template_folder
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html') and file not in ['index.html', 'base.html']:
                # Convert file path to route
                route = '/' + os.path.relpath(os.path.join(root, file), template_dir)[:-5]  # remove '.html'
                # Check if the route is valid (doesn't return a 404)
                with app.test_request_context(route):
                    try:
                        app.preprocess_request()
                        if app.dispatch_request().status_code != 404:
                            yield route
                    except:
                        pass  # If there's an error, don't yield this route

if __name__ == '__main__':
    print("Starting to freeze...")
    freezer.freeze()
    print("Freezing complete. Pages generated:")
    for page in freezer.all_urls():
        print(page)