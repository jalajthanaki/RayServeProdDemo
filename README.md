# Ray Production Applications

This repository contains production-grade applications built using Ray, a distributed computing framework for Python.

## Project Structure

- `text_ml.py`: Main implementation file containing Ray-based text processing/ML functionality
- `text_ml_client.py`: Client code to interact with the Ray application
- `serve_config.yaml`: Configuration file for Ray Serve deployment
- `__init__.py`: Package initialization file. This is must otherwise you will keep on getting __ModuleNotFound__ Error

## Prerequisites

- Python 3.9+
- Ray (latest version)

## Setup Instructions

1. Create and activate the conda environment:

```bash
conda create -n ray_examples_env python=3.9
conda activate ray_examples_env
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install ray
```

## Deployment

### CPU Deployment

To deploy the application using Ray Serve:

1. Build the deployment configuration:

```bash
serve build text_ml:app -o serve_config.yaml
```

2. Start the Ray cluster:

```bash
ray start --head
```

3. Deploy the application:

```bash
serve deploy serve_config.yaml
```

4. Check deployment status:

```bash
serve status
```

5. Run the client:

```bash
python text_ml_client.py
```

##### Note: `serve status` should be in the `RUNNING` and individual services are in healthy state to get the output.

### GPU Autoscaling Deployment

1. Build the deployment configuration with GPU autoscaling:

```bash
serve build text_ml:app -o serve_config_cpu_autoscalling.yaml
```

2. Start the Ray cluster:

```bash
ray start --head
```

3. Deploy with GPU autoscaling:

```bash
serve deploy serve_config_cpu_autoscalling.yaml
```

4. Check deployment status:

```bash
serve status
```

5. Monitor the deployment in Ray Dashboard:

```bash
ray dashboard
```

## Load Testing

To test the autoscaling behavior:

1. Install k6:

```bash
brew install k6
```

2. Run the load test:

```bash
k6 run loadtest.js
```

3. Monitor the autoscaling behavior:
   - Use `serve status` to check replica counts
   - View the Ray Dashboard at http://localhost:8265
   - Check the number of replicas scaling up and down based on load

The load test will help verify that the autoscaling configuration is working correctly, with replicas being added and removed based on the incoming request load.

## Development Commands

### Debugging

To run the application with debugging enabled:

```bash
ray debug text_ml.py
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Acknowledgments

- Ray Core Team
- Ray Serve Team
- Ray ML Team
