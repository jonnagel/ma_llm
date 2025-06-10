"""Configuration for cultural coherence detection criteria."""

COHERENCE_METRICS = {
    'truth_over_politics': {
        'indicators': [
            'data-driven decisions',
            'transparent reporting', 
            'admits mistakes',
            'published postmortems',
            'open salary bands'
        ],
        'weight': 0.35,
        'red_flags': [
            'messaging discipline',
            'narrative control',
            'no negative reviews'
        ]
    },
    'evidence_based_culture': {
        'indicators': [
            'peer review mentioned',
            'A/B testing culture',
            'metrics tracking',
            'model validation',
            'error budgets'
        ],
        'weight': 0.30,
        'red_flags': [
            'gut feel decisions',
            'hero culture',
            'no technical blog'
        ]
    },
    'minimal_corporate_theater': {
        'indicators': [
            'direct communication',
            'few meaningless meetings',
            'clear accountability',
            'remote work supported',
            'results over hours'
        ],
        'weight': 0.35,
        'red_flags': [
            'culture fit emphasis',
            'mandatory fun',
            'presenteeism'
        ]
    }
}
