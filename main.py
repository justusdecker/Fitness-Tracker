from src.common.build_flask import *
from src.backend.databases.data_access import DAH
for i in range(5):
    DAH.createItem(
        **{
            'title': 'test_object' + str(i)
        }
    )
def err_return(code: int = 404):
    """
    Returns a simple template for debugging purposes.
    """
    return render_template('error.html', err=code, msg=HTTP_STATUS_MESSAGES[code]), code

@app.route('/',methods = [GET])
def index():
    return render_template('default.html', items = DAH.readItems())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)