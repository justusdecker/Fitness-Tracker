from src.common.build_flask import *
from src.backend.databases.data_access import DAH, Item
for i in range(5):
    DAH.createItem(
        **{
            'title': 'test_object' + str(i),
            'img': 'https://www.vitaminexpress.org/_next/image?url=https%3A%2F%2Fimages.cdn.europe-west1.gcp.commercetools.com%2F783def08-dd2b-475d-b671-c397c0c2dbd7%2F6958-04-L-Arginin_70-SjmjxvAb.png&w=1440&q=80'
        }
    )
def err_return(code: int = 404):
    """
    Returns a simple template for debugging purposes.
    """
    return render_template('error.html', err=code, msg=HTTP_STATUS_MESSAGES[code]), code

@app.route('/',methods = [GET])
def index():
    return render_template('default.html', items = DAH.readItems(), Item = Item)
@app.route('/create',methods = [GET])
def create():
    return render_template('create.html', Item = Item)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)