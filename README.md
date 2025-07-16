# MKTmasta

## Run the project
install docker (for windows and macos users, install docker desktop)
follow the 3 commands on .bash file
backend (fastapi) will listen in port 8080
airflow web-client will listen in port 8000

## 1st phase
scrap stock market data via yfinance framework

compute peg ratios and other metadata
## 2nd phase
scraping macro economics data from FRED

scraping data from ism (institute for supply management) reports (manufacturing and services)
## 3rd phase
scraping options/derivatives data

compute pricer estimate based on Black-Scholes model (to help selecting stock target price and stop loss)
## 4th phase - can start after 1st phase done
generate an output for stock picking decisions (earnings calendar terms)

output front-end via a dataviz (power bi like or else, to be determinated)

genereate a short list selection based on those quantitatives (top 20 or other guideline)
## 5th phase
scheduling the entire pipeline on monthly or weekly basis (airflow or else)
## 6th phase
integrate a AI token output to sum up kpi's and additional main points from earnings call transcripts (as an input) with ollama apiRest
## 7th phase - in long term
in long term, storaging output and raw data for statistics purposes (regression model tests or else)

in long term ++, train a AI model or RAG (LLM or else if they are more convinient models) based on those output to generate stock picking decisions (in comparison with analysts choices)