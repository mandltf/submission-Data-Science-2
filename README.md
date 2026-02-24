# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Tuliskan seluruh permasalahan bisnis yang akan diselesaikan.
Faktor apa saja yang paling mempengaruhi mahasiswa menjadi Dropout?
1. Apakah mahasiswa yang menunggak biaya lebih sering dropout?
2. Apakah beasiswa menurunkan risiko dropout?
3. Apakah jumlah mata kuliah tidak lulus berpengaruh?
4. Apakah status ekonomi keluarga berpengaruh?
5. Apakah yang sudah menikah lebih rawan dropout?
6. Apakah kondisi ekonomi negara mempengaruhi dropout?

### Cakupan Proyek
1. Melakukan analisis data student untuk memahami karakteristik dan pola dropout.
2. Mengidentifikasi faktor-faktor yang berpengaruh terhadap dropout berdasarkan analisis data.
3. Membangun model machine learning untuk memprediksi kemungkinan dropout seorang mahasiswa.
4. Menyimpan hasil prediksi ke dalam database.
5. Membuat business dashboard interaktif untuk memonitor tingkat dropout.
6. Membuat prototype sistem untuk prediksi mahasiswa berpotensi dropout.

### Persiapan

Sumber data: [Student's Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
1. Buat virtual environment
```
python -m venv venv
```
2. Aktifkan virtual environment
```
venv\Scripts\activate
```
3. Install semua library dari requirements.txt
```
pip install -r requirements.txt
```

Akses Dashboard :
1. Install docker
```
https://www.docker.com/products/docker-desktop/
```
2. Jalankan Metabase dengan docker
```
docker run -d -p 3001:3000 ^
-v %cd%:/metabase-data ^
-e MB_DB_FILE=/metabase-data/metabase.db ^
--name metabaseStudent ^
metabase/metabase
```
3. Akses dashboard
```
http://localhost:3001
```
4. Hentikan Metabase
```
docker stop metabaseStudent
```

Menjalankan file .ipynb :
1. Buka folder project di VS Code atau Jupyter Notebook.
2. Pastikan virtual environment (venv) sudah dibuat dan berisi semua library dari requirements.txt.
3. Buka file notebook (.ipynb).
4. Pada bagian kanan atas, klik Kernel.
5. Pilih kernel dari virtual environment (venv) yang sudah dibuat sebelumnya.
6. Klik Run All untuk menjalankan seluruh sel kode.


## Business Dashboard
Dari total 1.556 mahasiswa, sebanyak 1.421 mahasiswa diprediksi berpotensi dropout. Meskipun secara analitik terdapat kelompok mahasiswa dengan jumlah mata kuliah lulus semester 2 yang cukup baik, model menunjukkan bahwa performa akademik awal tetap menjadi faktor penting dalam meningkatkan atau menurunkan risiko dropout, terutama bagi mahasiswa dengan jumlah kelulusan mata kuliah yang rendah.

Selain faktor akademik, status beasiswa turut berpengaruh, di mana mahasiswa penerima beasiswa cenderung memiliki tingkat kelulusan lebih tinggi dibandingkan non-beasiswa. Dari sisi keluarga, mahasiswa dengan status orang tua legally separated menunjukkan probabilitas dropout yang lebih tinggi. Secara ekonomi, mahasiswa yang memiliki tunggakan pembayaran juga cenderung memiliki risiko dropout lebih besar dibandingkan mahasiswa yang membayar tepat waktu.

## Menjalankan Sistem Machine Learning
1. Masuk ke virtual environment
```
venv/Scripts/activate
```
2. Jalankan streamlit
```
streamlit run app.py
```
atau akses
```

```

## Conclusion
Model prediksi menunjukkan bahwa mayoritas mahasiswa dalam dataset memiliki risiko dropout yang tinggi. Risiko ini tidak hanya dipengaruhi oleh satu faktor, tetapi merupakan hasil kombinasi antara performa akademik awal, kondisi ekonomi, dan latar belakang keluarga.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1 : Implementasi Early Warning System (EWS)
Dengan menggunakan prototype sistem prediksi, Jaya Jaya Institut dapat mengidentifikasi mahasiswanya yang berisiko dropout sejak semester 1–2 berdasarkan performa akademik, tunggakan, dan faktor lainnya. Kemudian, mahasiswa yang terdeteksi berisiko dapat langsung mendapatkan intervensi akademik seperti kelas remedial, tutoring, atau pendampingan dosen wali.
- action item 2 : Program Dukungan Finansial
Institut dapat memberikan skema cicilan fleksibel, bantuan darurat, atau perluasan akses beasiswa bagi mahasiswa dengan tunggakan pembayaran agar hambatan ekonomi tidak berujung pada dropout.
