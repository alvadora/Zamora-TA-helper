import streamlit as st
from collections import defaultdict

st.set_page_config(layout="wide")

item_type = ['equipment','TA materials','catalysts']

equipment_list = ['sengoku hakase badge','outlaw heart','sweetwater ring','black heart',
                  'absolab hat/overall/shoulder','absolab shoes/glove/cape','absolab weapon',
                  'pno secondary',
                  'arcane hat/overall/shoulder','arcane shoes/glove/cape','arcane weapon', 
                  'genesis weapon']

TA_mat_list = ['black scroll (level 2)','black scroll (level 3)','scroll of secrets','condensed crystal','fine spell essence',
    'grand spell essence','forever unrelenting flame','fragment of destiny','dusk essence','brilliant dusk essence','dream stone',
    'rock of time','sealed wiseman stone','star rock','moon rock','accessory stone','weapon stone','armor stone']

catalyst_list = ['emerald essence','strength essence','magic essence','time essence','stamina essence',
                 'life crystal','wind crystal','star crystal',
                 'dexterity stone','freedom stone','crimson stone','potent ruby','dream ruby','moon element',
                 'rage orb','soul orb','wealth orb','demon orb','evil hammer','soul amplifier']

mats = [
    {'depleted soul stone':{}},
    {'black scroll (level 1)':{}},
    {'soul elixir':{}},
    {'power crystal':{}},
    {'wisdom crystal':{}},
    {'dex crystal':{}},
    {'luk crystal':{}},
    {'dark crystal':{}},
    {'mana crystal':{}},
    {'basic spell essence':{}},
    {'confusion fragment':{}},
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
    {'alchemist stone':{}},
    {'sealed saint stone':{}},
    {'sealed warrior stone':{}},
    {'superior lidium heart':{}},
    {'commerci denaro':{}},
    {'monster park mommemorative coin':{}},
    {'gollux coin':{}},
    {'primal essence':{}},
    {'sloth':{}},
    {'envy':{}},
    {'wrath':{}},
    {'pride':{}},
    {'onyx secondary':{}},
    {'black mage remnnant':{}},
    {'damaged black heart':{}},
    {'superior lidium heart':{}},
    

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
                 'black crystal':3,
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

    {'black heart':{'outlaw heart':1,
                    'damaged black heart':3,
                    'superior lidium heart':2,
                    'commerci denaro':2000,
                    'monster park commemorative coin':200,
                    'gollux coin':100,
                    'sealed wiseman stone':8,
                    'sealed warrior stone':8,
                    'sealed saint stone':8}},

    {'absolab hat/overall/shoulder':{'sloth':7,
                                    'grand spell essence':40,
                                    'scroll of secrets':2,
                                    'condensed crystal':35,
                                    'moon rock':35,
                                    'star rock':35,
                                    'primal essence':40,
                                    'philosopher stone': 60,
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
                                'philosopher stone':60,
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
                      'sealed wiseman stone':4,
                       'sealed warrior stone':4,
                       'sealed saint stone':4}},

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
    
    {'arcane weapon':{'wrath':5,
                      'pride':5,
                      'sloth':3,
                      'envy':3,
                      'grand spell essence':100,
                      'scroll of secrets':4,
                      'condensed crystal':130,
                      'moon rock':130,
                      'star rock':130,
                      'primal essence':130,
                      'philosopher stone':170,
                      'twisted time':19000,
                      'sealed wiseman stone':8,
                      'sealed warrior stone':8,
                      'sealed saint stone':8,
                      'corresponding abso weapon':1,
                      }},

    {'arcane hat/overall/shoulder':{'pride':7,
                                     'sloth':5,
                                     'grand spell essence':90,
                                     'scroll of secrets':4,
                                     'condensed crystal':100,
                                     'moon rock':100,
                                     'star rock':100,
                                     'opal':200,
                                     'sapphire':200,
                                     'primal essence':100,
                                     'philosopher stone':150,
                                     'twisted time':15000,
                                     'sealed wiseman stone':9,
                                     'sealed warrior stone':9,
                                     'sealed saint stone':9,
                                     'corresponding absolab hat/overall/shoulder':1}},

    {'arcane shoes/glove/cape':{'wrath':7,
                                 'envy':5,
                                 'grand spell essence':70,
                                 'scroll of secrets':4,
                                 'condensed crystal':90,
                                 'moon rock':90,
                                 'star rock':90,
                                 'bronze plate':150,
                                 'mithril plate':150,
                                 'primal essence':100,
                                 'philosopher stone':150,
                                 'twisted time':15000,
                                 'sealed wiseman stone':8,
                                 'sealed warrior stone':8,
                                 'sealed saint stone':8,
                                 'corresponding absolab shoes/glove/cape':1}},

    {'genesis weapon':{'wrath':8,
                       'pride':8,
                       'sloth':5,
                       'envy':5,
                       'grand spell essence':150,
                       'scroll of secrets':6,
                       'condensed crystal':200,
                       'moon rock':200,
                       'star rock':200,
                       'corresponding arcane weapon':1,
                       'primal essence':180,
                       'philosopher stone':250,
                       'twisted time':30000,
                       'sealed wiseman stone':12,
                       'sealed warrior stone':12,
                       'sealed saint stone':12,
                       'black mage remnant':3}},
    
    {'emerald essence':{'opal':3,
                        'sapphire':3,
                        'aquamarine':3,
                        'emerald':3,
                        'black scroll (level 1)':1,
                        'soul elixir':1}},

    {'strength essence':{'basic spell essence':3,
                         'power crystal':2,
                         'black scroll (level 1)':1,
                         'soul elixir':1}},

    {'magic essence':{'mana crystal':4,
                      'wisdom crystal':2,
                      'black scroll (level 1)':1}},

    {'time essence':{'twisted time':50,
                     'piece of time':10,
                     'power crystal':1,
                     'wisdom crystal':1,
                     'dex crystal':1,
                     'luk crystal':1,
                     'black scroll (level 1)':1,
                     'soul elixir':1}},

    {'stamina essence':{'garnet':12,
                        'alchemist stone':8,
                        'bronze plate':2,
                        'black scroll (level 1)':1,
                        'soul elixir':1}},

    {'life crystal':{'depleted soul stone':4,
                     'emerald essence':2,
                     'dusk essence':2,
                     'black scroll (level 2)':1,
                     'soul elixir':1}},

    {'wind crystal':{'emerald essence':2,
                     'dusk essence':2,
                     'black scroll (level 2)':1,
                     'soul elixir':1}},

    {'star crystal':{'time essence':2,
                     'strength essence':2,
                     'magic essence':2,
                     'condensed crystal':1,
                     'black scroll (level 2)':1,
                     'soul elixir':2}},

    {'dexterity stone':{'moon rock':5,
                        'wind crystal':1,
                        'black scroll (level 3)':1,
                        'soul elixir':2,
                        'condensed crystal':5}},    

    {'freedom stone':{'condensed crystal':3,
                      'confusion fragment':3,
                      'wind crystal':1,
                      'black scroll (level 3)':1,
                      'soul elixir':3}},

    {'crimson stone':{'moon rock':4,
                      'star rock':4,
                      'star crystal':2,
                      'black scroll (level 3)':1,
                      'forever unrelenting flame':4}},

    {'potent ruby':{'wind crystal':2,
                    'black scroll (level 3)':1,
                    'soul elixir':5,
                    'moon rock':2,
                    'star rock':2}},

    {'dream ruby':{'dream stone':15,
                   'black scroll (level 3)':1,
                   'soul elixir':10}},

    {'moon element':{'gold':10,
                     'brilliant dusk essence':1,
                     'moon rock':3,
                     'star crystal':1,
                     'black scroll (level 3)':1,
                     'star rock':3}},

    {'rage orb':{'lidium':5,
                 'rock of time':10,
                 'moon rock':10,
                 'dark crystal':30,
                 'wisdom crystal':30,
                 'unrelenting flame':10,
                 'black scroll (level 3)':1,}},

    {'soul orb':{'twisted time':300,
                 'confusion fragment':15,
                 'potent ruby':2,
                 'star crystal':1,
                 'sealed warrior stone':1,
                 'black scroll (level 3)':1,
                 'condensed crystal':2,
                 'star rock':2,
                 'moon rock':2}},
                                
    {'wealth orb':{'twisted time':800,
                   'gold':50,
                   'moon rock':3,
                   'star rock':3,
                   'diamond':50,
                   'condensed crystal':3,
                   'sealed wiseman stone':1,
                   'black scroll (level 3)':1,}},

    {'demon orb':{'lidium':6,
                  'stamina essence':4,
                  'life crystal':1,
                  'black scroll (level 3)':1,
                  'soul elixir':2}},

    {'evil hammer':{'moon rock':6,
                    'confusion fragment':15,
                    'condensed crystal':6,
                    'grand spell essence':10,
                    'scroll of secrets':1,
                    'primal essence':2,
                    'forever unrelenting flame':10,
                    'star rock':6,
                    'depleted soul stone':30}},

    {'soul amplifier':{'twisted time':1000,
                       'mana crystal':100,
                       'philosopher stone':15,
                       'forever unrelenting flame':10,
                       'brilliant dusk essence':5,
                       'moon rock':2,
                       'scroll of secrets':1,
                       'sealed saint stone':3,
                       'soul elixir':10,
                       'depleted soul stone':50,
                       'life crystal':1}},

]

