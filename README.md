# 🌲 Evergreen Content Label Validation Dashboard

A Streamlit dashboard for validating evergreen content classification disagreements between human labels and AI model predictions.

## 🚀 Features

- **Disagreement Review**: View articles where human labels and AI predictions differ
- **Voting System**: Vote on whether human labels or model predictions are more accurate
- **Progress Tracking**: Monitor validation progress with real-time statistics
- **Export Results**: Download voting results as CSV
- **Clean UI**: Modern, responsive interface with clear visual indicators

## 📋 Prerequisites

- Python 3.8+
- pip

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd evergreen
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Prepare your data**
   - Place your `validation_data.csv` file in the project root
   - Ensure it has the required columns: `article_id`, `title`, `source`, `url`, `body_content`, `human_label`, `model_prediction`, `model_confidence`, `model_reasoning`, `agreement`

2. **Run the dashboard**
   ```bash
   streamlit run dashboard.py
   ```

3. **Access the dashboard**
   - Open your browser and go to `http://localhost:8501`
   - Enter your name/ID in the sidebar
   - Start voting on disagreements

## 📊 Data Format

Your CSV file should contain the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `article_id` | int | Unique identifier for each article |
| `title` | str | Article title |
| `source` | str | Source of the article |
| `url` | str | Article URL (optional) |
| `body_content` | str | Article content |
| `human_label` | bool | Human classification (True=Evergreen, False=Not Evergreen) |
| `model_prediction` | bool | AI model prediction (True=Evergreen, False=Not Evergreen) |
| `model_confidence` | str | Model confidence level |
| `model_reasoning` | str | Model's reasoning for the prediction |
| `agreement` | bool | Whether human and model labels agree |

## 🗳️ Voting System

For each disagreement, users can vote on:
- **👤 Human Label Better**: The human classification is more accurate
- **🤖 Model Prediction Better**: The AI model prediction is more accurate

Votes are automatically saved to `validation_votes.json` and can be exported as CSV.

## 🚀 Deployment

### Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set the main file path to `dashboard.py`
   - Deploy!

### Local Deployment

For local deployment with custom data:
1. Add your `validation_data.csv` to the project
2. Run `streamlit run dashboard.py`
3. Access via `http://localhost:8501`

## 📁 Project Structure

```
evergreen/
├── dashboard.py          # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
├── validation_data.csv  # Your data file (not in repo)
└── validation_votes.json # Vote results (not in repo)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check that your CSV file has the correct format
2. Ensure all required dependencies are installed
3. Verify that the virtual environment is activated
4. Check the Streamlit logs for error messages

## 🔄 Updates

- **v1.0**: Initial release with basic voting functionality
- **v1.1**: Removed "Both Wrong" option, improved UI with larger fonts and better emojis
- **v1.2**: Removed category filtering, simplified data structure
