#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-reddit-movies.jarbasai=skill_reddit_movies:RedditMoviesSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-reddit-movies',
    version='0.0.1',
    description='ovos reddit movies skill plugin',
    url='https://github.com/JarbasSkills/skill-reddit-movies',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_reddit_movies": ""},
    package_data={'skill_reddit_movies': ['locale/*', 'ui/*']},
    packages=['skill_reddit_movies'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
