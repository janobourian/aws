# Bedrock

## Basics

AI: imitate the human brain behavior
ML: Regression
Neural Networks: Cluster and classification

## Generative AI and Foundation Models Concepts

Model/Foundation Model: Algorithm + Training Data

### How Generative AI works

* Prompt - Input provided to Model
* Tokenizer
* Context Window: number of tokens the model can take as input at once
* Model 
* Max Token/Stop Sequence
* Detokenizer
* Completion - Output of Model
* Inference: Act of using model to generate text
* Foundation model: 
    * Deep neural networks
    * Unlabeled data
    * Generalized: One FM for multiple tasks
    * Pre-trained
    * Large: Exposed to vast amounts of data
    * Expensive
    * GPT-3, DALL-E, Jurassic, PaLM, Gopher

* Tokens: One token generally corresponds to ~4 characters of text for common English text
* Parameters: can be considered count of connections and weights between nodes in a neural network
* Temperature: This parameter controls the creative ability of your model

### Services offering in Generative AI from AWS

* Amazon EC2 Trn1n and EC2 Inf2: IaaS (self managed) for ML experts to build, train and deploy your own models
* Amazon Sagemaker JumpStart: Provides pretained, open-soure models. Deploy open sources FMs with custom configuration
* Amazon codewhisperer: An AI coding companion in 15+ programming languages for code generation
* Amazon Bedrock: Fully manged serverlles service 

## Amazon Bedrock, deep dive

* Fully managed serverless service from AWS
* Make base Foundation Models from Amazon and third-party model providers accessible through an API
* How does Amazon Bedrock work?:
    * AWS Console / AWS CLI / SDK
    * Bedrock API:
        * prompt
        * temperature
        * max_tokens
        * modelId
        * contentType
        * accept
    * Amazon Bedrock Service
    * Foundation Models:
        * Amazon titan: general purpose models
        * Jurassic-2: LLM for text generation
        * Claude: LLM for conversations, question answering and workflow automation
        * Stable Diffusion: generation of unique images, art, logos and designs