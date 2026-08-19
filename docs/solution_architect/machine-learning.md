# Machine Learning

## Amazon Rekognition

* Find objects, people, text, scenes in images and videos using ML
* Facial Analysis and facil search
* Use cases:
  * Labeling
  * Content moderation
  * Text detection
  * Face Detection and analysis
  * Face Search and verification
  * Celebrity Recognition
  * Pathing
* Content Moderation
  * Detect content that is inappropiate, unwantes, or offensive.
  * Set a Minimum Confidence Threshold for items that will be flagged
  * Flag sensitive content for manual review in Amazon Augmented AI (A21)
  * Help comply with regulation

## Trascribe

* Automatically convert speech to text
* Uses a `deep learning process` called `automatic speech recognition` (ASR)
* Automatically remove Personally Identifiable Information

## Polly

* Opposite to Transcribe
* Text to speech
* Lexicon and SSML
  * Customize the pronunciation of words with Pronunciation lexicons
  * Upload the lexicon and use them in the Synthesize Speech
  * Acronyms AWS -> Amazon Web Services
* Generate speech from plain text or from documents marked up with Speech Synthesis Markup Language (SSML) - enables more customization

## Translate

* Natural and accurate language translation
* You can translate content such as websites and applications

## Lex + Connect Overview

* Amazon Lex: Same technology that powers Alexa
  * Automatic Speech Recognition ASR to convert speech to text
  * Natural Language Understanding to recognize the intent of text, callers
* Amazon Connect:
  * Receive calls, create contact flows, cloud-based virtual contact center
  * Can integrate with other CRM systems or AWS
  * No upfront payments, 80% cheaper than traditional contact center solutions

## Comprehend

* Fro Natural Language Processing - NLP
* Fully managed and serverless service
* Uses machine learning to find insights and relationships in text
* Sample use cases:
  * Analyze customer interactions

* Amazon Comprehend Medical Overview
  * Detects and returns useful information in unstructured clinical text
  * Uses NLP to detect Protected Health Information

## SageMaker

* Fully managed service for developers / data scientis to build ML models
* Typically difficult to do all the preocesses in one place + Provision servers
* Machine learning process (simplified): predicting your exam score
* Process:
  * Historical Data
  * Label Data
  * Score
  * Build
  * ML model
  * Train and Tune
  * Deploy the model for new data

## Kendra

* Fully managed document search service powered by Machine Learning
* Extract from within a document
* Process
  * Data Sources
  * Indexing

## Personalize

* Fully managed ML-service to build apps with real-time personalized recommendations
* Example: personalized product recommendations/re-ranking, customized direct marketing
* Same technology used by Amazon.com
* Process:
  * Amazon S3
  * Amazon Personalize API fro real-time data integration
  * Amazon Personalize reading data from S3

## Textract

* Automatically extracts text, handwriting and data from any scanned documents using AI and ML
* Extract data from forms and tables
* Read and process any type of documents
* Use cases:
  * Financial Services
  * Healthcare
