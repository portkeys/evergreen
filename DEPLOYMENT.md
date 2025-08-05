# 🚀 Deployment Guide for Streamlit Cloud

## Quick Setup

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `evergreen-validation-dashboard`
3. Make it public (required for free Streamlit Cloud)

### 2. Push to GitHub

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set the main file path to: `dashboard.py`
6. Click "Deploy!"

## 📁 Important Notes

### Data Files
- Your `validation_data.csv` file is **NOT** included in the repository (it's in `.gitignore`)
- For Streamlit Cloud deployment, you'll need to either:
  - **Option A**: Include the CSV in the repository (remove from `.gitignore`)
  - **Option B**: Upload the CSV to Streamlit Cloud's file uploader
  - **Option C**: Store the CSV in a cloud storage service (S3, Google Drive, etc.)

### Recommended Approach for Production

1. **Include the CSV in the repository** (for simplicity):
   ```bash
   # Remove validation_data.csv from .gitignore
   git add validation_data.csv
   git commit -m "Add validation data"
   git push origin main
   ```

2. **Or use Streamlit's file uploader**:
   - Modify the dashboard to include a file upload widget
   - Users can upload their own CSV files

## 🔧 Configuration

### Environment Variables (if needed)
If you need to add environment variables:
1. Go to your app settings in Streamlit Cloud
2. Add any required environment variables
3. Redeploy the app

### Custom Domain (Optional)
1. In Streamlit Cloud settings, add your custom domain
2. Update your DNS settings accordingly

## 🆘 Troubleshooting

### Common Issues

1. **App not loading**: Check that `dashboard.py` is the correct main file path
2. **Import errors**: Ensure all dependencies are in `requirements.txt`
3. **Data not found**: Make sure your CSV file is included in the repository
4. **Permission errors**: Ensure the repository is public (for free tier)

### Debugging

1. Check the Streamlit Cloud logs in your app dashboard
2. Test locally first: `streamlit run dashboard.py`
3. Verify all dependencies are listed in `requirements.txt`

## 📊 Monitoring

- Monitor your app's performance in Streamlit Cloud dashboard
- Check usage statistics and logs
- Set up alerts if needed

## 🔄 Updates

To update your deployed app:
```bash
git add .
git commit -m "Update dashboard"
git push origin main
```
Streamlit Cloud will automatically redeploy your app. 