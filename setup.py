import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Flask-UA-Enricher",
    version="0.0.1",
    license="MIT",
    author="agentzex",
    author_email="cypy919@gmail.com",
    description="Decorates flask views and enrich User-Agent header in case of reduced UA string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agentzex/flask-Sec-CH-UA",
    keywords=[
        "flask",
        'flask-ua',
        'flask-ua-enricher',
        'flask-Sec-CH-UA',
        'flask-useragent-enrich',
        'flask-useragent-enricher',
        'flask-sec-ua',
        'useragent-enricher',
    ],
    packages=setuptools.find_packages(),
    platforms="any",
    install_requires=[
        "flask>=2.0.0"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)