materials = {}
for d in mats:
    materials.update(d)
    
def get_base_requirements(item,qty):
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

def get_crafting_tree_string(item, qty, indent="", is_last=True):
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

def material_page():
    st.markdown("<h3 style='text-align: center; color: white;'>ZamoraMS</h3>", unsafe_allow_html=True)
    st.markdown("<h6 style = 'text-align: center; color: white; '>TA Material Calculator</h6>", unsafe_allow_html = True)
    st.divider()
    st.caption("Add items to build a combined materials list")

    col1, col2, = st.columns([3,2], vertical_alignment = 'center')

    # initialize cart in session state
    if 'cart' not in st.session_state:
        st.session_state['cart'] = []

    with col1:
        # Single-selection controls (used to add items to the cart)
        sel_type = st.selectbox("Choose a category:", options= item_type, key='sel_itemtype')
        if sel_type == 'equipment':
            sel_item = st.selectbox('Choose the equipment:', options=equipment_list, key='sel_item')
        if sel_type == 'TA materials':
            sel_item = st.selectbox('Choose the equipment:', options=TA_mat_list, key='sel_item')
        if sel_type == 'catalysts':
            sel_item = st.selectbox('Choose the equipment:', options=catalyst_list, key='sel_item')
        sel_qty = st.number_input('Quantity:',
                                 min_value = 1,
                                 max_value = 999,
                                 value = 1,
                                 step = 1,
                                 key='sel_qty')
    with col2:
        def add_item():
            entry = {'itemtype': st.session_state.get('sel_itemtype', 'equipment'),
                     'item': st.session_state.get('sel_item'),
                     'qty': st.session_state.get('sel_qty', 1)}
            st.session_state.cart.append(entry)

        st.button('Add item', on_click=add_item)

    # display cart and allow removals
    st.divider()
    st.write('Items to include:')
    if st.session_state.cart:
        for i, entry in enumerate(list(st.session_state.cart)):
            cols = st.columns([8,1])
            cols[0].write(f"{i+1}. {entry['item']} (x{entry['qty']}) — {entry['itemtype']}")

            def make_remove(idx):
                def _remove():
                    # remove by index
                    if 0 <= idx < len(st.session_state.cart):
                        st.session_state.cart.pop(idx)
                return _remove

            cols[1].button('Remove', key=f'remove_{i}', on_click=make_remove(i))
    else:
        st.write('No items added yet — use the controls above and click "Add item"')

    # Show crafting paths and totals. If cart empty, show current single selection as before.
    st.divider()
    col3, col4 = st.columns([1,1], vertical_alignment = 'top')
    with col3:
        st.write("Crafting path:")
        if st.session_state.cart:
            # show each item's crafting tree
            for i, entry in enumerate(st.session_state.cart):
                st.write(f"Item {i+1}: {entry['item']} (x{entry['qty']})")
                mat_lines = get_crafting_tree_string(entry['item'], entry['qty'])
                st.code("\n".join(mat_lines))
        else:
            # fallback to current selection
            item = st.session_state.get('sel_item')
            qty = st.session_state.get('sel_qty', 1)
            mat_lines = get_crafting_tree_string(item, qty)
            st.code("\n".join(mat_lines))

    with col4:
        st.write('Total quantity required:')
        combined = defaultdict(int)
        if st.session_state.cart:
            for entry in st.session_state.cart:
                reqs = get_base_requirements(entry['item'], entry['qty'])
                for k, v in reqs.items():
                    combined[k] += v
        else:
            item = st.session_state.get('sel_item')
            qty = st.session_state.get('sel_qty', 1)
            combined = get_base_requirements(item, qty)

        # display as plain lines so strings don't show Python-style quotes
        if combined:
            for k, v in dict(combined).items():
                st.write(f"{k}: {v}")
        else:
            st.write({})

