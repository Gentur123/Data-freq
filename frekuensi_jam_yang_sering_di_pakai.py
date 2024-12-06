# -*- coding: utf-8 -*-
"""frekuensi jam yang sering di pakai

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pKG8BAB0SVASR7oYpXO1Z0Vq2BRUaXrv
"""

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd

df = pd.read_csv('/content/drive/My Drive/User Earnings and Job Status Report Platon.csv')

import pandas as pd
import matplotlib.pyplot as plt

# ... (kode untuk membaca data dan preprocessing) ...

# 1. Filter data untuk mengecualikan status "fulltime"
filtered_df = df[df['status'] != 'fulltime']

# 2. Asumsi kolom yang berisi informasi waktu adalah 'takenDate'
# dan formatnya adalah 'YYYY-MM-DD HH:MM:SS'
filtered_df['hour'] = pd.to_datetime(filtered_df['takenDate']).dt.hour

# 3. Menghitung frekuensi setiap jam (pada data yang sudah difilter)
hour_frequencies = filtered_df['hour'].value_counts()

plt.figure(figsize=(11, 5))  # ukuran gambar

plt.hist(df['hour'], bins=24, edgecolor='black')  # bins=24 untuk setiap jam

plt.xlabel("Jam")
plt.ylabel("Frekuensi")
plt.title("Distribusi Frekuensi Jam")

plt.xticks(range(24))  # Menampilkan label untuk setiap jam

plt.show()
