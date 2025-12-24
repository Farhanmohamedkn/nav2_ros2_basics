from setuptools import find_packages, setup

package_name = 'nav2_bringup_custom'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/nav2_bringup_custom']),
    ('share/nav2_bringup_custom', ['package.xml']),
    ('share/nav2_bringup_custom/launch',
        ['launch/simulation.launch.py']),
    ('share/nav2_bringup_custom/config/localization',
        ['config/localization/ekf.yaml']),
    ('share/nav2_bringup_custom/maps',
        ['maps/map.yaml', 'maps/map.pgm']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='farhan',
    maintainer_email='farhan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
