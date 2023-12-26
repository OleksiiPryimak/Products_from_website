<h1>Products from Website</h1>
<p>This code will help you automatically extract selected information from selected websites.</p>
<p>This script extracts product information from a website using XPath. It takes two arguments:</p>
<ul>
    <li><strong>url</strong>: The URL of the website to scrape</li>
    <li><strong>xpath</strong>: The XPath expression to select the desired product information</li>
</ul>
<p>The script uses the <strong>click</strong> library to parse command-line arguments, the <strong>requests</strong> library to make HTTP requests, and the <strong>lxml</strong> library to parse HTML content.</p>
<h1>Example / How to use:</h1>
<p>Execute the following command:</p>
<p><code>python Products_from_website.py "[https://www.castorama.pl/produkty/urzadzanie/wyposazenie-kuchenne/zlewozmywaki.html](https://www.castorama.pl/produkty/urzadzanie/wyposazenie-kuchenne/zlewozmywaki.html)" "//*[@id='categoryMainContent']/div/section/div/div/section/section/h3"</code></p>
<p>This will extract product titles from the website for the specific category.</p>
<p>And the script will print the extracted product information to the console.</p>

<h1>Tests for Products_from_website.py</h1> 
<p><strong>For testing you need to have downloaded HTML-file.html</strong></p>
<p>This file contains tests for the Products_from_website.py script. The tests are designed to verify that the script correctly extracts product information from a website using XPath.</p>
