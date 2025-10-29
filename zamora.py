import streamlit as st
from collections import defaultdict

st.set_page_config(layout="wide")

item_type = ['equipment','TA materials','catalysts']

equipment_list = ['sengoku hakase badge','outlaw heart','sweetwater ring',
'absolab hat/overall/shoulder','absolab shoes/glove/cape','absolab weapon','pno secondary']

TA_mat_list = ['black scroll (level 2)','black scroll (level 3)','scroll of secrets','condensed crystal','fine spell essence',
    'grand spell essence','forever unrelenting flame','fragment of destiny','dusk essence','brilliant dusk essence','dream stone',
    'rock of time','sealed wiseman stone','star rock','moon rock','accessory stone','weapon stone','armor stone']
catalyst_list = []

mats = [
    {'black scroll (level 1)':{}},
    {'soul elixir':{}},
    {'power crystal':{}},
    {'wisdom crystal':{}},
    {'dex crystal':{}},
    {'luk crystal':{}},
    {'dark crystal':{}},
    {'mana crystal':{}},
    {'basic spell essence':{}},
    {'unrelenting flame':{}},
    {'twisted time':{}},
    {'dream fragment':{}},
    {'garnet':{}},
    {'amethyst':{}},
    {'aquamarine':{}},
    {'emerald':{}},
    {'opal':{}},
    {'sapphire':{}},
    {'topaz':{}},
    {'diamond':{}},
    {'black crystal':{}},
    {'bronze plate':{}},
    {'steel plate':{}},
    {'mithril plate':{}},
    {'adamantium plate':{}},
    {'orihalcon plate':{}},
    {'sapphire':{}},
    {'silver':{}},
    {'steel':{}},
    {'gold plate':{}},
    {'black crystal':{}},
    {'lidium':{}},
    {'piece of time':{}},
    {'primal essence':{}},
    {'philosopher stone':{}},
    {'sealed saint stone':{}},
    {'sealed warrior stone':{}},
    {'superior lidium heart':{}},
    {'commerci denaro':{}},
    {'monster park mommemorative moin':{}},
    {'gollux coin':{}},
    {'primal essence':{}},
    {'sloth':{}},
    {'envy':{}},
    {'onyx secondary':{}},
    {'black scroll (level 2)': {'black scroll (level 1)':3,
                                  'soul elixir':3}},
    {'black scroll (level 3)': {'black scroll (level 2)':3,
                                  'soul elixir':15}},
    {'scroll of secrets': {'black scroll (level 3)': 2,
                             'soul elixir':18}},
    {'condensed crystal': {'power crystal':2,
                             'wisdom crystal':2,
                             'dex crystal':2,
                             'luk crystal':2,
                             'dark crystal':2,
                             'mana crystal':2,
                             'basic spell essence':3}},
    {'fine spell essence':{'basic spell essence':2,
                             'mana crystal':2,}},
    {'grand spell essence':{'fine spell essence':2,
                              'mana crystal':3}},
    {'forever unrelenting flame':{'unrelenting flame':5,
                                    'twisted time':50,
                                    'soul elixir':1}},
    {'fragment of destiny':{'spark of determination':30,
                              'shadow of annihilation':1}},
    {'dusk essence':{'mana crystal':8,
                       'soul elixir':2}},
    {'brilliant dusk essence': {'dusk essence':5,
                                  'grand spell essence':3,
                                  'soul elixir':1}},
    {'dream stone':{'dream fragment':16,
                    'soul elixir':1}},
    {'rock of time':{'piece of time':10,
                    'soul elixir':1}},
    {'sealed wiseman stone':{'mana crystal':200,
                            'rock of time':27,
                            'wisdom crystal':15,
                            'grand spell essence':12,
                            'brilliant dusk essence':5,
                            'philosopher stone':4,
                            'primal essence':2}},
    {'star rock':{'garnet':3,
                 'amethyst':3,
                 'aquamarine':3,
                 'emerald':3,
                 'opal':3,
                 'sapphire':3,
                 'topaz':3,
                 'diamond':3,
                 'black crstal':3,
                 'soul elixir':1}},
    {'moon rock':{'bronze plate':3,
                 'steel plate':3,
                 'mithril plate':3,
                 'adamantium plate':3,
                 'silver':3,
                 'orihalcon plate':3,
                 'gold':3,
                 'lidium':3,
                 'soul elixir':3}},
    {'accessory stone':{'sealed saint stone':2,
                       'scroll of secrets':1}},
    {'weapon stone':{'sealed warrior stone':3,
                    'scroll of secrets':1}},
    {'armor stone':{'sealed wiseman stone':1,
                   'scroll of secrets':1}},
    {'sengoku hakase badge':{'star rock':30,
               'condensed crystal':30,
               'moon rock':30,
               'accessory stone':4,
               'scroll of secrets':4,
               'magik mirror shard':1}},
    {'outlaw heart':{'superior lidium heart':1,
                    'commerci denaro':1000,
                    'monster park commemorative coin':100,
                    'gollux coin':50,
                     'sealed wiseman stone':4,
                     'sealed warrior stone':4,
                     'sealed saint stone':4}},
    {'sweetwater ring':{'commerci denaro':2000,
                       'condensed crystal':40,
                       'star rock':30,
                       'moon rock':30,
                       'gold':100,
                       'power crystal':100,
                       'black crystal':70,
                       'primal essence':30,
                       'philosopher stone':40,
                       'twisted time':6000,
                        'sealed wiseman stone':3,
                        'sealed warrior stone':3,
                        'sealed saint stone':3}},
    {'absolab hat/overall/shoulder':{'sloth':7,
                                    'grand spell essence':40,
                                    'scroll of secrets':2,
                                    'condensed crystal':35,
                                    'moon rock':35,
                                    'star rock':35,
                                    'primal essence':40,
                                    'twisted time':8000,
                                    'sealed wiseman stone':2,
                                    'sealed warrior stone':2,
                                    'sealed saint stone':2}},
    {'absolab shoes/glove/cape':{'envy':7,
                                'grand spell essence':40,
                                'scroll of secrets':2,
                                'condensed crystal':35,
                                'moon rock':35,
                                'star rock':35,
                                'primal essence':40,
                                'twisted time':8000,
                                'sealed wiseman stone':2,
                                'sealed warrior stone':2,
                                'sealed saint stone':2}},
    {'absolab weapon':{'envy':8,
                      'sloth':8,
                      'grand spell essence':55,
                      'scroll of secrets':3,
                      'condensed crystal':64,
                      'moon rock':64,
                      'star rock':64,
                      'primal essence':50,
                      'philosopher stone':70,
                      'twisted time':9000,
                      'sealed wiseman stone':2,
                       'sealed warrior stone':2,
                       'sealed saint stone':2}},
    {'pno secondary':{'onyx secondary':1,
                     'sloth':1,
                     'envy':1,
                     'scroll of secrets':3,
                     'star rock':25,
                     'moon rock':25,
                     'grand spell essence':60,
                     'sealed wiseman stone':4,
                      'sealed warrior stone':4,
                      'sealed saint stone':4,
                     'primal essence':50,
                     'philosopher stone':100,
                     'twisted time':10000,
                      'mana crystal':300}},
]

