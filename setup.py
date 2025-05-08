from setuptools import setup, find_packages

setup(
    name='maze_game',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ],
    entry_points={
        'console_scripts': [
            'maze_game=maze_game.game:main'
        ]
    },
)
