from flask import Flask, session, g, render_template, request
from services.gui import app


@app.errorhandler(404)
def not_found(error):
    return render_template('exceptions/404.html'), 404


@app.before_request
def load_current_user():
    if 'token' in request.cookies:
        g.user = request.cookies['token']
    else:
        g.user = None


#@app.teardown_request
#def remove_db_session(exception):
#    db_session.remove()


#@app.context_processor
#def current_year():
#    return {'current_year': datetime.utcnow().year}


#app.add_url_rule('/docs/', endpoint='docs.index', build_only=True)
#app.add_url_rule('/docs/<path:page>/', endpoint='docs.show',
#                 build_only=True)
#app.add_url_rule('/docs/<version>/.latex/Flask.pdf', endpoint='docs.pdf',
#                build_only=True)


from services.gui.views import posts, statistics, users

app.register_blueprint(posts.mod)
app.register_blueprint(statistics.mod)
app.register_blueprint(users.mod)

app.run(debug=True)