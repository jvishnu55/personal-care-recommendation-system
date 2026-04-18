from flask import Flask, render_template, request

app = Flask(__name__)

# -----------------------------
# FACE PRODUCTS (FULL)
# -----------------------------
face_products = {
    "dry": {
        "facewash": ["Cetaphil Gentle Cleanser", "Dove Hydrating Face Wash"],
        "serum": ["Hyaluronic Acid Serum", "Vitamin E Serum"],
        "moisturizer": ["CeraVe Moisturizing Cream", "Nivea Soft Cream"]
    },
    "oily": {
        "facewash": ["Himalaya Neem Face Wash", "Clean & Clear Foaming Wash"],
        "serum": ["Niacinamide Serum", "Salicylic Acid Serum"],
        "moisturizer": ["Oil-Free Moisturizer", "Neutrogena Hydro Boost"]
    },
    "normal": {
        "facewash": ["Simple Face Wash", "Cetaphil Daily Cleanser"],
        "serum": ["Vitamin C Serum", "Niacinamide Serum"],
        "moisturizer": ["Aloe Vera Gel", "Light Moisturizer"]
    },
    "combination": {
        "facewash": ["Plum Green Tea Face Wash", "Mamaearth Tea Tree Wash"],
        "serum": ["Niacinamide Serum", "Vitamin C Serum"],
        "moisturizer": ["Gel Moisturizer", "Light Cream"]
    },
    "sensitive": {
        "facewash": ["Cetaphil Gentle Cleanser", "Aveeno Calm Wash"],
        "serum": ["Hyaluronic Acid Serum"],
        "moisturizer": ["Fragrance-Free Moisturizer"]
    }
}

# -----------------------------
# HAIR PRODUCTS (FULL)
# -----------------------------
hair_products = {
    "straight": {
        "shampoo": ["L'Oreal Smooth Shampoo", "Pantene Smooth Care"],
        "conditioner": ["Lightweight Conditioner", "Silk Smooth Conditioner"],
        "oil": ["Coconut Oil", "Almond Oil"],
        "serum": ["L'Oreal Hair Serum", "Streax Hair Serum"]
    },
    "wavy": {
        "shampoo": ["OGX Coconut Shampoo", "Herbal Essences"],
        "conditioner": ["Hydrating Conditioner"],
        "oil": ["Argan Oil", "Jojoba Oil"],
        "serum": ["Livon Serum", "Argan Hair Serum"]
    },
    "curly": {
        "shampoo": ["Shea Moisture Shampoo"],
        "conditioner": ["Curl Conditioner"],
        "oil": ["Castor Oil", "Argan Oil"],
        "serum": ["Curl Serum"]
    },
    "coily": {
        "shampoo": ["Shea Moisture Intensive"],
        "conditioner": ["Deep Conditioner"],
        "oil": ["Castor Oil"],
        "serum": ["Growth Serum"]
    }
}

# -----------------------------
# RECOMMEND FUNCTIONS
# -----------------------------
def recommend_face(age, skin):
    rec = face_products.get(skin, {})

    serum = rec.get("serum", []).copy()

    # Age-based addition
    if age > 30:
        serum.append("Retinol Serum (Anti-Aging)")

    return {
        "Face Wash": rec.get("facewash", []),
        "Serum": serum,
        "Moisturizer": rec.get("moisturizer", [])
    }

def recommend_hair(age, hair):
    rec = hair_products.get(hair, {})

    serum = rec.get("serum", []).copy()

    # Age-based addition
    if age > 25:
        serum.append("Biotin Hair Growth Serum")

    return {
        "Shampoo": rec.get("shampoo", []),
        "Conditioner": rec.get("conditioner", []),
        "Hair Oil": rec.get("oil", []),
        "Hair Serum": serum
    }

# -----------------------------
# ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        choice = request.form["choice"]
        age = int(request.form["age"])

        if choice == "face":
            skin = request.form["skin"]
            result = recommend_face(age, skin)

        elif choice == "hair":
            hair = request.form["hair"]
            result = recommend_hair(age, hair)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)