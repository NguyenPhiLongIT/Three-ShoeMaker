from src.models.indicator_model import get_all_indicators

class IndicatorViewModel:
    def __init__(self):
        self.indicator_list = []
    
    def load_data(self):
        """Load indicator data from model."""
        self.indicator_list = get_all_indicators()
        return self.indicator_list
    
    def get_formatted_indicators(self):
        """Return formatted indicator data for view."""
        return [
            {
                'id': indicator['id'],
                'name': indicator['name'],
                'code': indicator['code'],
                'rating': indicator['rating'],
                'description': indicator['description'],
                'image_path': indicator['image_path']
            }
            for indicator in self.indicator_list
        ]
