from setuptools import setup

setup_requires = ['setuptools']
try:
    setup(
        name="TestAppQFileDialog",
        version='1',
        author="",
        author_email="",
        description="",
        url="",
        license='GPLv3+',
        packages=['TestAppQFileDialog'],
        include_package_data=True,
        package_data={},
        setup_requires=setup_requires,
        entry_points={'gui_scripts': ['TestAppQFileDialog = TestAppQFileDialog.__main__:main']},
        keywords='',
        classifiers=[]
    )
except Exception as e:
    print(e)
