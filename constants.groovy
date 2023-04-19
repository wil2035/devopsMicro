def ENVIRONMENTS = [
    'dev': [
        'host': 'localhosr',
        'user': 'jenkins',
        'port': 22,
        'docker_registry': 'dev-registry.example.com',
        'tag': 'dev'
    ],
    'prod': [
        'host': 'prod',
        'user': 'jenkins',
        'port': 22,
        'docker_registry': 'prod-registry.example.com',
        'tag': 'dev'
    ]
]