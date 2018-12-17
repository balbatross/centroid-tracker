import setuptools

setuptools.setup(
        name="centroid_tracker",
        version="0.0.3",
        author="Ross Leitch",
        author_email="ross@end-game.com",
        description="A small centroid tracker library based off https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/",
        url="https://github.com/balbatross/centroid-tracker",
        packages=['tracker'],
        install_requires=[
            'scipy',
            'numpy'
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
)
