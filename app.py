from flask import Flask, render_template, request

from epidemic_spider import EpidemicSpider



app = Flask(__name__)

epidemic_spider = EpidemicSpider()

@app.route("/", methods=["GET", "POST"])
def epidemic():
    # Epidemic function page
    if request.method == "GET":
        return render_template("about-epidemic.html")

    if request.method == "POST":
        get_data = request.get_json()
        print(get_data)
        if get_data["newstype"] == "rumors":
            return epidemic_spider.get_rumors(f"https://lab.isaaclin.cn/nCoV/api/rumors?page={get_data['page']}")
        elif get_data["newstype"] == "news":
            return epidemic_spider.get_news(f"https://lab.isaaclin.cn/nCoV/api/news?page={str(get_data['page'])}")
        elif get_data["newstype"] == "overall":
            return epidemic_spider.get_overall("https://lab.isaaclin.cn/nCoV/api/overall")
        else:
            return epidemic_spider.get_data("https://lab.isaaclin.cn/nCoV/api/area?latest=1")

if __name__ == "__main__":
    app.run(debug=True) 
