# :cloud: Air Quality Predictor :cloud:
A web app to predict the next hour's air quality, given this hour's pollutant and air quality features!

![](https://github.com/Dillonwong12/healthscope-assessment/blob/main/app/assets/air_quality_predictor.gif)

- EDA, data pre-processing, and model training details are available in healthscope-assessment/ml_dev
- Utilises a stacked LSTM autoencoder model to perform predictions
  
## Usage
1. Clone this repo
```bash
git clone https://github.com/Dillonwong12/healthscope-assessment.git
```

2. Change to the /app directory
```bash
cd healthscope-assessment/app
```

3. Build the docker image
```bash
docker build -t streamlit .
```

4. Finally, run the web app!
```bash
docker run -p 8501:8501 streamlit
```

The app should now be running on http://localhost:8501!!
