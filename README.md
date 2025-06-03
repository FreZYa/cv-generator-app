# 📄 CV Generator App

Modern ve kullanıcı dostu bir CV (özgeçmiş) oluşturma uygulaması. Django framework kullanılarak geliştirilmiştir.

## 🌟 Özellikler

- ✨ Modern ve responsive web arayüzü
- 📝 Kolay CV form doldurma
- 📄 Profesyonel PDF çıktısı
- 📋 CV listesi görüntüleme
- 🎨 Güzel ve temiz tasarım
- 📱 Mobil uyumlu arayüz
- 🔒 Güvenli veri saklama

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- pip
- wkhtmltopdf (PDF oluşturma için)

### 1. Projeyi klonlayın
```bash
git clone https://github.com/FreZYa/cv-generator-app.git
cd cv-generator-app
```

### 2. Virtual environment oluşturun
```bash
python -m venv env
```

### 3. Virtual environment'ı aktifleştirin
**Windows:**
```bash
env\Scripts\activate
```
**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```

### 5. wkhtmltopdf kurulumu

**Windows:**
- [wkhtmltopdf download](https://wkhtmltopdf.org/downloads.html) adresinden indirin
- Kurulum sonrası PATH'e ekleyin

**Ubuntu/Debian:**
```bash
sudo apt-get install wkhtmltopdf
```

**MacOS:**
```bash
brew install wkhtmltopdf
```

### 6. Veritabanı migration'larını çalıştırın
```bash
cd cvapp
python manage.py makemigrations
python manage.py migrate
```

### 7. Süper kullanıcı oluşturun (opsiyonel)
```bash
python manage.py createsuperuser
```

### 8. Sunucuyu başlatın
```bash
python manage.py runserver
```

Uygulama http://127.0.0.1:8000 adresinde çalışacaktır.

## 📖 Kullanım

1. **CV Oluşturma**: Ana sayfada CV bilgilerinizi doldurun
2. **PDF İndirme**: CV listesi sayfasından PDF olarak indirebilirsiniz
3. **Yönetim**: Admin panelinden (/admin) CV'leri yönetebilirsiniz

## 🛠️ Teknolojiler

- **Backend**: Django 4.2.21
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **PDF**: pdfkit + wkhtmltopdf
- **Database**: SQLite (geliştirme), PostgreSQL (prodüksiyon önerisi)
- **UI**: Bootstrap + Font Awesome

## 📁 Proje Yapısı

```
cv-generator-app/
├── cvapp/
│   ├── cvapp/          # Django proje ayarları
│   ├── pdf/             # Ana uygulama
│   ├── templates/       # HTML şablonları
│   ├── static/          # CSS, JS, resim dosyaları
│   ├── media/           # Kullanıcı yüklenen dosyalar
│   └── manage.py
├── env/                 # Virtual environment
├── requirements.txt     # Python paketleri
└── README.md
```

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 🌟 Özellik İstekleri

- [ ] Çoklu CV template'leri
- [ ] Fotoğraf yükleme özelliği
- [ ] Sosyal medya linkleri
- [ ] CV paylaşma özelliği
- [ ] Kullanıcı hesapları
- [ ] CV düzenleme özelliği

## 🚀 Gelecek Güncellemeler

- React.js frontend entegrasyonu
- API endpoints
- Kullanıcı authentication sistemi
- Çoklu dil desteği
- Gelişmiş PDF template'leri 