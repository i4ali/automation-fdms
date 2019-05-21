
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