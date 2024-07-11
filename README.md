
  

# Basic Bias Evaluator

Bias evaluation system based on OpenAI's APIs.

  

- Example prompts specific to gender bias.

- Sentiment analysis on outputs.

- Space for additional evaluation types and prompts.

  
## Environment, Keys & Variables

To update the **[env.py](https://github.com/simon-h3/bias-evaluator/blob/main/env.py)** variables:

  

    OPENAI_KEY = *key here*

  

Once API key has been specified, the `evaluate.py` code can communicate with OpenAI's APIs.

  
 To install Python modules required:

    pip install -r requirements.txt

  ## Execution

To execute, run the following in a terminal or IDE.

  

    python3 evaluate.py

  

## Viewing

  

Once execution complete, all html* tables viewable in the browser at the following path:

  

**[results/*.html](https://github.com/simon-h3/bias-evaluator/tree/main/results)**
