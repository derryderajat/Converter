### Converter

Converter :
- [x] Image to PDF
- [ ] PDF to Image

#### Instalasi

##### Windows

1. **Instal Python:**
   - Unduh dan instal Python dari [python.org](https://www.python.org/downloads/windows/).
   - Pastikan menambahkan Python ke PATH saat instalasi.

2. **Clone Repository:**
   ```bash
   git clone git@github.com:derryderajat/Converter.git
   cd Converter
   ```

3. **Setup Lingkungan Virtual (opsional):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. **Instal Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

##### Mac/Linux

1. **Instal Python:**
   - Pastikan Python sudah terinstal. Buka terminal dan jalankan:
     ```bash
     python --version
     ```
   - Jika belum terinstal, instal Python sesuai dengan distribusi sistem Anda.

2. **Clone Repository:**
   ```bash
   git clone git@github.com:derryderajat/Converter.git
   cd Converter
   ```

3. **Setup Lingkungan Virtual (opsional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Instal Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

#### Menjalankan Aplikasi

1. **Jalankan Aplikasi:**
   - Pastikan lingkungan virtual aktif (jika digunakan).

2. **Start Server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Akses Aplikasi:**
   - Buka browser dan navigasikan ke `http://localhost:8000`.

#### Endpoint

- **Convert Image to PDF:**
  - Endpoint: `http://localhost:8000/api/convert/image2pdf`
  - Method: POST
  - Form-data: `file` (choose an image file)

#### Contoh Penggunaan

- **Curl Command:**
  ```bash
  curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:8000/api/convert/image2pdf
  ```

#### Tambahan

Tambahkan informasi tambahan seperti dokumentasi API, catatan rilis, atau catatan pengembangan yang relevan dengan proyek Anda.

### Terima kasih telah menjelaskan singkat untuk project ini di Readme.md