#this is a thing and i made it *smiley face here* 
#run venv: source venv/bin/activate
#read file & plot: python daily_climate_normals.py -f NORMAL_DLY_sample.csv  


#print("bing bong")
import pandas as pd 
import matplotlib.pyplot as plt
import argparse
from datetime import datetime 




def read_file_with_pandas(file_name):
    return pd.read_csv(file_name)

def read_file(file_name):
    with open(file_name, "r") as file:
        print(file.readlines())

def plot_stuff(df):
    dates = df["DATE"]
    daily_min = df["DLY-TMIN-NORMAL"]
    daily_max = df["DLY-TMAX-NORMAL"]
    formatted_dates = []
    for date in dates:
        date_format = '%Y%m%d'
        formatted_dates.append(datetime.strptime(str(date), date_format))
    #plt.subplot(2,1,1)
    plt.plot(formatted_dates, daily_min, c='maroon', ls="--", label='daily minimum')
    #plt.legend(loc="upper left")
    #plt.subplot(2,1,2)
    plt.plot(formatted_dates, daily_max, c='navy', label="daily maximum")
    plt.title("Daily Precipitation Normals")
    plt.xlabel("date")
    plt.ylabel("rain")
    plt.legend(loc="upper left")
    plt.xticks(rotation='vertical')
    plt.show() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", type=str, required=True)
    args = parser.parse_args()
    df = read_file_with_pandas(args.file)
    plot_stuff(df)
