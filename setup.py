from distutils.core import setup

setup(
    name="Timecard",
    version="3.0.0",
    packages=["timecard"],
    url="https://github.com/sirkonst/timecard",
    license="MIT",
    author="Konstantin Enchant",
    author_email="sirkonst@gmail.com",
    description="Framework for rendering tables wih metric values",
    long_description=__import__("timecard.timecard").__about__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
)
