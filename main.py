from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/forgot-password")
def forgot_password():
    return render_template("forgot-password.html")

@app.route("/login")
def login():
    return render_template("login.html")

# Rota para produto com parâmetro de ID dinâmico
@app.route("/product/<int:produto_id>")
def product(produto_id):
    return render_template("product.html", produto_id=produto_id)

@app.route("/register")
def register():
    return render_template("register.html")

# Não executar caso seja importação.
if __name__ == "__main__":
    app.run(debug=True)
