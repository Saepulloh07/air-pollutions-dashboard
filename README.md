
# Air Quality Dashboard ✨

## Setup Environment - Anaconda

1. Create a new conda environment:
    ```bash
    conda create --name main-ds python=3.11.9
    ```

2. Activate the conda environment:
    ```bash
    conda activate main-ds
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Setup Environment - Shell/Terminal

1. Create a new directory:
    ```bash
    mkdir air-pollutions-dashboard
    ```

2. Navigate to the new directory:
    ```bash
    cd air-pollutions-dashboard
    ```

3. Install pipenv if not already installed:
    ```bash
    pip install pipenv
    ```

4. Install required packages using pipenv:
    ```bash
    pipenv install
    ```

5. Activate the pipenv shell:
    ```bash
    pipenv shell
    ```

6. Install additional required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Run Streamlit App

1. Start the Streamlit app:
    ```bash
    streamlit run dashboard.py
    ```