def TA_catalyst_page():
    st.markdown("<h3 style='text-align: center; color: white;'>ZamoraMS</h3>", unsafe_allow_html=True)
    t1_catalyst = ['emerald essence','strength essence','magic essence','time essence','stamina essence']
    t2_catalyst = ['life crystal','wind crystal','star crystal']
    t3_catalyst = ['dexterity stone','freedom stone','crimson stone','potent ruby','dream ruby','moon element','soul orb','demon orb']
    unique_catalyst = ['soul amplifier']
    catalyst_effects = {
        'emerald essence':{'success_rate':4,'type':'addition','equipment':['weapon','accessory','ring']},
        'strength essence':{'attack':6,'success_rate':-3,'type':'addition','equipment':['weapon']},
        'magic essence':{'magic_attack':6,'success_rate':-3,'type':'addition','equipment':['weapon']},
        'time essence':{'all_stats':9,'success_rate':-8,'type':'addition','equipment':['weapon','accessory','ring']},
        'stamina essence':{'max_hp_mp':600,'success_rate':-5,'type':'addition','equipment':['weapon','accessory','ring']},
        'life crystal':{'success_rate':13,'type':'addition','equipment':['weapon','accessory','ring']},
        'wind crystal':{'attack':7,'magic_attack':7,'success_rate':-15,'type':'addition','equipment':['weapon','accessory','ring']},
        'star crystal':{'all_stats':25,'attack':18,'magic_attack':18,'success_rate':-15,'type':'addition','equipment':['weapon']},
        'dexterity stone':{'all_stats':1.05,'success_rate':-32,'type':'multiplication','equipment':['accessory']},
        'freedom stone':{'IED':1.2,'success_rate':-25,'type':'multiplication','equipment':['heart']},
        'crimson stone':{'attack':1.2,'magic_attack':1.2, 'success_rate':-40,'type':'multiplication','equipment':['weapon']},
        'potent ruby':{'attack':13,'magic_attack':13,'success_rate':-30,'type':'addition','equipment':['weapon','accessory','ring','armor']},
        'dream ruby':{'attack':1.05,'magic_attack':1.05,'success_rate':0,'type':'multiplication','equipment':['weapon']},
        'moon element':{'boss_damage':1.2,'success_rate':-25,'type':'multiplication','equipment':['heart']},
        'soul orb':{'attack':1.15,'magic_attack':1.15,'all_stats':1.3,'type':'multiplication','success_rate':-45,'equipment':['accessory']},
        'demon orb':{'max_hp_mp':2500,'success_rate':-20,'type':'addition','equipment':['weapon','accessory','ring']},
        'soul amplifier':{'success_rate':32,'type':'addition','equipment':['weapon','accessory','ring']}
    }

    # ensure cart exists and is a list
    if 'cart' not in st.session_state:
        st.session_state['cart'] = []

    st.markdown("#### Catalyst selection")

    tier = st.radio("Choose catalyst tier:", options=['T1', 'T2', 'T3', 'Unique'], horizontal=True)

    choices = []
    if tier == 'T1':
        choices = t1_catalyst
    elif tier == 'T2':
        choices = t2_catalyst
    elif tier == 'T3':
        choices = t3_catalyst
    else:
        choices = unique_catalyst

    selected = st.multiselect("Select catalysts to add:", options=choices, key='sel_cats')
    qty = st.number_input('Quantity for each selected catalyst:', min_value=1, max_value=5, value=1, step=1, key='cat_qty')

    def add_selected():
        # enforce only a total-quantity cap (max 5 units total across all catalyst entries)
        selected_names = st.session_state.get('sel_cats', [])
        if not selected_names:
            return

        existing = [e for e in st.session_state.cart if e.get('itemtype') == 'catalyst']
        current_total_qty = sum(int(e.get('qty', 1)) for e in existing)

        max_total_qty = 5
        qty_left = max_total_qty - current_total_qty

        if qty_left <= 0:
            st.warning(f"Cannot add catalysts: total quantity limit ({max_total_qty}) already reached.")
            return

        added = 0
        added_units = 0
        requested_qty = int(st.session_state.get('cat_qty', 1))

        for name in selected_names:
            if qty_left <= 0:
                break

            # determine how many units to add for this entry (can't exceed qty_left)
            unit_to_add = min(requested_qty, qty_left)

            if unit_to_add <= 0:
                break

            entry = {'itemtype': 'catalyst', 'item': name, 'tier': tier, 'qty': unit_to_add}
            st.session_state.cart.append(entry)

            qty_left -= unit_to_add
            added += 1
            added_units += unit_to_add

        if added == 0:
            st.warning("No catalysts were added due to limits.")
        else:
            if added < len(selected_names):
                st.warning(f"Added {added} catalyst(s) ({added_units} unit(s)); some selections were skipped due to quantity limits.")
            elif added_units < requested_qty * len(selected_names):
                st.info(f"Added {added} catalyst(s) with reduced quantities to respect the total quantity cap ({max_total_qty}).")

    st.button('Add selected catalysts to cart', on_click=add_selected)

    st.divider()

    st.write('Catalyst cart:')
    # show only catalyst entries
    catalyst_entries = [e for e in st.session_state.cart if e.get('itemtype') == 'catalyst']
    if catalyst_entries:
        for i, entry in enumerate(list(catalyst_entries)):
            cols = st.columns([6,1,1])
            cols[0].write(f"{i+1}. {entry['item']} (tier {entry['tier']}) x{entry['qty']}")

            def make_remove(idx):
                def _remove():
                    # remove the idx-th catalyst occurrence among catalysts
                    # find actual global index in session cart
                    count = -1
                    for gi, ge in enumerate(st.session_state.cart):
                        if ge.get('itemtype') == 'catalyst':
                            count += 1
                        if count == idx:
                            st.session_state.cart.pop(gi)
                            break
                return _remove

            cols[1].button('Remove', key=f'remove_cat_{i}', on_click=make_remove(i))
            # allow quick quantity edit
            def make_update(idx):
                def _update():
                    # show a small prompt isn't possible; instead skip complex inline edits for now
                    pass
                return _update
            cols[2].button('Edit', key=f'edit_cat_{i}', on_click=make_update(i))
    else:
        st.write('No catalysts added yet.')

    st.divider()

    # compute cumulative effects and success rate
    additive = defaultdict(float)
    multiplicative = defaultdict(lambda: 1.0)
    total_success = 0.0

    # compute per-unit ordering for success-rate penalties
    # build a flat ordered list of unit names (each unit represents one catalyst unit)
    unit_list = []
    for entry in catalyst_entries:
        name = entry.get('item')
        qty = int(entry.get('qty', 1))
        for _ in range(qty):
            unit_list.append(name)

    # only consider up to max_total_units (should be <=5 by add logic)
    max_total_units = 5
    unit_list = unit_list[:max_total_units]

    # first compute additive and multiplicative effects using quantities
    for entry in catalyst_entries:
        name = entry['item']
        qty = int(entry.get('qty', 1))
        eff = catalyst_effects.get(name, {})
        ctype = eff.get('type', 'addition')

        for k, v in eff.items():
            if k in ('type', 'equipment', 'success_rate'):
                continue
            try:
                val = float(v)
            except Exception:
                continue

            if ctype == 'multiplication':
                multiplicative[k] *= (val ** qty)
            else:
                additive[k] += val * qty

    # now compute success rate per unit (so 4th and 5th units get extra -8%)
    for idx, unit_name in enumerate(unit_list):
        eff = catalyst_effects.get(unit_name, {})
        sr = float(eff.get('success_rate', 0.0))
        # extra penalty for 4th (idx==3) and 5th (idx==4) unit
        if idx in (3, 4):
            sr -= 8.0
        total_success += sr

    st.write('Cumulative catalyst effects:')
    col_a, col_b = st.columns(2)
    with col_a:
        st.write('Additive bonuses:')
        if additive:
            for k, v in additive.items():
                # display integers without decimal when appropriate
                if abs(v - round(v)) < 1e-8:
                    v_display = int(round(v))
                else:
                    v_display = round(v, 4)
                st.write(f"{k}: {v_display}")
        else:
            st.write('None')

    with col_b:
        st.write('Multiplicative bonuses:')
        if multiplicative:
            for k, v in multiplicative.items():
                st.write(f"{k}: {round(v,4)}x")
        else:
            st.write('None')


    st.divider()
    st.write("Assuming you have 900 TA exp giving you 155% chance to succeed without any catalysts")
    st.write(f"Success rate: {round(155+total_success,2)} %")

    # --- Item stat input and expected value calculation ---
    st.markdown('#### Item Stat Calculator')
    st.markdown('Remember to always apply your additive catalysts before multiplicative ones!')
    with st.form('item_stats_form'):
        base_stats = st.number_input('Base All Stats', min_value=0, value=0, step=1)
        base_attack = st.number_input('Base Attack', min_value=0, value=0, step=1)
        base_magic = st.number_input('Base Magic Attack', min_value=0, value=0, step=1)
        submitted = st.form_submit_button('Calculate Expected Value')

    if submitted:
        # For each stat, determine if additive or multiplicative from catalyst_effects type
        def get_final_stat(stat_name, base_value):
            add_total = 0.0
            mult_total = 1.0
            for entry in catalyst_entries:
                name = entry['item']
                qty = int(entry.get('qty', 1))
                eff = catalyst_effects.get(name, {})
                ctype = eff.get('type', 'addition')
                if stat_name in eff:
                    try:
                        val = float(eff[stat_name])
                    except Exception:
                        val = 0.0
                    if ctype == 'addition':
                        add_total += val * qty
                    elif ctype == 'multiplication':
                        mult_total *= val ** qty
            return (base_value + add_total) * mult_total

        final_stats = get_final_stat('all_stats', base_stats)
        final_attack = get_final_stat('attack', base_attack)
        final_magic = get_final_stat('magic_attack', base_magic)
        final_hpmp = get_final_stat('max_hp_mp', 0)

        st.write(f"Expected All Stats= {final_stats}, Expected Attack = {final_attack}, Expected Magic Attack = {final_magic}, Expected HP/MP = {final_hpmp}")


                            
pages = {'All things TA NPC related':[
    st.Page(material_page, title ='TA material calculator'),
    st.Page(TA_catalyst_page, title = 'TA catalyst calculator'),
]}

pg = st.navigation(pages)
pg.run()














