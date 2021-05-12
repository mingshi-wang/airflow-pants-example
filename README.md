# airflow-pants-example
1. Build a pex file for the airflow dag:
```
./pants package examples/src/python/pipeline/main.py
```
2. Run these commands to list tasks and run the dag:
```
dist/examples.src.python.pipeline/pex_binary.pex list_dags -sd examples/src/python/dags
dist/examples.src.python.pipeline/pex_binary.pex list_tasks my_dag -sd examples/src/python/dags
dist/examples.src.python.pipeline/pex_binary.pex test my_dag my_task 2021-05-12T00:00:00Z -sd examples/src/python/dags
```
