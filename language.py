import json

class PasswordStrengthAnalyzer:
    def __init__(self, language='en'):
        with open(f'{language}.json', 'r') as f:
            self.language_data = json.load(f)
    
    def analyze_password(self, password):
        # perform password analysis
        score = 0
        feedback = []
        
        # generate feedback based on score and language data
        for rule in self.language_data['rules']:
            if rule['score'] <= score:
                feedback.append(rule['message'])
        
        # return score and feedback
        return score, feedback
