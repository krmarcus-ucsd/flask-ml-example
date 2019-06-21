from flask import Flask, jsonify, render_template, request
from ml.jaccard import SimilarItemsMlModel
from forms.SimilarItems import SimilarItemsForm

app = Flask(__name__)
app.secret_key = 'development key'

mlModel = SimilarItemsMlModel()


@app.route('/items/similar', methods=['GET', 'POST'])
def similar_item_form():
    form = SimilarItemsForm()
    if request.method == 'POST':
        form.similarItems = mlModel.get_similar_items(form.item_id.data)
    return render_template('similar.html', form=form)


@app.route('/items', defaults={'start_index': 0, 'count': 50}, methods=['GET'])
@app.route('/items/<int:start_index>', defaults={'count': 50}, methods=['GET'])
@app.route('/items/<int:start_index>/<int:count>', methods=['GET'])
def get_items(start_index, count):
    data = {'items': mlModel.get_items(start_index, count),
            'next': start_index + count,
            'previous': start_index - count if start_index - count > 0 else 0}
    return render_template('items.html', data=data)


@app.route('/api/similar/<item_id>', methods=['GET'])
def similar_to_item_api(item_id):
    return jsonify(mlModel.get_similar_items(item_id))


@app.route('/api/items', defaults={'start_index': 0, 'count': 50}, methods=['GET'])
@app.route('/api/items/<int:start_index>', defaults={'count': 50}, methods=['GET'])
@app.route('/api/items/<int:start_index>/<int:count>', methods=['GET'])
def get_items_api(start_index, count):
    return jsonify(mlModel.get_items(start_index, count))


@app.route('/', methods=['GET'])
def index():
    return 'hello from flask!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
