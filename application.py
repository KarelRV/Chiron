#!flask/bin/python
# comment here
from App import application
application.run(debug=True, host='0.0.0.0', port=4000)
#application.run(debug=False,host='0.0.0.0', port=80)

