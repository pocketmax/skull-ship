# Chap 1: Understanding prompting and prompt tech

Introducing LLM prompts
How LLM prompts work
Types of LLM prompts
Components of an LLM prompt
Role prompting
Voice definition
Using patterns to enhance prompt effectiveness
Exploring some examples of combining prompt engineering techniques
exploring LLM parameters
How to approach prompt engineering (experimentation)
The challenges and limitations of using LLM prompts

* LLMs are made with a type of NN called a transformer
* uses positional encoding

# LLM training
## Pre-training
  - exposed to large amounts of text
  - which words follow others i.e. dog followed by bark
  - topics and concepts certain words are related to
* chunking: process of breaking down text into small digestible chunks
* tokens: can be words, partial words or even special characters

* vector space: organized words by there simularites and differences
## fine-tuning: like focusing on areas of study after completing a general education
* LLM practices generating outputs for tasks based on labeled example data.
* labeled data: data that has been annotated with labels that catagorize or desribe the contents. They help train models by providing examples of the expected output.
* fitted response: result after providing LLM with new prompt
* natural language processing tasks
  - sentiment analysis
  - topic modeling
  - document classification
* context window: matters for the following reasons
  - Coherence and relevance: Larger context window lets model maintain thread of conversation or doc leading to more coherent and contexually relevant responses
  - text generation: generate content thats consistant with previous sections
  - conversation depth: in dialogue sys, a larger context win lets the AI remember and refer to earlier parts of teh conversation
  - knowledge retrieval: tasks referring to large bodies of text or pulling from multiple segments in a doc, a larger context win allows the model to cross-referene and synthesize info more effectively

Large context windows require more resources which can impact resp time.
few-shot learning: model provided with a small number of examples to learn from
zero-shot learning: model relies soley on its pre-existing knowledge and the given prompt to generate a response

* data augmentation: LLM is trained on data that has been artificially expanded by adding noise or variations to the existing data. Can be a way to improve performance where there is limited labeled data

* active learning (few-shot learning): small amount of labeled examples and is asked to identify the most informative examles to label. Fine tuning is done globally for all convos. User gives few examples during prompting to get the output to follow a certain pattern

* transfer learning: LLM is trained on a task that is similar to the task that is being asked to perform. This can be a better way to generated high-quality responses since it allows the LLM to learn from a larger dataset.

* instructional prompts: ask the model to perform a task i.e. summarizing text, translating a sentence or answering a question. Typically start with a directive such as "translate the following sentence into french" or "summarize the following paragraph"

* Conversational prompts: engage the model in a natural human like conversation. Can be framed as questions, statements and often involve a back-and-forth dialogue between the user and the model. Can be a lot of things like casual chit-chat or more focused discussions on specific subjects

* Contenxtual prompts: provide background or context to guide the models response. They help the model understand the users intent, the desired format of the output or any constraints that should be considered while generating a response.
"You are an AI assistant created by OpenAI to be helpful, harmless, and honest. The user has asked
you to summarize the key events in the following passage [insert passage]"

* Creative prompts: invite the model to generate original content or ideas like writting a poem, creating a story or brainstorming a solution to the problem. i.e. "write a poem about the ocean"

* Factual prompts: seek accurate and specific info from the model often in the form of a question. like queries about historical events, scientific concepts or general trivia. Rely on model to recall and synthesize info that is learned during pre-training phase. i.e. "what year was the constitution signed?"

* step by step prompt: require the model to give a sequence of steps or a procedure to accomplish a task such as a recipe or a tutorial or an algorithm.

* opinion based prompts: ask the model to give an opinion, perspective or recommendation on a topic.

* Multi-modal prompts: input data of multiple types like images, audio or video along with followup text

* Systematic prompts: responses that follow a specific structure, pattern or format. i.e. making a list of items, making an outline for an essay or presentation or providing a structured analysis of a topic.

* Prompt chains i.e. chain of thought: a series of interconnected inputs and outputs where the model response to one prompt is used as input for the next prompt. i.e. "what is the capital of france?" "the capital is Paris" "What is the population of paris?"

## Components of an LLM prompt
* Task Description: a clear description of the task the model is to perform
* Context: can help the model understand the scope, constraints and background info relevant to the task i.e. domain specific terminology
* Input Data: should be relevent to the task and formulated in a way that is easy for the model to understand and analyze
* placeholder tokens: These are variables that indicate where the model should insert it's response. Can help with structure and format of the output i.e. "imagine you are visiting a city [City_Name]"

* Examples: including examples in the prompt helps
* Constraints: imposing constraints ensures the response meets requirements, adheres to guidelines or avoids problematic content. i.e. "compose a 4 line poem about a sunrise"
* Tone and style: can help generate outputs that align with intended purpose and audience

## Role prompting for tailored interactions
* Expoert roles: pretending to be an expert in a specific field can get the model to give a more informed and detailed response
* Fictional roles: assuming the role of a fictional character can make immersive and creative interaction
* Guiding roles: taking on the role that guides or mentors the model like a teacher or coach can encourage the model to think more deeply about the topic, explore alternative perspectives or refine its understanding of complex concepts
* Collaborative roles: pose as collaborator like a teammate or co-author can help with more dynamic interactions


studytogether.com

# prompt database
www.thepromptindex.com
promptbase.com

input text vs prompt?

page 33