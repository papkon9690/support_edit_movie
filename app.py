from flask import Flask, render_template, request
import convert_img as ci

# flaskの定義
templates_path = "templates/"
static_path = "static/"
app = Flask(__name__ , template_folder=templates_path, static_folder=static_path)

# パスの定義
img_folder = static_path + "img/"


@app.route('/', methods=['GET', 'POST'])
def add_telop():
    input_img_path = img_folder + "input.png"
    output_img_path = img_folder + "output.png"

    if request.method == 'POST':
        # フォームからデータを取得
        telop_text = request.form['telop_text']
        img_file_data = request.files['img_file']
        img_file_data.save(input_img_path)

        ci.draw_telop_and_add_img(telop_text , input_img_path , output_img_path)

        return render_template(
            "add_telop.html" ,
            output_img_path  = output_img_path ,
        )
    
    return render_template("add_telop.html")




if __name__ == "__main__":
    port_number = 6600
    app.run(port = port_number , debug=True)

