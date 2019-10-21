# 以CNN預測以V/A值二維情緒座標之情緒

## 1. 取得資料
資料來源：Emotion in Music Database (1000 songs) \
請至 http://cvml.unige.ch/databases/emoMusic/ 申請資料的下載

## 2. 訊號轉換
並使用Librosa套件進行音訊資料的轉換 \
Code: feature.py \
該原始會需要儲存圖片 \
請另外建立目錄，取名為SourceData \
並在該目錄下建立STFT, CQT, MFCC, MEFF_DELTA, Chroma_STFT, Chroma_CQT等目錄

## 3. 資料分段
再來使用PIL套件進行圖片的分割 \
以下的Code會將圖片分割為長度為五秒，且與前一張圖片有50%重疊的圖片 \
Code: Cut45sec.py \
該原始碼會需要儲存圖片 \
請另外建立目錄，取名為5secWith50paOverlappping

## 4. 資料分類
下一步為將切割好的時間片段分類 \
請先建立資料夾MLdata \
並在該目錄下建立STFT, CQT, MFCC, MEFF_DELTA, Chroma_STFT, Chroma_CQT等目錄 \
在這些目錄下A、V兩個目錄 \
在這兩者目錄下建立RAW, train, test, validation等目錄 \
且在這四個目錄中建立-1.0, -0.9, -0.8, -0.7, ..., 0.8, 0.9, 1.0等共21個資料夾 \
使用的原始碼為 \
Code: classify.py \
csv_file與target_folder請手動更改程式碼，分別為valence與arousal兩種

## 5. 進行訓練
在訓練開始前，可以選擇是否要進行10 cross folder validation的步驟\
如需要進行10 cross folder validation, 請自行將資料依照使用者偏好的比例分成十份\
並建立與編入10CrossFolderValidation目錄\
後使用 CNN_10FCV_Train.py 進行資料訓練\
訓練好後會將訓練權重輸出在執行訓練的目錄之下, 名稱為 CNN_10FCV_CQT_Final.h5

## 6. 進行預測
使用Predict Script進行預測\
Code: Predict_script.py


## step 1. Getting data
Source: Emotion in Music Database (1000 songs) \
Please go to http://cvml.unige.ch/databases/emoMusic/ to apply for downlading raw data

## step 2. Signal transfer
Code: feature.py\
Using python package "librosa" to transfer music signal into music feature\
featur.py need to save file at local folder\
please create a folder called "SourceData"\
Under the SourceData, please create folders, and named them as "SFTF", "CQT", "MFCC", "MFCC_DELTA", "Chroma_STFT", "Chroma_CQT"

## step 3. Data Segmentation
Code: Cut45sec.py
Using python package call "PIL" to splite data\
The Cut45sec.py will output a image, which is 5 sec with 50% overlapping\
This script still need to save file at local folder\
Please creat a folder called "5secWith50paOverlapping"

## step 4. Data Classification
Code: Classify.py\
The next step is to classify the cut time segments.\
Please create a folder MLdata first.\
And in this directory, please create following folder: STFT, CQT, MFCC, MEFF_DELTA, Chroma_STFT, Chroma_CQT\
In these directories,create A and V directories.\
under the folder, create RAW, train, test, validation in these two directories.\
And in these four directories, create a total of 21 folders -1.0, -0.9, -0.8, -0.7, ..., 0.8, 0.9, 1.0, etc.
The source code used is \
Code: classify.py \
csv_file and target_folder, please manually change the code into valence and arousal

## 5. Training
Before the start of the training, you can choose whether you want to perform the 10 cross folder validation step\
If you need to carry out 10 cross folder validation, please divide the data into ten according to the user's preference.\
And build and compile into the 10CrossFolderValidation directory\
After using CNN_10FCV_Train.py for data training\
After training, the training weights will be output under the directory of the training, named CNN_10FCV_CQT_Final.h5\

## 6. Forecasting
Predict using Predict Script\
Code: Predict_script.py
