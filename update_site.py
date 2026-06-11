import re
import os
import glob

base_dir = r"C:\Users\Solano\.gemini\antigravity-ide\scratch\biodinamica"
html_path = os.path.join(base_dir, "index.html")
css_path = os.path.join(base_dir, "css", "style.css")
js_path = os.path.join(base_dir, "js", "app.js")

# 1. Update HTML
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add Swiper CSS in head
if "swiper-bundle.min.css" not in html:
    html = html.replace('<!-- Phosphor Icons -->', '<!-- Swiper CSS -->\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />\n\n    <!-- Phosphor Icons -->')

# Add Swiper JS before app.js
if "swiper-bundle.min.js" not in html:
    html = html.replace('<script src="js/app.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>\n    <script src="js/app.js"></script>')

# Replace Hero Section (remove video, set background in CSS, add class hero-bg)
hero_pattern = r'<header class="hero">.*?</header>'
new_hero = '''<header class="hero hero-bg">
        <div class="hero-overlay"></div>
        <div class="hero-content fade-in-up">
            <span class="badge">Novo Espaço</span>
            <h1>A MAIOR E MELHOR<br><span class="text-neon">DO ENTORNO</span></h1>
            <p>Mais de 20 anos transformando vidas com equipamentos modernos e professores qualificados.</p>
            <a href="#services" class="btn-primary">Conheça a Academia</a>
        </div>
    </header>'''
html = re.sub(hero_pattern, new_hero, html, flags=re.DOTALL)

# Add images to Services
services_pattern = r'<div class="service-card">\s*<i class="ph-fill ph-barbell"></i>\s*<h3>Musculação</h3>\s*<p>.*?</p>\s*</div>'
new_service_1 = '''<div class="service-card">
                    <div class="service-img"><img src="assets/media/WhatsApp_Image_2026-06-11_at_12.47.36.jpeg" alt="Musculação"></div>
                    <i class="ph-fill ph-barbell"></i>
                    <h3>Musculação</h3>
                    <p>Equipamentos modernos para ganho de massa, força e resistência.</p>
                </div>'''
html = re.sub(services_pattern, new_service_1, html, flags=re.DOTALL)

services_pattern2 = r'<div class="service-card">\s*<i class="ph-fill ph-bicycle"></i>\s*<h3>Spinning</h3>\s*<p>.*?</p>\s*</div>'
new_service_2 = '''<div class="service-card">
                    <div class="service-img"><img src="assets/media/WhatsApp_Image_2026-06-11_at_12.48.06.jpeg" alt="Spinning"></div>
                    <i class="ph-fill ph-bicycle"></i>
                    <h3>Spinning</h3>
                    <p>Aulas intensas para queimar calorias e melhorar o cárdio.</p>
                </div>'''
html = re.sub(services_pattern2, new_service_2, html, flags=re.DOTALL)

services_pattern3 = r'<div class="service-card">\s*<i class="ph-fill ph-users"></i>\s*<h3>Ginástica & Aulas</h3>\s*<p>.*?</p>\s*</div>'
new_service_3 = '''<div class="service-card">
                    <div class="service-img"><img src="assets/media/WhatsApp_Image_2026-06-11_at_13.09.19.jpeg" alt="Ginástica"></div>
                    <i class="ph-fill ph-users"></i>
                    <h3>Ginástica & Aulas</h3>
                    <p>Aulas em grupo animadas para suar a camisa com muita energia.</p>
                </div>'''
html = re.sub(services_pattern3, new_service_3, html, flags=re.DOTALL)

services_pattern4 = r'<div class="service-card">\s*<i class="ph-fill ph-clipboard-text"></i>\s*<h3>Avaliação Física</h3>\s*<p>.*?</p>\s*</div>'
new_service_4 = '''<div class="service-card">
                    <div class="service-img"><img src="assets/media/WhatsApp_Image_2026-06-11_at_13.12.56.jpeg" alt="Avaliação"></div>
                    <i class="ph-fill ph-clipboard-text"></i>
                    <h3>Avaliação Física</h3>
                    <p>Consultoria de saúde personalizada e treinos sob medida.</p>
                </div>'''
html = re.sub(services_pattern4, new_service_4, html, flags=re.DOTALL)


# Replace Gallery with Swiper
media_dir = os.path.join(base_dir, "assets", "media")
images = [os.path.basename(p) for p in glob.glob(os.path.join(media_dir, '*.jpeg')) if 'WhatsApp_Image_2026-06-11' in os.path.basename(p)]
images.sort()

swiper_slides = ""
for img in images:
    swiper_slides += f'                    <div class="swiper-slide"><img src="assets/media/{img}" alt="Galeria"></div>\n'

new_gallery = f'''<div class="section-header fade-in-up">
                <h2>NOSSO <span class="text-neon">ESPAÇO</span></h2>
            </div>
            
            <div class="gallery-slider-container fade-in-up delay-1">
                <div class="swiper gallery-swiper">
                    <div class="swiper-wrapper">
{swiper_slides}
                    </div>
                    <!-- Add Pagination -->
                    <div class="swiper-pagination"></div>
                    <!-- Add Navigation -->
                    <div class="swiper-button-next"></div>
                    <div class="swiper-button-prev"></div>
                </div>
            </div>'''

gallery_pattern = r'<div class="section-header fade-in-up">.*?</div>\s*</div>\s*</section>'
html = re.sub(gallery_pattern, new_gallery + '\n        </div>\n    </section>', html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

if ".hero-bg" not in css:
    css += '''

/* New Premium Styles */
.hero-bg {
    background: url('../assets/media/recepção.jpeg') center/cover no-repeat;
}
.hero-bg .hero-overlay {
    background: linear-gradient(to right, rgba(10,10,10,0.95) 0%, rgba(10,10,10,0.4) 100%);
    z-index: 0;
}
.hero-content {
    z-index: 2;
}

/* Glassmorphism Service Cards */
.service-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 0;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
.service-img {
    width: 100%;
    height: 200px;
}
.service-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-bottom: 2px solid var(--neon-main);
}
.service-card i {
    margin-top: 1.5rem;
}
.service-card h3, .service-card p {
    padding: 0 1.5rem;
}
.service-card p {
    padding-bottom: 2rem;
}

/* Swiper Gallery */
.gallery-slider-container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px 0 50px 0;
}
.gallery-swiper {
    width: 100%;
    height: 500px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.swiper-slide {
    text-align: center;
    background: #000;
    display: flex;
    justify-content: center;
    align-items: center;
}
.swiper-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.swiper-button-next, .swiper-button-prev {
    color: var(--neon-main) !important;
}
.swiper-pagination-bullet-active {
    background: var(--neon-main) !important;
}
'''
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 3. Update JS
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

if "new Swiper" not in js:
    js += '''

    // Init Swiper
    const swiper = new Swiper('.gallery-swiper', {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
            rotate: 20,
            stretch: 0,
            depth: 200,
            modifier: 1,
            slideShadows: true,
        },
        loop: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            320: { slidesPerView: 1 },
            768: { slidesPerView: 2 },
            1024: { slidesPerView: 3 }
        }
    });
'''
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Site updated successfully.")
