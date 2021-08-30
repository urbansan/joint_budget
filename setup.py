import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="joint_budget",
    description="Common budget manager",
    version="1.0.0",
    author="Kris Urbanczyk",
    author_email="urbansanek@gmail.com",
    project_urls={
        "Source Code": "https://github.com/urbansan/joint_budget",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "dataclasses; python_version < '3.7'",
        "aiofiles",
        "fastapi[all]==0.68.1",
        "uvicorn[standard]~=0.13.0",
        "jinja2"

    ],
    # entry_points={
    #     "console_scripts": [
    #         "multiprocess = shell_multiprocess.main:main",
    #     ]
    # },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
