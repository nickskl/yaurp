from flask import Flask, session, g, render_template, request
from services.gui import app
from services.gui.config import current_config
from services.gui.utils import do_check_admin, do_check_publisher
import jsonpickle


@app.errorhandler(404)
def not_found(error):
    return render_template('exceptions/404.html'), 404


@app.before_request
def load_current_user():

    if 'token' in request.cookies:
        result = do_check_admin(request.cookies)
        g.is_admin = jsonpickle.decode(result.response.content)
        result = do_check_publisher(result.response.cookies)
        g.is_publisher = jsonpickle.decode(result.response.content)
        g.logged_in = True
        g.user = result.response.cookies['token']
    else:
        g.user = None
        g.is_admin = False
        g.is_publisher = False
        g.logged_in = False


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

app.run(port=current_config.PORT)