from pyspark import SparkContext, SparkConf
import sys

def genOutput(line):
    splits = line.split(",")
    return "{}, {}".format(splits[1], splits[2])

if __name__ == "__main__":
    if len(sys.argv)==3:
        conf = SparkConf().setAppName("US airports rdd demo app").setMaster("local[*]")
        sc = SparkContext(conf = conf)
        in_path=sys.argv[1]
        airportsrdd = sc.textFile(in_path)

        airportsusarddfltrd = airportsrdd.filter(lambda line: float(line.split(",")[6])> 40)
        airportcitynamesedd =  airportsusarddfltrd.map(lambda line:genOutput(line))
        out_path=sys.argv[2]
        airportcitynamesedd.saveAsTextFile(out_path)

    else:
        print("Invalid number of arguments passed")
        exit(1)