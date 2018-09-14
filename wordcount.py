from pyspark import SparkContext, SparkConf
import sys

if __name__ == "__main__":
    if len(sys.argv)==2:
        conf = SparkConf().setAppName("airports").setMaster("local[*]")
        sc = SparkContext(conf = conf)
        path=sys.argv[1]
        lines = sc.textFile(path)

        words = lines.flatMap(lambda line: line.split(" "))

        wordCounts = words.countByValue()

        for word, count in wordCounts.items():
            print("{} : {}".format(word.encode('utf8'), count))
    else:
        print("Invalid number of arguments passed")
        exit(1)