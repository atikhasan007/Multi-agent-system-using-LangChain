from src.tools.tools import web_search , scrape_url
from src.pipeline.pipeline import run_research_pipeline

# output = web_search.invoke("latest news on ai research?")
# print(output)


# result = scrape_url.invoke("https://www.artificialintelligence-news.com")

# print(result)


topic = "The impact of AI the job market in 2026"
run_research_pipeline(topic)