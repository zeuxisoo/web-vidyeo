import os
import json
from flask import current_app, url_for

def assets_for(filename):
    dist_path = os.path.join(current_app.static_folder, 'dist')
    manifest  = os.path.join(dist_path, 'rev-manifest.json')

    with open(manifest) as m:
        data = json.load(m)

    if filename in data:
        return url_for('static', filename=os.path.join('dist', data[filename]))

    return "";
