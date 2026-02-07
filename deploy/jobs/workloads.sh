set -ex

export PYTHONPATH=$PYTHONPATH:$PWD
mkdir -p results


# Test data
export RESULTS_FILE=results/test_data_results.txt
export DATASET_LOC="https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/dataset.csv"
pytest --dataset-loc=$DATASET_LOC tests/data --verbose --disable-warnings > $RESULTS_FILE
cat $RESULTS_FILE


# Save to S3 
BUCKET=model-registry-dev-mangukiya-v2

aws s3 cp results/ \
  "s3://$BUCKET/$GITHUB_USERNAME/results/" \
  --recursive
