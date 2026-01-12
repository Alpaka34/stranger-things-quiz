# stranger_quiz_app.py
import streamlit as st

st.set_page_config(page_title="Stranger Things - Hangi Karaktersin?", layout="centered")

st.title("🧇 Stranger Things Karakter Testi")
st.markdown("Cevaplarını ver, hangi karakter olduğunu öğren!")

# ────────────────────────────────────────────────
# Kullanıcı bilgileri
# ────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    cinsiyet = st.selectbox(
        "Cinsiyetin",
        options=["Kadın", "Erkek", "Diğer / Belirtmek istemiyorum"],
        index=2
    )

with col2:
    kilo = st.number_input("Kilon (kg)", min_value=30, max_value=150, value=60, step=1)

# ────────────────────────────────────────────────
# Sorular
# ────────────────────────────────────────────────
st.subheader("Soruları cevapla")

sorular = [
    {
        "soru": "Arkadaş grubunda genelde nasıl bir roldesin?",
        "secenekler": [
            "Liderlik yapar, planları ben hazırlarım",
            "Espri yapar, ortamı neşelendiririm",
            "Sessizim ama kritik anlarda yardım ederim",
            "Cesurca öne atılır, korumacıyımdır",
            "Bağımsız hareket ederim, kendi yolumu çizerim"
        ]
    },
    {
        "soru": "Tehlike anında ilk tepkin ne olur?",
        "secenekler": [
            "Gücümü kullanır doğrudan savaşırım",
            "Herkesi korumak için öne atılırım",
            "Hızlıca plan yapar kaçış yolu bulurum",
            "Korksam da sevdiklerim için dayanırım",
            "Kaçarım ama sonra geri döner intikam alırım"
        ]
    },
    {
        "soru": "En sevdiğin aktivite hangisi?",
        "secenekler": [
            "Bilim, deney, icat yapmak",
            "Müzik dinlemek, yaratıcı işler",
            "Spor, rekabet, hareket",
            "Yemek yemek, muhabbet etmek",
            "Araştırmak, sır çözmek"
        ]
    },
    {
        "soru": "En büyük korkun ne?",
        "secenekler": [
            "Sevdiklerimi kaybetmek",
            "Kontrolü tamamen kaybetmek",
            "Yalnız kalmak, dışlanmak",
            "Toplumun yargılaması",
            "Geçmiş travmaların geri gelmesi"
        ]
    },
    {
        "soru": "Bir sorunu çözmek için en çok güvendiğin şey?",
        "secenekler": [
            "Aklım ve mantığım",
            "Sezgilerim ve içgüdülerim",
            "Ekip çalışması ve arkadaşlarım",
            "Kuvvet ve cesaret",
            "Kaçış ve hayatta kalma yeteneğim"
        ]
    },
    {
        "soru": "Romantik ilişkilerde nasılsın?",
        "secenekler": [
            "Çok sadık ve koruyucuyum",
            "Flörtöz ama aslında derin biriyim",
            "Utangaç ve yavaş ilerlerim",
            "Bağımsızım, kolay bağlanmam",
            "Eğlenceli ve spontanım"
        ]
    },
    {
        "soru": "En sevdiğin atıştırmalık / yemek?",
        "secenekler": [
            "Waffle / gofret",
            "Şekerli şeyler, abur cubur",
            "Pizza",
            "Kahve veya bira",
            "Sağlıklı şeyler, meyve vs."
        ]
    },
    {
        "soru": "Hayatında en önemli şey ne?",
        "secenekler": [
            "Arkadaşlarım / grubum",
            "Ailem",
            "Özgürlüğüm ve kendim olmak",
            "Gerçek aşk / derin bağ",
            "Adalet ve doğruyu bulmak"
        ]
    }
]

# Cevapları tutacak liste (0-4 arası index)
cevaplar = []

for i, q in enumerate(sorular, 1):
    secim = st.radio(
        f"{i}. {q['soru']}",
        options=q["secenekler"],
        index=None,  # zorunlu seçim için None
        key=f"q{i}"
    )
    if secim is None:
        cevaplar.append(0)  # varsayılan
    else:
        cevaplar.append(q["secenekler"].index(secim) + 1)  # 1-5 arası

