"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# the `backend/server/server/wsgi.py file
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.default_risk_model.random_forest import RandomForestClassifier
from apps.ml.default_risk_model.extra_trees import ExtraTreesClassifier

try:
    registry = MLRegistry()
    #First Classifier
    rf = RandomForestClassifier()
    registry.add_algorithm(endpoint_name="default_risk_model",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="1.0",
                            owner="Elaniin Tech Company",
                            algorithm_description="Default Risk for DiiMO",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
     # Extra Trees classifier
    et = ExtraTreesClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="default_risk_model",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="1.0",
                            owner="Elaniin Tech Company",
                            algorithm_description="Extra Trees for DiiMO",
                            algorithm_code=inspect.getsource(RandomForestClassifier))


   
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))