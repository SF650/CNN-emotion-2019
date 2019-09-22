import gc
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

def feature(file, num):

    y, sr = librosa.load(file, sr=44100)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beats = librosa.beat.beat_track(y=y,sr=sr)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,sr=sr)
    y_beats = librosa.clicks(frames=beats, sr=sr)
    
    plt.figure(figsize=(6, 4))
    D=librosa.amplitude_to_db(librosa.stft(y),ref=np.max)
    librosa.display.specshow(D, y_axis='linear')
    plt.title('STFT Linear-frequency power spectrogram')
    plt.savefig('..\\SourceData\\STFT\\' + str(num) + '.JPG')
    plt.close()
    
    
    CQT=librosa.amplitude_to_db(librosa.cqt(y,sr = 44100), ref=np.max)
    plt.figure(figsize=(6, 4))
    librosa.display.specshow(CQT,y_axis='cqt_note')
    plt.title('Constant-Q power spectrogram (note)')
    plt.savefig('..\\SourceData\\CQT\\' + str(num) + '.JPG')
    plt.close()
    
    M=librosa.feature.mfcc(y=y, sr=sr)
    plt.figure(figsize=(6, 4))
    librosa.display.specshow(M, x_axis = 'time')
    plt.title('MFCC')
    plt.savefig('..\\SourceData\\MFCC\\' + str(num) + '.JPG')
    plt.close()
    
    Mfcc_delta = librosa.feature.delta(M)
    
    Beat_Mfcc_delta = librosa.util.sync(np.vstack([M, Mfcc_delta]), beat_frames)
    plt.figure(figsize=(6, 4))
    librosa.display.specshow(Beat_Mfcc_delta, x_axis = 'time')
    plt.title('Beat_Mfcc_delta')
    plt.savefig('..\\SourceData\\MFCC_DELTA\\' + str(num) + '.JPG')
    plt.close()
    
    M=librosa.feature.chroma_stft(y=y, sr=sr)
    plt.figure(figsize=(6, 4))
    librosa.display.specshow(M, y_axis='chroma')
    plt.title('Chroma_STFT')
    plt.savefig('..\\SourceData\\Chroma_STFT\\' + str(num) + '.JPG')
    plt.close()
    
    C=librosa.feature.chroma_cqt(y=y, sr=sr)
    plt.figure(figsize=(6, 4))
    librosa.display.specshow(C,y_axis='chroma')
    plt.title('Chroma_CQT')
    plt.savefig('..\\SourceData\\Chroma_CQT\\' + str(num) + '.JPG')
    plt.close()
	
path = ".\\clips_45seconds\\"

for num in range(1,2):
    file = path + str(num) + ".mp3"
    feature(file, num)
    plt.close('all')
    gc.collect()