# ────────────────────────────────────────────────
# Hesaplama fonksiyonu
# ────────────────────────────────────────────────
def hesapla_karakter(cevaplar_list, cinsiyet_sec, kilo_deger):
    puanlar = {
        "Eleven": 0,
        "Mike Wheeler": 0,
        "Dustin Henderson": 0,
        "Will Byers": 0,
        "Steve Harrington": 0,
        "Nancy Wheeler": 0,
        "Jim Hopper": 0,
        "Max Mayfield": 0,
    }

    # Basit eşleştirme matrisi (her soru için 1-5 → hangi karaktere +1)
    eslesme = [
        [[ "Mike Wheeler", "Nancy Wheeler" ], ["Dustin Henderson"], ["Will Byers"], ["Steve Harrington", "Jim Hopper"], ["Max Mayfield", "Eleven"]],  # q1
        [["Eleven"], ["Steve Harrington", "Jim Hopper"], ["Nancy Wheeler", "Dustin Henderson"], ["Will Byers"], ["Max Mayfield"]],              # q2
        [["Dustin Henderson"], ["Will Byers"], ["Max Mayfield"], ["Dustin Henderson"], ["Nancy Wheeler", "Jim Hopper"]],                     # q3
        [["Mike Wheeler", "Jim Hopper"], ["Eleven"], ["Will Byers"], ["Max Mayfield"], ["Max Mayfield"]],                                   # q4
        [["Dustin Henderson", "Nancy Wheeler"], ["Eleven", "Will Byers"], ["Mike Wheeler", "Steve Harrington"], ["Jim Hopper"], ["Max Mayfield"]], # q5
        [["Mike Wheeler", "Eleven"], ["Steve Harrington"], ["Will Byers"], ["Nancy Wheeler", "Max Mayfield"], ["Robin Buckley"]],           # q6
        [["Eleven"], ["Dustin Henderson"], ["Dustin Henderson"], ["Jim Hopper"], ["Max Mayfield"]],                                         # q7
        [["Mike Wheeler", "Dustin Henderson"], ["Jim Hopper"], ["Max Mayfield"], ["Eleven", "Mike Wheeler"], ["Nancy Wheeler"]]            # q8
    ]

    for q_idx, secim in enumerate(cevaplar_list):
        if 1 <= secim <= 5:
            for kar in eslesme[q_idx][secim-1]:
                if kar in puanlar:
                    puanlar[kar] += 1

    # Bonuslar
    cins = cinsiyet_sec.lower()
    if "kadın" in cins:
        puanlar["Eleven"] += 2
        puanlar["Max Mayfield"] += 2
        puanlar["Nancy Wheeler"] += 1
    elif "erkek" in cins:
        puanlar["Mike Wheeler"] += 1
        puanlar["Steve Harrington"] += 2
        puanlar["Jim Hopper"] += 2

    if kilo_deger > 85:
        puanlar["Jim Hopper"] += 2
    elif kilo_deger < 50:
        puanlar["Eleven"] += 2

    en_iyi = max(puanlar, key=puanlar.get)
    return en_iyi, puanlar[en_iyi], puanlar

# ────────────────────────────────────────────────
# Buton ve sonuç
# ────────────────────────────────────────────────
if st.button("Sonucumu Göster 🚀", type="primary", use_container_width=True):
    if any(c == 0 for c in cevaplar):
        st.error("Lütfen tüm soruları cevapla!")
    else:
        karakter, puan, tum_puanlar = hesapla_karakter(cevaplar, cinsiyet, kilo)

        st.success(f"**SEN: {karakter}**")
        st.markdown(f"**Puanın:** {puan}")

        aciklamalar = {
            "Eleven": "Güçlü ama duygusal bir ruha sahipsin. Sevdiklerini korumak için her şeyi yaparsın. Waffle delisisin!",
            "Mike Wheeler": "Sadık, duygusal ve grubunun doğal liderisin.",
            "Dustin Henderson": "Zeki, esprili, bilim aşığı ve en iyi dostsun!",
            "Will Byers": "Hassas, yaratıcı ve derin duygulara sahipsin.",
            "Steve Harrington": "Eskiden popülerdin, şimdi herkesin abisi / koruyucusu oldun.",
            "Nancy Wheeler": "Zeki, kararlı, gerçeğin peşinden koşan birisin.",
            "Jim Hopper": "Sert görünüyorsun ama kalbin yumuşacık. Baba enerjisi!",
            "Max Mayfield": "Bağımsız, cesur ve kendi yolunu çizen birisin."
        }

        st.markdown("### Neden " + karakter + "?")
        st.info(aciklamalar.get(karakter, "Harika bir karakter sensin!"))

        # İsteğe bağlı: Tüm puanları göster
        with st.expander("Tüm karakter puanları"):
            st.json(tum_puanlar)