Before Apache Beam appeared, there had been no unified API in the big data world. Frameworks like Hadoop, Flink, and Spark provided their own way to define data processing pipelines. Beam lets you write your application once, saving the cost and time.

Here are the types of use cases where Beam can prove its value:

1. Moving data between different storage media
2. Transforming data into a more desirable format
3. Real-time data processing (e.g. detecting anomalies in real-time data)

## Concepts

- Pipeline: A Pipeline is a definition of your data processing task. All components are defined in the scope of the Pipeline. This is also a place where you provide execution options that tell Beam where and how to run.

- PCollection: A PCollection stands for a data set that Beam’s pipeline works on. The data set can be either bounded or unbounded. We say the data set is bounded when it came from a fixed source, e.g. from a file or a database table. The data set is unbounded when new data can arrive at any moment. PCollections are the inputs and outputs for each PTransform.

- PTransform: A PTransform is a single data processing operation. A PTransform takes one or more PCollections as input, performs a specified operation on each element in PCollection and returns zero or more PCollections as output.