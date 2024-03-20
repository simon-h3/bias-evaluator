import pandas as pd
import datetime

RESULTS_FOLDER = "results/"

def generate_describe_prompts_table(prompts, response):
    title = '<h1>Describe a... Prompts</h1>'

    df = pd.DataFrame({'Prompts ': prompts, 'Response': response})
    html_table = df.to_html()

    html = title + html_table
    datetime_string = str(datetime.datetime.now()).replace(" ", "_").replace("-", "_")
    OUTPUT_PATH = RESULTS_FOLDER + 'describe_prompts' + datetime_string[0:16] +'.html'

    with open(OUTPUT_PATH, 'w') as f:
        f.write(html)

    print('describe_prompts.html generated')

def generate_ambiguous_prompts_table(prompt, response):
    title = '<h1>Ambiguous Prompts</h1>'

    df = pd.DataFrame({'Prompt': prompt, 'Response': response})
    html_table = df.to_html()

    html = title + html_table
    datetime_string = str(datetime.datetime.now()).replace(" ", "_").replace("-", "_")
    OUTPUT_PATH = RESULTS_FOLDER + 'ambiguous_prompts' + datetime_string[0:16] +'.html'

    with open(OUTPUT_PATH, 'w') as f:
        f.write(html)

    print('ambiguous_prompts.html generated')


def generate_sentiment_analysis_table(inputs, outputs):
    title = '<h1>Sentiment Analysis</h1>'

    df = pd.DataFrame({'Input': inputs, 'Output': outputs})
    html_table = df.to_html()

    html = title + html_table
    datetime_string = str(datetime.datetime.now()).replace(" ", "_").replace("-", "_")
    OUTPUT_PATH = RESULTS_FOLDER + 'sentiment_analysis' + datetime_string[0:16] +'.html'

    with open(OUTPUT_PATH, 'w') as f:
        f.write(html)

    print('sentiment_analysis.html generated')