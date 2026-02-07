import json

import pytest
import utils
from pathlib import Path
from components import tune

import ray


@pytest.mark.training
def test_tune_models(dataset_loc):

    
    ray.init(
    num_cpus=2,         
    num_gpus=0,
    include_dashboard=False,
    ignore_reinit_error=True,
)

    num_runs = 2
    experiment_name = utils.generate_experiment_name(prefix="test_tune")
    initial_params = Path("configs/initial_params.json")
    assert initial_params.exists(), "initial_params.json not found"
    results = tune.tune_models(
        experiment_name=experiment_name,
        dataset_loc=dataset_loc,
        initial_params=str(initial_params),
        num_workers=1,
        cpu_per_worker=1,
        gpu_per_worker=0,
        num_runs=num_runs,
        num_epochs=1,
        num_samples=51,
        batch_size=256,
        results_fp=None,
    )
    utils.delete_experiment(experiment_name=experiment_name)
    ray.shutdown()

    assert len(results.get_dataframe()) == num_runs