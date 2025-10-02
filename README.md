# Mini Airflow DAG — Demo by Utkarsh Mishra

It is inspired by `puckel/docker-airflow` (link: https://github.com/puckel/docker-airflow).

## What is here
- `dags/my_demo_dag.py` — a small DAG with three Python tasks:
  - `task_a` → `task_b` → `task_c`
  - `task_b` randomly fails ~40% to demonstrate retry behavior (retries=1)

## How to view (no runtime artifacts here)
Files are visible in the `dags/` folder. This repository is a prototype for explaining DAGs, retries and dependency flow. It is **not** a deployed Airflow instance.
