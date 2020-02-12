from flask import Flask
from item import Item
from normal_item import Normal_item
from aged_brie import Aged_brie
from backstage_passes import Backstage_passes
from sulfuras import Sulfuras
from conjured import Conjured
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inventario/')
def inventario():
    return render_template('inventario.html')


@app.route('/updateInventario/')
def updateInventario():
    return render_template('updateInventario.html')
    return 'Lista de objetos en el inventario'


if __name__ == '__main__':
    app.run(debug=True)

    lista_items = Gilded_rose([
        Normal_item("+ 5 Dexterity Vest", 10, 20),
        Aged_brie("Aged Brie", 2, 0),
        Normal_item("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured("Conjured Mana Cake", 3, 6)])
    lista_items.update_quality()
