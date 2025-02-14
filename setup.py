import os,setuptools
with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/esupar"

setuptools.setup(
  name="esupar",
  version="1.3.8",
  description="Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models for Japanese and other languages",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="NLP Japanese Chinese Thai English German Serbian Coptic",
  packages=setuptools.find_packages(),
  install_requires=[
    "supar>=1.1.4",
    "transformers>=4.19.0",
    "deplacy>=2.0.3"
  ],
  python_requires=">=3.7",
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Natural Language :: Japanese",
    "Natural Language :: Chinese (Simplified)",
    "Natural Language :: Chinese (Traditional)",
    "Natural Language :: Thai",
    "Natural Language :: English",
    "Natural Language :: German",
    "Natural Language :: Serbian",
    "Topic :: Text Processing :: Linguistic"
  ],
  project_urls={
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
