import json
from collections import OrderedDict


district = open('Tanzania/Districts.json', 'rb')
dict_distric = json.load(district)
length_dict = len(dict_distric['Distr'])


all_rg = []

for i in range(length_dict):
    dt = dict_distric['Distr'][i]['properties']

    dtl = list(dt['region'])
    for x in dtl:
        if x not in all_rg:
            all_rg.append(x)

    print(len(all_rg))
    # print(len(dtl))
# good up to now
    # print(dt['region'])

# print(len(dict_distric['Distr']))

'''
length_dict = len(dict_distric['Distr'])


class District():
    regions = []


    def all_regions(self):
        for x in range(length_dict):
            all_reg = dict_distric['Distr'][x]['properties']['region']

            # print(all_reg.split('Region'))

            regions = list(all_reg.split())

            print(regions)
            

            # for i in regions:
            #     if i not in reg:
            #         reg.append(i)
            # print(reg)
            # print([dict.fromkeys(regions)])
            # regions = self.regions
            # rg = regions.append(all_reg)
            # print(all_reg)
            # print(type(new))


        # return all_reg

obj = District()
obj.all_regions()



'''