# MapReduce-Hadoop
### Individual Assignment for IST3134 Big Data Analytics in the Cloud

_Uploading dataset_  
dataset kaggle link: [recipes.csv](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews?select=recipes.csv)  
To upload the dataset on the local machine: ```wget https://temp-file.org/download/1jar3Xrd7G2dD/NTmJK9ehmZSs5R6/recipes.csv```  
To put the dataset on the HDFS: ```hadoop fs -put recipes.csv```  

For each approach, the ```time``` command was used to measure the execution time.

* Baseline: ```time python3 count.py```  
  Results: ```cat ingredient_count_results.csv | less```
  
* Local MapReduce: ```time cat recipes.csv | python3 mapper.py | sort - | python3 reducer.py -> ingredientcount.csv```    
  Results: ```cat ingredientcount.csv | less```
  
* HDFS MapReduce: ```time mapred streaming -files mapper2.py,reducer2.py -input recipes.csv -output hdfs_ingredcount -mapper "python3 mapper2.py" -reducer "python3 reducer2.py" ```    
  Results: ```hadoop fs -cat hdfs_ingredcount/part-00000 | less```
  
* MRjob: ```time python3 job.py -r hadoop hdfs:///user/hadoop/recipes.csv --output hdfs:///user/hadoop/MRresults```    
  Results: ```hadoop fs -cat MRresults/part-00000 | less```
