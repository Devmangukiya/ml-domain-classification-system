import json

import pytest
import utils
from pathlib import Path
from components import train
import ray

@pytest.mark.training
def test_train_model(dataset_loc):

    ray.init(
    num_cpus=2,         
    num_gpus=0,
    include_dashboard=False,
    ignore_reinit_error=True,
)

    experiment_name = utils.generate_experiment_name(prefix="test_train")
    train_loop_config = Path("configs/train_loop_config.json")

    assert train_loop_config.exists(), "train_loop_config.json not found.."

    result = train.train_model(
        experiment_name=experiment_name,
        dataset_loc=dataset_loc,
        train_loop_config= str(train_loop_config),
        num_workers=1,
        cpu_per_worker=1,
        gpu_per_worker=0,
        num_epochs=2,
        num_samples=45,
        batch_size=64,
        results_fp=None
    )
    utils.delete_experiment(experiment_name=experiment_name)

    ray.shutdown()
    train_loss_list = result.metrics_dataframe.to_dict()["train_loss"]
    assert train_loss_list[0] > train_loss_list[1]  # loss decreased