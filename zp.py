import ray
import os

if ray.is_initialized():
        ray.shutdown()
ray.init(
        ignore_reinit_error=True,
        num_gpus=0,              
        include_dashboard=True,
        dashboard_host="127.0.0.1",
        dashboard_port=8265,
        runtime_env={
            "env_vars": {
                "GITHUB_USERNAME": os.environ.get("GITHUB_USERNAME", "")
            }
        },
    )


print(ray.cluster_resources())
