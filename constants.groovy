def ENVIRONMENTS = [
    'dev': [
        'host': 'localhost',
        'docker_registry': '212783366536.dkr.ecr.us-east-1.amazonaws.com',
        'repository' : 'microservice'
        'tag': 'dev',

    ],
    'prod': [
        'docker_registry': 'prod-registry.example.com',
        'tag': 'prod'
    ]
]