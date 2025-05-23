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

To deploy the application using Ray Serve:

1. Build the deployment configuration: Pregenerated serve_config.yaml is already available.

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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Ray Core Team
- Ray Serve Team
- Ray ML Team