materials = {}
for d in mats:
    materials.update(d)
    
def get_base_requirements(item,qty=1):
    if item not in materials:
        return {item:qty}
    
    sub = materials[item]
    if not sub:
        return {item:qty}
    
    total = defaultdict(int)
    for sub_item, sub_qty in sub.items():
        reqs = get_base_requirements(sub_item, qty*sub_qty)
        for k, v in reqs.items():
            total[k]+=v
    return dict(total)

def get_crafting_tree_string(item, qty=1, indent="", is_last=True):
    lines = []
    branch = "└─ " if is_last else "├─ "
    lines.append(f"{indent}{branch}{item} (x{qty})")
    
    sub_materials = materials.get(item, {})
    if not sub_materials:
        return lines  # base material
    
    next_indent = indent + ("   " if is_last else "│  ")
    
    last_index = len(sub_materials) - 1
    for i, (sub_item, sub_qty) in enumerate(sub_materials.items()):
        is_last_sub = i == last_index
        lines.extend(get_crafting_tree_string(sub_item, sub_qty * qty, next_indent, is_last_sub))
    
    return lines

def TA_page():
    st.title('TA help')
    st.divider()
    itemtype = st.selectbox("Choose a category:", options= item_type, placeholder = 'equipment')
    if itemtype == 'equipment':
        item = st.selectbox('Choose the equipment:',options = equipment_list, placeholder = 'outlaw heart')
    if itemtype == 'TA materials':
            item = st.selectbox('Choose the equipment:',options = TA_mat_list, placeholder = 'moon rock')
    if itemtype == 'catalysts':
            item = st.selectbox('Choose the equipment:',options = catalyst_list, placeholder = 'moon rock')
    mat_lines = get_crafting_tree_string(item,1)
    mat_text = "\n".join(mat_lines)
    st.write("Required materials:")
    st.code(mat_text)
    st.write('Total material quantity required:')
    st.write(get_base_requirements(item))

pages = {'TA helper':[
    st.Page(TA_page, title ='TA helper')
]}

pg = st.navigation(pages)
pg.run()
