[go back to README](README.md)

## [Domain](https://rasa.com/docs/rasa/2.x/domain/)
The domain defines how a chatbot operates, which is composed of intents, entities, slots,
responses, forms, and actions. It also defines a configuration for conversation sessions.
1. [Slots]: your bot's memory. They act as a key-value store. Types include text slot, boolean slot,
   categorical slot, float, list, any (any type. e.g., dicts, lists, ...)
2. Slot Auto-fill: be set up automatically if your NLU model picks up an entity,
   and your domain contains a slot with the same name,
   and store_entities_as_slots=True and auto_fill=True.
   The initial value of the slot is provided in your domain file.
3. Responses: actions that send messages to a user without running any custom code or returning events.
   It's defined in your domain file.
4. Forms: a special type of action meant to help your chatbot collect information from a user.
   It's defined in your domain file.
5. Actions: what your bot can do. It includes
    1. respond to a user
    2. make an external API call
    3. query a database
    4. just about anything. All custom actions should be listed in your domain.
6. Session Config
## Config
1. Components: user input -> structured output.
   This component includes entity extraction, intent classification, response selection,
   pre-processing, and more.
    1. LM options:
        1. MitieNLP: default model. can build your own model on your corpus
        2. SpacyNLP
        3. HFTransformersNLP
    2. [Tokenzier](https://rasa.com/docs/rasa/2.x/components#tokenizers): split text into tokens
        1. Options: WhitespaceTokenizer, JiebaTokenizer (Chinese), MitieTokenizer, SpacyTokenizer,
           ConveRTTokenizer (deprecated. Use ConveRTFeaturizer?),
           LanguageModelTokenizer (deprecated. Use LanguageModelFeaturizer)
    3. Featurizer:
        1. sparse featurizers and dense featurizers
        2. sequence features and sentence features
        3. Options: MitieFeaturizer (dense), SpacyFeaturizer (dense), ConveRTFeaturizer (dense),
           LanguageModelFeaturizer (dense), RegexFeaturizer (sparse),
           CountVectorsFeaturizer (sparse), LexicalSyntacticFeaturizer (sparse)
    4. IntentClassifier
        1. Options: ~~, DIETClassifier (for both intent and entity), FallbackClassifier
    5. EntityExtractors
        1. If you use multiple entity extractors, we advise that each extractor targets an exclusive set of entity types.
    6. EntitySynonymMapper
    7. Selectors: predicts the best response of a bot, from a set of candidate responses
2. Custom components: Use rasa.nlu.components.Component. Add it in your pipeline by adding the module path.
    1. [Skeleton template](https://rasa.com/docs/rasa/2.x/components#custom-components)
    2. Custom Tokenizer: Use rasa.nlu.tokenizers.tokenizer.Tokenizer
    3. Custom Featurizer: Use RASA standard output dimension (defined for dense and sparse)
3. Policies: define which action to take at each step in a conversation. ML or rule-based or both (in tandem).
    1. Policy Priority:
        1. recommend one policy per priority level in your config
        2. If your policy is a machine learning policy, it should most likely have priority 1, the same as the TEDPolicy
    2. ML policies: Includes
        1. Memoization Policy: remembers the stories from your training data, checking matching stories in stories.yml
            1. AugmentedMemoizationPolicy: has max_history, a forgetting mechanism
    3. Rule-based Policies: to use fixed behaviors (e.g,. biz logic)
    4. Configuring Policies:
        1. Story: a tracker which consists of the states of the conversation just before each action was taken.
        2. Every event creates a new state (e.g., running a bot action, receiving a user message, setting slots)
            1. Step 1: tracker provides a bag of active features
            2. Step 2: Convert all the features into numeric vectors
    5. Custom Policies is possible
    6. Deprecated Policies
4. Importers:
    1. Training data: RASA has a built-in logic to collect and load training data in RASA format. You can also customer how your
       You can also customize how your training data gets imported using custom training data importers.
    2. To write a custom importer, see a template for TrainingDataImporter.
## Actions
After each user message, the model will predict an action that the assistant should perform next.
1. Responses:
    1. Can use variables: enclosing a variable in curly brackets. Or, fill in a variable within a custom action.
       Can use channel-specific (e.g., slack) response variations, conditional response variations
        1. Conditional: specific response variations can also be selected based on one or more slot values
    2. Rich responses: images and interactive elements (e.g., depending on clicked buttons)
    3. Can call responses from your custom actions
2. Forms: slot filling
    1. Define a form in your domain
    2. Activating a form by adding a story or rule. This describes when your bot should run the form.
    3. Deactivating form: automaticaly done once all required slots are filled. Define the end fo a form with a rule or a story.
    4. Slot mappings:
        1. Four pre-defined mappings in RASA
        2. Custom Slot Mappings is supported
    5. For unhappy form paths
        1. If a user's input doesn't fill the requested slot, form action wil be rejected (raising ActionExecutionRejection)
        2. For intentionally rejecting, you can return ActionExecutionRejected event as part of your custom validations or slot mappings
    6. Default Actions: built in the dialogue manage (DM) by default. To personalize your bot, customize these.

## Channels
1. your own website, FB messenger, slack, telegram, custom connectors, ...

## Architecture
1. [NLU Only](https://rasa.com/docs/rasa/2.x/nlu-only):
   You can use RASA NLU as a standalone NLU service
2. [NLU Servers](https://rasa.com/docs/rasa/2.x/nlg):
   You can outsource the response generation and separate it from the dialogue learning.
   The bot will still learn to predict actions and to react to user input based on paste dialogues, but
   the responses it sends back to the user will be generated outside of RASA Open Source.
   Use HTTP server for the outsourced NLU

[go back to README](README.md)