import graphene
import joblib
from graphene import ObjectType, String, Float, Field

class PredictionResult(ObjectType):
    price = Float()

class Query(ObjectType):
    predict_price = Field(PredictionResult, airline=String(), flight=String(), source_city=String(), departure_time=String(), stops=String(), arrival_time=String(), destination_city=String(), flight_class=String(), duration=Float(), days_left=String())

    def resolve_predict_price(self, info, **kwargs):
        # Load your model (ensure the path is correct)
        model = joblib.load('./flight_price_predictor.pkl')

        # Prepare the data for prediction
        # Note: The following is just an example, you need to adjust it based on your model's needs
        data = [[kwargs.get('airline'), kwargs.get('flight'), kwargs.get('source_city'), kwargs.get('departure_time'), kwargs.get('stops'), kwargs.get('arrival_time'), kwargs.get('destination_city'), kwargs.get('flight_class'), kwargs.get('duration'), kwargs.get('days_left')]]
        
        # Perform the prediction
        predicted_price = model.predict(data)

        # Return the result
        return PredictionResult(price=predicted_price[0])

schema = graphene.Schema(query=Query)
