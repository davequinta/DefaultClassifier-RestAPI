from django.test import TestCase

from apps.ml.default_risk_model.random_forest import RandomForestClassifier
from apps.ml.default_risk_model.extra_trees import ExtraTreesClassifier

import inspect
from apps.ml.registry import MLRegistry

class MLTests(TestCase):
    #Testing First Algorithm
    def test_algorithm(self):
        input_data = {
            "level": 2.0,
            "credits_paid": 7.0,
            "blocked_due_credit_denial": 0.0,
            "credits_in_process": 0.0,
            "credits_active": 0.0,
            "credits_overdue": 0.0,
            "credits_rejected": 0.0,
            "special_client": 0.0,
            "client_status": 0.0,
            "number_fee": 1.0,
            "value_fee": 10.66,
            "capital": 35.0,
            "overdue_to_pay": 0.0,
            "overdue_paid": 0.0,
            "fee_status": 2.0,
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        print('RESPONSE RF',response)
        self.assertEqual("OK", response["status"], response)
        self.assertTrue("label" in response)
    #Testing second algorithm
    def test_et_algorithm(self):
        input_data = {
            "level": 2.0,
            "credits_paid": 7.0,
            "blocked_due_credit_denial": 0.0,
            "credits_in_process": 0.0,
            "credits_active": 0.0,
            "credits_overdue": 0.0,
            "credits_rejected": 0.0,
            "special_client": 0.0,
            "client_status": 0.0,
            "number_fee": 1.0,
            "value_fee": 10.66,
            "capital": 35.0,
            "overdue_to_pay": 0.0,
            "overdue_paid": 0.0,
            "fee_status": 2.0,
        }
        alg = ExtraTreesClassifier()
        response = alg.compute_prediction(input_data)
        print('RESPONSE ET',response)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
     

#Test Registry
def test_registry(self):
    registry = MLRegistry()
    self.assertEqual(len(registry.endpoints), 0)
    endpoint_name = "default_risk_model"
    algorithm_object = RandomForestClassifier()
    algorithm_name = "random forest"
    algorithm_status = "production"
    algorithm_version = "1.0"
    algorithm_owner = "Elaniin Tech Company"
    algorithm_description = "Random Forest for DiiMO"
    algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
    registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                algorithm_status, algorithm_version, algorithm_owner,
                algorithm_description, algorithm_code)
        # there should be one endpoint available
    self.assertEqual(len(registry.endpoints), 1)