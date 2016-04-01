import os
from app import create_app # app as application
application = create_app(os.getenv('INSIGHT_CONFIG') or 'default' )


if __name__ == '__main__':
	application.run(host="0.0.0.0",debug=True)