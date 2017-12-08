import json
def menu_project(filename):
        with open(filename) as f:
                try:
                        menu_text = json.load(f)
                        pass
                        result = []
                        for i in range(len(menu_text)):
                                menu_sum = 0
                                for item in menu_text[i]['menu']['items']:
                                        if item is not None and 'label' in item and 'id' in item and type(item['id']) == int and 0 <= item['id'] <= 100 :
                                                menu_sum += item['id']
                                result.append(menu_sum)
                        if result == []:
                                return 'No data is available.'
                        else:
                                return result
                except ValueError:
                    return('This is invalid json. Try again.')
