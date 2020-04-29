# dota-clusters

![Image of Dota2](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dota2.com%2Fplay%2F&psig=AOvVaw1Jo1ON8G7R8Ai_xVeHMDKd&ust=1588267272869000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPjK_eaSjukCFQAAAAAdAAAAABAD)
![Image of a Clustering](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/EM-Gaussian-data.svg/186px-EM-Gaussian-data.svg.png)


Back when learning about the work my dad does, I was super interested in Dota. Combining these two topics into a fun learning scenario, he compiled all the heroes by stats, and ran a hierarchical clustering to group them by closest stat compositions. I absolutely loved this visualization, and felt like I understood his work that much better.

This project is an homage to this first exposure to clustering tools. I still have a passion for gaming, and want to combine this passion with technologies I want to dive deeper into. 

There will be two facets to this project:

## Hero Stat Exploration
The goal of this is to scrape all hero data from the Dota wiki, compile this information into a database, and use this data to build a 3-means exploration on what hero's "true" callings are.  

In this case, it is classifying them, based on clusterings, whether they truly are their primary stat by design.  Another idea is to explore the heros by role.

## Hero Creation
Ever wanted to create your own hero?  Here's your chance!  Using hero data from the Dota wiki, I will construct a k-NN type classification tool that allows people to enter the stats of their hero, and it will output the type of them.  

## Tech Stack
Because this is a way to dive deeper into a tech stack, early ideas for this project are as follows:
* Python as main dev environment
* Docker for environmental setup
* PostgreSQL for database purposes
* [Still choosing my machine learning tech]
