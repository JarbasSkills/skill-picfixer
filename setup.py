#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-picfixer.jarbasai=skill_picfixer:PicFixerSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-picfixer',
    version='0.0.1',
    description='ovos kings of horror skill plugin',
    url='https://github.com/JarbasSkills/skill-picfixer',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_picfixer": ""},
    package_data={'skill_picfixer': ['locale/*', 'ui/*']},
    packages=['skill_picfixer'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
