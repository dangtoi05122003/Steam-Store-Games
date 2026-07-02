import attr

@attr.s(kw_only=True, auto_attribs=True)
class base_dag_config():
    owner: str
    retries: int
    retry_delay: int
    dag_id: str
    dag_type: str
    schedule_interval: str
    max_actives_runs: int
    start_date: str
    catchup: bool
    is_paused_upon_creation: bool