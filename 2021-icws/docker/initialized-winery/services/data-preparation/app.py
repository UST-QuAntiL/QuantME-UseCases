from quart import Quart, request, jsonify
import asyncio
import sys
from fileService import FileService
from wuPalmer import WuPalmerService

app = Quart(__name__)
app.config["DEBUG"] = False
loop = asyncio.get_event_loop()

default_attributes = ['DominanteFarbe', 'DominanterZustand', 'DominanteCharaktereigenschaft', 'DominanterAlterseindruck']


def generate_url(url_root, route, file_name):
    return url_root + '/static/' + route + '/' + file_name + '.txt'


@app.route('/')
async def index():
    return 'QHana Data Preparation Microservice'


@app.route('/api/wu-palmer/<int:job_id>', methods=['POST'])
async def perform_wu_palmer_data_preparation(job_id):
    """
    Trigger the wu palmer data preparation algorithm.
    We have the following parameters (name : type : description):
    input_data_url : string : download location of the input data
    attributes : [string] : the attributes to prepare
    """

    # response parameters
    message = "success"
    status_code = 200

    # load the data from url
    input_data_url = request.args.get('input_data_url', type=str)
    if input_data_url is None:
        input_data_url = (await request.get_json())['data-input_data_url']
    attributes = request.args.get('attributes', type=list)
    if attributes is None:
        attributesResponse = (await request.get_json())
        if attributesResponse is None:
            print('Using default attributes for comparison: ' + str(default_attributes))
            attributes = default_attributes
        else:
            attributes = attributesResponse['data-attributes']

    input_file_path = './static/distance-matrices/muse-input' + str(job_id) + '.csv'
    output_file_path = './static/distance-matrices/distance-matrix' + str(job_id) + '.txt'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/distance-matrices')

        # delete old files if exist
        FileService.delete_if_exist(input_file_path, output_file_path)

        # download the input data and store it locally
        print('Loading input data from URL: ' + str(input_data_url))
        await FileService.download_to_file(input_data_url, input_file_path)
        print('Successfully loaded input data...')

        # deserialize the input data
        entities = FileService.load_entities(input_file_path)
        print('Comparing based on the following attributes: ' + str(attributes))

        # calculate the distance matrix
        await WuPalmerService.wu_palmer_data_preparation(entities, output_file_path, attributes)

        distance_matrix_url = generate_url(request.host_url,
                                           'distance-matrices',
                                           'distance-matrix' + str(job_id))
        print('Result available at URL: ' + distance_matrix_url)

        return jsonify(message=message, status_code=status_code, distance_matrix_url=distance_matrix_url)

    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
        loop.run_until_complete(app.run_task(host="0.0.0.0", port=port))
    except Exception as ex:
        print("Usage: {} <port>".format(sys.argv[0]))
        exit()
