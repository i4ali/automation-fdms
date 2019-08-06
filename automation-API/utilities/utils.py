
def well_exists_in_polygon(response):
    wells=[]
    for items in response.json():
        wells.append(items['wellName'])
    assert "SHANNON `49` 1" in wells


def data_for_well_exists_in_polygon(response):
    for items in response.json():
        if items['wellName'] == "SHANNON `49` 1":
            assert items['data']['header']
            assert items['data']['clientFormationTops']


def get_well_uid_mapping(response):
    name_uuid_mapping={}
    for well in response.json()["wells"]:
        name_uuid_mapping[well['name']] = well['uuid']
    return name_uuid_mapping


def get_well_uid(response):
    return {"well_uuid": response.json()["wells"][0]["uuid"]}


def assert_finish_status_interpolation(response):
    assert response.json()["interpolation"]["status"] == "FINISHED"


def assert_finish_status_homogenization(response):
    assert response.json()["homogenization"]["status"] == "FINISHED"