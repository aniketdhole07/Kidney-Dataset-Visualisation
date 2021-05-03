# Kidney-Dataset-Visualisation
A WebApp for Faster and Easy Visualisation of NanoDtring Kidney Dataset

## Steps
If You want to run the Images of [Nanostring Dataset](http://nanostring-public-share.s3-website-us-west-2.amazonaws.com/GeoScriptHub/KidneyDataset/ROI_reports.zip) ,you can directly skip to step 3. If you have other Dataset you can reun the initial steps.
1. To Optimize Images , Update the `path` variable and the code of `optimise_images.py` will automatically compress all the images in that directory.
2. To Convert Text to CSV File ,Update the Source and Destination Path of .txt and .csv file and Run the code `convert_txt_to_csv` .
3. For Main WebAPP, Make Sure the Images are Present in the `static` folder if you are using Customised Data ( Data Already present for Nanostring Dataset) as Flask recognises that location. Then Just Run `home.py` and the Flask Server Willl start in LocalHost.

## Running Commands:

1. `git clone https://github.com/aniketdhole07/Kidney-Dataset-Visualisation`
2. `cd Kidney-Dataset-Visualisation`
3. `pip install pandas Flask plotly`
4. `python3 home.py`
5. Open `http://127.0.0.1:5000/ ` in your browser
