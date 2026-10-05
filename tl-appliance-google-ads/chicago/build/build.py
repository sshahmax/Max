# -*- coding: utf-8 -*-
"""
Builds a brand-new Google Ads Editor import for TL Appliance Repair — Chicago.
Output: 3 CSV files (main / locations / negatives) in ./out
"""
import csv, os, re, difflib, collections

OUT = 'out'
os.makedirs(OUT, exist_ok=True)

CAMPAIGN = 'TL-CHI | Luxury Appliance Repair'
BASE = 'https://tappliancerepair.site/chicago/'
ROOT = 'https://tappliancerepair.site/'
PHONE = '(847) 834-6513'
BUDGET = '300.00'
SUFFIX = ('utm_source=google&utm_medium=cpc&utm_campaign=tl-chi-lux'
          '&utm_content={adgroupid}_{creative}&utm_term={keyword}'
          '&mt={matchtype}&dev={device}&net={network}&kwid={targetid}'
          '&geo={loc_physical_ms}&geoi={loc_interest_ms}')

# ----------------------------------------------------------------------------
# Areas for "{brand} + area" keywords (Exact only)
# ----------------------------------------------------------------------------
AREAS = [
    'chicago', 'chicago il', 'chicagoland', 'north shore', 'lincoln park', 'gold coast',
    'lakeview', 'river north', 'streeterville', 'old town', 'hyde park', 'bucktown',
    'wicker park', 'west loop', 'south loop', 'logan square', 'lincoln square',
    'ravenswood', 'edgewater', 'andersonville', 'evanston', 'oak park', 'river forest',
    'skokie', 'wilmette', 'winnetka', 'glencoe', 'kenilworth', 'highland park',
    'lake forest', 'lake bluff', 'northbrook', 'glenview', 'deerfield', 'park ridge',
    'arlington heights', 'barrington', 'inverness', 'long grove', 'libertyville',
    'hinsdale', 'oak brook', 'burr ridge', 'clarendon hills', 'western springs',
    'la grange', 'elmhurst', 'downers grove', 'naperville', 'wheaton', 'glen ellyn',
    'palos park', 'orland park', 'schaumburg', 'lincolnshire',
]

# ----------------------------------------------------------------------------
# Generic headline / description pools (two variants: A and B — never mixed)
# ----------------------------------------------------------------------------
TRUST_A = [
    'Exact Quote Before Any Work',
    'Labor Backed For 90 Days',
    'Genuine Parts, Not Generics',
    'Visit Fee Counts Toward Repair',
]
TRUST_B = [
    'You Approve The Price First',
    '90 Days On Every Labor Job',
    'Genuine Parts Ride Along',
    'Not A Manufacturer Network',
]
LOCAL_A = [
    'Chicago & Suburbs Covered',
    'Calls Taken Around The Clock',
    'Book A Visit In Two Minutes',
]
LOCAL_B = [
    'North Shore To Hinsdale',
    'Dispatcher Picks Up 24/7',
    'Same-Day Slots When Available',
]
DESC_A = [
    'Techs based around Chicago, from Evanston to Naperville. You hear the exact price and say yes before we start.',
    'Diagnostic fee quoted when you book and credited to the repair. Labor covered for 90 days, parts by their maker.',
]
DESC_B = [
    'An independent repair company, not a manufacturer network. Genuine parts, written price, 90 days on labor.',
    'Phone answered day and night. Same-day or next-day openings across most of Chicago and the suburbs.',
]

# ----------------------------------------------------------------------------
# Ad groups
#   key, name, url path (relative to BASE or absolute), max cpc, path1, path2,
#   keywords (core, Exact+Phrase), area_brand (None or brand phrase list for area combos),
#   pos1 (3 headlines, first two pinned to position 1), spec (6 headlines),
#   dA (2 descriptions for ad A), dB (2 descriptions for ad B)
# ----------------------------------------------------------------------------
G = []

def grp(name, url, cpc, p1, p2, kws, pos1, spec, dA, dB, area_brand=None, area_tpl=None):
    G.append(dict(name=name, url=url if url.startswith('http') else BASE + url, cpc=cpc,
                  p1=p1, p2=p2, kws=kws, pos1=pos1, spec=spec, dA=dA, dB=dB,
                  area_brand=area_brand, area_tpl=area_tpl))

# ============================== SUB-ZERO ====================================
grp('Sub-Zero > Fridge Repair', 'sub-zero/refrigerator-repair/', '42.00', 'SubZero', 'Fridge',
    ['sub zero refrigerator repair', 'sub zero fridge repair', 'subzero refrigerator repair',
     'sub-zero refrigerator repair', 'sub zero refrigerator repair near me', 'sub zero fridge repair near me',
     'sub zero built in refrigerator repair', 'sub zero refrigerator service', 'sub zero refrigerator technician',
     'sub zero refrigerator not working', 'sub zero fridge not working', 'sub zero refrigerator repair service',
     'sub zero refrigerator repairman', 'sub zero refrigerator making noise', 'sub zero refrigerator too cold',
     'sub zero temperature fluctuating', 'sub zero door gasket replacement', 'sub zero door not sealing',
     'sub zero door hinge repair', 'sub zero control board replacement', 'sub zero fan motor replacement',
     'sub zero water dispenser not working', 'sub zero service light on', 'fix sub zero refrigerator', 'repair sub zero refrigerator', 'sub zero refrigerator repair cost',
     'sub zero fridge technician', 'sub zero refrigerator repair chicago', 'sub zero fridge repair chicago'],
    ['Sub-Zero Fridge Repair Chicago', 'Sub-Zero Refrigerator Fixes', 'Built-In Sub-Zero Fridge Help'],
    ['Warm Shelves, Cold Freezer?', 'Noisy Fan Or Dead Board? Fixed', 'Gasket Swaps Done In-Kitchen',
     'Temps Drifting Up And Down?', 'Water Dispenser Quit Working?', 'Classic, Designer & PRO 48'],
    ['Sub-Zero fridge running warm, sweating or humming loudly? Both cooling circuits are tested one by one.',
     'Gaskets, hinges, fan motors and boards replaced right in your kitchen. Sealed-system faults confirmed first.'],
    ['Service light on, temps swinging or a door that will not stay shut: we find the actual cause, then quote.',
     'Columns, built-ins and refrigerator drawers. Parts stocked for common Sub-Zero failures, so most jobs end in one visit.'])

grp('Sub-Zero > Not Cooling', 'sub-zero/refrigerator-repair/', '42.00', 'SubZero', 'NotCooling',
    ['sub zero not cooling', 'sub zero refrigerator not cooling', 'sub zero fridge not cooling',
     'sub zero not getting cold', 'sub zero refrigerator not cold', 'sub zero fridge not cold',
     'sub zero refrigerator warm', 'sub zero fridge warm', 'sub zero warm inside', 'sub zero refrigerator too warm',
     'sub zero stopped cooling', 'sub zero not cooling after power outage',
     'sub zero refrigerator not cooling but freezer works', 'sub zero freezer works but fridge warm',
     'sub zero not working', 'sub zero refrigerator stopped working', 'sub zero refrigerator not cooling properly',
     'sub zero not cooling enough', 'sub zero fridge side warm', 'sub zero refrigerator not staying cold',
     'sub zero compartment too warm', 'sub zero not cooling chicago'],
    ['Sub-Zero Not Cooling? Chicago', 'Sub-Zero Fridge Gone Warm?', 'Sub-Zero Stopped Cooling Help'],
    ['Milk Spoiling Too Fast?', 'Freezer Fine, Fridge Warm?', 'Evaporator Iced Over? Thawed',
     'Compressor Running Nonstop?', 'Clogged Condenser Cleared', 'Temp Sensors Tested & Swapped'],
    ['Fridge side warm while the freezer holds? That points to one circuit. We test it and tell you what failed.',
     'Dirty condenser, iced evaporator, dead fan or a failed board: each checked in order, fixed with OEM parts.'],
    ['A Sub-Zero that stopped cooling after an outage or a storm is often a quick fix. We say so before you pay.',
     'Warm compartment, long run times, frost where it should not be: diagnosed at your home, priced before work.'])

grp('Sub-Zero > Freezer Repair', 'sub-zero/freezer-repair/', '40.00', 'SubZero', 'Freezer',
    ['sub zero freezer repair', 'sub zero freezer not freezing', 'sub zero freezer not cold', 'sub zero freezer not working',
     'sub zero freezer too warm', 'sub zero freezer frost buildup', 'sub zero freezer frosting up',
     'sub zero freezer drawer repair', 'sub zero freezer service', 'sub zero freezer technician',
     'sub zero freezer repair near me', 'sub zero freezer defrost problem', 'sub zero freezer column repair',
     'sub zero freezer ice buildup', 'sub zero freezer thawing', 'sub zero freezer temperature rising', 'sub zero freezer door not closing', 'sub zero freezer alarm',
     'sub zero freezer repair chicago'],
    ['Chicago Sub-Zero Freezer Fix', 'Sub-Zero Freezer Not Freezing?', 'Sub-Zero Freezer Column Help'],
    ['Ice Cream Soft, Frost Thick?', 'Defrost Circuit Restored', 'Freezer Drawer Off Its Track?',
     'Snow On The Back Wall? Call', 'Door Alarm Will Not Stop?', 'Temps Climbing Overnight?'],
    ['Soft ice cream, frost sheets or a freezer alarm that keeps chiming: the defrost system is checked first.',
     'Freezer drawers, columns and bottom freezers. Heaters, thermostats, fans and seals replaced with OEM parts.'],
    ['A freezer losing cold overnight usually has one failed part. We find it, quote it, and fix it that visit if stocked.',
     'Frost build-up is a symptom, not the problem. We trace it to the seal, heater or sensor and fix the cause.'])

grp('Sub-Zero > Ice Maker Repair', 'sub-zero/ice-maker-repair/', '38.00', 'SubZero', 'IceMaker',
    ['sub zero ice maker repair', 'sub zero ice maker not working', 'sub zero ice maker not making ice',
     'sub zero not making ice', 'sub zero ice maker frozen', 'sub zero ice maker leaking', 'sub zero ice maker slow',
     'sub zero ice maker replacement', 'sub zero ice maker service', 'sub zero ice machine repair',
     'sub zero undercounter ice maker repair', 'sub zero uc 15 repair', 'sub zero uc-15i repair',
     'sub zero ice maker repair near me', 'sub zero ice maker technician', 'sub zero ice maker stopped working',
     'sub zero ice maker not dispensing', 'sub zero ice maker not filling with water', 'sub zero ice maker small cubes',
     'sub zero ice maker hollow cubes', 'sub zero ice maker clumping', 'sub zero ice maker repair chicago'],
    ['Sub-Zero Ice Maker Fixes', 'Sub-Zero Not Making Ice?', 'Sub-Zero Ice Machine Service'],
    ['Empty Bin Every Morning?', 'Hollow Or Tiny Cubes? Solved', 'Inlet Valve & Supply Tested',
     'UC-15 Undercounter Units Too', 'Ice Clumping Into One Block?', 'Harvest Cycle Stuck? We Reset'],
    ['No ice, slow ice or cloudy cubes: the fill valve, inlet line, mold heater and controls are tested in order.',
     'Built-in ice makers and UC-15 undercounter machines. Replacement units installed when a rebuild is not worth it.'],
    ['Ice maker frozen solid or leaking under the bin? Fixed with genuine parts and a price you approve first.',
     'Water pressure, filter, ejector arm and sensor all checked so the repair holds. 90 days on our labor.'])

grp('Sub-Zero > Wine Storage Repair', 'sub-zero/wine-storage-repair/', '38.00', 'SubZero', 'Wine',
    ['sub zero wine cooler repair', 'sub zero wine fridge repair', 'sub zero wine refrigerator repair',
     'sub zero wine storage repair', 'sub zero wine cellar repair', 'sub zero wine cooler not cooling',
     'sub zero wine cooler too warm', 'sub zero wine cooler service', 'sub zero wine unit repair',
     'sub zero wine cooler repair near me', 'sub zero wine column repair', 'sub zero wine cooler not working',
     'sub zero wine fridge not cold', 'sub zero wine storage not cooling', 'sub zero 427 repair',
     'sub zero wine cooler humming', 'sub zero wine cooler temperature wrong', 'sub zero undercounter wine repair',
     'sub zero wine cooler repair chicago'],
    ['Sub-Zero Wine Cooler Repair', 'Sub-Zero Wine Column Service', 'Sub-Zero Wine Storage Fixes'],
    ['Collection Creeping Warm?', 'Both Zones Holding Steady', 'Humidity Or Vibration Issues?',
     'UV Glass Door Not Sealing?', 'Undercounter & Full Columns', 'Thermostats & Fans Replaced'],
    ['Wine column drifting warm or cycling loudly? Each zone is measured and the fault isolated before any quote.',
     'Undercounter wine fridges, 24-inch and 30-inch columns. Fans, sensors, boards and door seals replaced in place.'],
    ['Your bottles should sit at a steady 55. We restore both zones and show you the reading before we leave.',
     'Wine storage is a priority call: we aim for the first open slot so the collection does not keep warming.'])

grp('Sub-Zero > Leaks & Frost', 'sub-zero/refrigerator-repair/', '40.00', 'SubZero', 'Leaking',
    ['sub zero leaking water', 'sub zero leaking', 'sub zero refrigerator leaking', 'sub zero leaking inside',
     'sub zero water on floor', 'sub zero water leak repair', 'sub zero drain clogged', 'sub zero freezer leaking water',
     'sub zero leaking water inside fridge', 'sub zero refrigerator leaking water', 'sub zero fridge leaking',
     'sub zero water under crisper', 'sub zero drain line frozen', 'sub zero puddle on floor',
     'sub zero condensation inside', 'sub zero sweating door', 'sub zero frost inside refrigerator',
     'sub zero ice inside fridge', 'sub zero leaking chicago'],
    ['Sub-Zero Leaking Water? Call', 'Sub-Zero Puddle On The Floor?', 'Sub-Zero Leak Repair Chicago'],
    ['Puddle Beneath The Drawers?', 'Frozen Drain Line Cleared', 'Sweating Doors & Wet Gaskets',
     'Drip Pan & Tube Inspected', 'Frost Inside The Fridge Box?', 'Floors Protected, Mess Removed'],
    ['Water on the floor or under the drawers? Usually a blocked or frozen drain. Cleared and tested the same visit.',
     'Condensation, frost patches and drips come from seals, heaters or drain lines. We fix the source, not the symptom.'],
    ['Catch a leak early and the floor survives. We arrive with drain tools, heaters and gaskets for Sub-Zero models.',
     'A Sub-Zero should never sweat or drip. We find the failed part, quote it in writing, then do the work.'])

grp('Sub-Zero > Compressor & Sealed System', 'sub-zero/refrigerator-repair/', '44.00', 'SubZero', 'Compressor',
    ['sub zero compressor repair', 'sub zero compressor replacement', 'sub zero compressor not running',
     'sub zero compressor cost', 'sub zero sealed system repair', 'sub zero freon leak', 'sub zero refrigerant leak',
     'sub zero condenser repair', 'sub zero evaporator repair', 'sub zero compressor failure',
     'sub zero refrigerator compressor', 'sub zero evaporator fan replacement', 'sub zero condenser fan motor',
     'sub zero compressor replacement cost', 'sub zero refrigerator compressor replacement',
     'sub zero compressor hot', 'sub zero compressor clicking', 'sub zero compressor noise',
     'sub zero low refrigerant', 'sub zero recharge freon', 'sub zero sealed system technician',
     'sub zero compressor repair chicago'],
    ['Sub-Zero Compressor Service', 'Sub-Zero Sealed System Work', 'Sub-Zero Compressor Replaced'],
    ['Compressor Clicking Or Silent?', 'Refrigerant Leaks Located', 'Coil Replacement Done Right',
     'Repair Or Replace? Honest Call', 'Dual Compressor Models Served', 'Vacuum, Charge & Verify'],
    ['Compressor hot, clicking or silent? We confirm it is really the compressor before quoting a sealed-system job.',
     'Leak found, system evacuated, part replaced, recharged and verified. OEM compressors with the price agreed first.'],
    ['A sealed-system repair is a big decision. You get the exact figure and a straight answer on repair versus replace.',
     'Dual-compressor Sub-Zero built-ins: one side can fail alone. We fix that side only, so you pay for what broke.'])

grp('Sub-Zero > Installation & Replacement', 'sub-zero/installation/', '34.00', 'SubZero', 'Install',
    ['sub zero installation', 'sub zero install', 'sub zero installer', 'sub zero refrigerator installation',
     'sub zero built in installation', 'sub zero panel installation', 'install sub zero refrigerator',
     'sub zero replacement', 'sub zero refrigerator replacement', 'sub zero installation near me',
     'sub zero installation service', 'sub zero refrigerator installer', 'sub zero installers near me',
     'sub zero column installation', 'sub zero integrated installation', 'sub zero removal and installation',
     'sub zero door panel alignment', 'sub zero water line installation', 'sub zero installation chicago',
     'sub zero installer chicago', 'replace old sub zero'],
    ['Sub-Zero Installation Chicago', 'Sub-Zero Installers Near You', 'Swap Out An Old Sub-Zero'],
    ['Panels Aligned, Doors Leveled', 'Water Line & Leveling Included', 'Old Unit Hauled Away',
     'Columns & Integrated Models', 'Built-In Fit Checked First', 'Install Date Set When You Call'],
    ['Installing a new Sub-Zero or replacing a tired one? We handle removal, set, leveling, panels and the water line.',
     'Integrated columns and classic built-ins fitted flush, doors aligned, cooling verified before we leave.'],
    ['Cabinet cutout, power and water checked before install day, so the unit goes in once and goes in right.',
     'Flat installation price agreed up front. Old refrigerator removed, new one tested and running when we go.'])

grp('Sub-Zero > Series & Models', 'sub-zero/refrigerator-repair/', '40.00', 'SubZero', 'Models',
    ['sub zero pro 48 repair', 'sub zero 600 series repair', 'sub zero 700 series repair', 'sub zero 500 series repair',
     'sub zero 400 series repair', 'sub zero classic series repair', 'sub zero designer series repair',
     'sub zero column refrigerator repair', 'sub zero integrated refrigerator repair', 'sub zero built in repair',
     'sub zero 48 inch refrigerator repair', 'sub zero 42 inch refrigerator repair', 'sub zero 36 inch refrigerator repair',
     'sub zero side by side repair', 'sub zero french door refrigerator repair', 'sub zero bottom freezer repair',
     'sub zero refrigerator drawers repair', 'sub zero undercounter refrigerator repair',
     'sub zero built in refrigerator service', 'sub zero 650 repair', 'sub zero 690 repair', 'sub zero 736 repair',
     'sub zero bi 36 repair', 'sub zero bi 42 repair', 'sub zero bi 48 repair', 'sub zero it 36 repair',
     'sub zero ic 36 repair', 'sub zero 24 inch drawer repair'],
    ['Sub-Zero 600 & 700 Series Help', 'Sub-Zero PRO 48 Repair Chicago', 'Sub-Zero BI & IT Models Fixed'],
    ['Classic Series Specialists', 'Designer Column Repairs', 'Older 500 Series Still Served',
     'Drawers & Undercounter Units', 'Parts For 20-Year-Old Models', 'Side-By-Side & French Door'],
    ['BI-36, BI-42, BI-48, IT and IC columns, PRO 48: we know the layout of each series and carry its common parts.',
     'Older 500, 600 and 700 series units are worth keeping. We source the right parts and quote before any work.'],
    ['Model number on the inside wall? Read it to the dispatcher and the tech arrives with the likely parts.',
     'Classic, Designer, PRO and undercounter drawers all repaired at your home. 90 days on labor, parts by their maker.'])

grp('Sub-Zero > Brand & Areas', 'sub-zero/', '38.00', 'SubZero', 'Chicago',
    ['sub zero repair', 'sub zero repair near me', 'subzero repair', 'sub-zero repair', 'sub zero appliance repair',
     'sub zero service', 'sub zero technician', 'sub zero technician near me', 'sub zero repair service',
     'sub zero repair company', 'sub zero repairman', 'local sub zero repair', 'sub zero specialist near me',
     'sub zero repair cost', 'sub zero appliance repair near me', 'subzero repair near me', 'sub zero service near me',
     'sub zero repair technician', 'sub zero service call', 'sub zero service technician', 'sub zero service company',
     'sub zero appliance service', 'sub zero specialist', 'subzero service', 'sub zero repair man', 'sub zero fix', 'sub zero help', 'sub zero repair quote', 'sub zero repair estimate',
     'independent sub zero repair', 'sub zero repair illinois', 'sub zero repair suburbs'],
    ['Sub-Zero Repair In Chicago', 'Sub-Zero Technicians Nearby', 'Sub-Zero Service, Chicagoland'],
    ['Fridges, Freezers, Ice & Wine', 'Lincoln Park To Lake Forest', 'Sub-Zero Only, No Factory Ties',
     'Most Repairs Done In One Trip', 'Gold Coast, Oak Park, Hinsdale', 'Panel-Ready Units Stay Put'],
    ['Sub-Zero refrigerators, freezers, ice makers and wine units repaired at your home across Chicagoland.',
     'Independent Sub-Zero specialists. Written price before work, OEM parts, 90 days on labor, phone answered 24/7.'],
    ['From the Gold Coast to Lake Forest and out to Naperville: local techs, stocked vans, same-day slots when open.',
     'Tell us the model and symptom. We quote the diagnostic on the phone and the repair price before we touch it.'],
    area_brand='sub zero', area_tpl=['sub zero repair {a}', '{a} sub zero repair', 'sub zero service {a}'])

# ================================= WOLF =====================================
grp('Wolf > Range Repair', 'wolf/range-repair/', '36.00', 'Wolf', 'Range',
    ['wolf range repair', 'wolf range repair near me', 'wolf range service', 'wolf range technician',
     'wolf range not working', 'wolf range igniter replacement', 'wolf range burner not lighting',
     'wolf range oven not heating', 'wolf range clicking', 'wolf dual fuel range repair', 'wolf gas range repair',
     'wolf range oven door repair', 'wolf range repairman', 'wolf stove repair', 'wolf stove repair near me',
     'wolf range oven not working', 'wolf range temperature wrong', 'wolf range griddle not heating',
     'wolf range convection fan noise', 'wolf range self clean problem',
     'wolf 48 inch range repair', 'wolf 36 inch range repair', 'wolf range repair chicago',
     'wolf stove repair chicago'],
    ['Wolf Range Repair In Chicago', 'Wolf Stove Not Working?', 'Wolf Dual Fuel Range Service'],
    ['Burner Clicks But No Flame?', 'Preheat Never Finishes?', 'Spark Modules & Igniters',
     'Griddle Plate Staying Cold?', 'Convection Fan Rattling?', '30, 36, 48 & 60 Inch Ranges'],
    ['Wolf range clicking, burner not lighting or oven never reaching temp? Igniters, modules and valves on the van.',
     'Dual fuel and all-gas Wolf ranges, 30 to 60 inches. Oven elements, sensors, fans and door hinges replaced in place.'],
    ['A Wolf that heats unevenly or will not hold temperature is usually a sensor or element. Fixed with OEM parts.',
     'Gas smell? Call the gas company first. For everything else on your Wolf range, call us and get a price before work.'])

grp('Wolf > Wall Oven Repair', 'wolf/wall-oven-repair/', '36.00', 'Wolf', 'WallOven',
    ['wolf wall oven repair', 'wolf oven repair', 'wolf oven repair near me', 'wolf oven not heating',
     'wolf oven not working', 'wolf double oven repair', 'wolf oven service', 'wolf oven technician',
     'wolf oven door repair', 'wolf oven temperature problem', 'wolf oven fan not working',
     'wolf oven light not working', 'wolf oven won t turn on', 'wolf oven display not working',
     'wolf m series oven repair', 'wolf e series oven repair', 'wolf l series oven repair',
     'wolf oven convection not working', 'wolf oven door glass replacement', 'wolf oven hinge repair',
     'wolf oven repair chicago', 'wolf wall oven repair chicago'],
    ['Wolf Wall Oven Repair Chicago', 'Wolf Oven Running Cold?', 'Wolf Double Oven Service'],
    ['Blank Display Or Dead Panel?', 'Bake Element & Sensor Swaps', 'M, E And L Series Ovens',
     'Door Will Not Latch Or Seal?', 'Oven Fan Gone Quiet?', 'Error Code On Screen? Read It'],
    ['Single and double ovens, M, E and L series. Door hinges, glass, gaskets and fans replaced with OEM parts.'],
    ['A dark display is not always a dead board. We check power, relays and the panel before quoting anything.',
     'Dinner ovens are a priority. Same-day or next-day slots in most of Chicago and the suburbs when open.'])

grp('Wolf > Rangetop Repair', 'wolf/rangetop-repair/', '34.00', 'Wolf', 'Rangetop',
    ['wolf rangetop repair', 'wolf rangetop not lighting', 'wolf rangetop igniter', 'wolf rangetop service',
     'wolf rangetop burner repair', 'wolf rangetop clicking', 'wolf rangetop repair near me',
     'wolf rangetop technician', 'wolf rangetop griddle repair', 'wolf rangetop not working',
     'wolf 36 rangetop repair', 'wolf 48 rangetop repair', 'wolf rangetop low flame', 'wolf rangetop gas smell',
     'wolf rangetop repair chicago'],
    ['Wolf Rangetop Repair Chicago', 'Wolf Rangetop Will Not Light?', 'Wolf Rangetop Igniter Fixes'],
    ['Constant Clicking? Silenced', 'Weak Or Yellow Flame Tuned', 'Griddle Thermostat Replaced',
     'Sealed Burners Rebuilt', 'Valves & Spark Modules Stocked', '36 & 48 Inch Rangetops'],
    ['Wolf rangetop clicking nonstop, one burner dead or flames low? Igniters, modules and valves on the van.',
     'Griddle and charbroiler modules, sealed burners and knobs serviced in place. Exact price approved before work.'],
    ['Constant sparking usually means moisture or a cracked igniter. Diagnosed fast, fixed with genuine parts.',
     'Independent Wolf repair for rangetops across Chicago and the suburbs. 90 days on labor, phone answered 24/7.'])

grp('Wolf > Cooktop Repair', 'wolf/cooktop-repair/', '34.00', 'Wolf', 'Cooktop',
    ['wolf cooktop repair', 'wolf induction cooktop repair', 'wolf gas cooktop repair', 'wolf cooktop not working',
     'wolf cooktop repair near me', 'wolf cooktop service', 'wolf cooktop technician', 'wolf cooktop igniter',
     'wolf cooktop not lighting', 'wolf induction not heating', 'wolf cooktop glass replacement', 'wolf cooktop burner repair', 'wolf electric cooktop repair',
     'wolf cooktop clicking', 'wolf cooktop repair chicago'],
    ['Wolf Cooktop Repair In Chicago', 'Wolf Induction Not Heating?', 'Wolf Gas Cooktop Service'],
    ['One Induction Zone Out?', 'Cracked Glass Top Replaced', 'Burner Clicks, No Flame?',
     'Error Flashing On Induction?', 'Gas, Electric & Induction', 'Glass Panel Ignoring Taps?'],
    ['Wolf induction zone not heating or gas burner refusing to light? Boards, coils, igniters checked at your home.',
     'Gas, electric and induction Wolf cooktops. Glass tops, touch panels and burner assemblies replaced with OEM parts.'],
    ['Written price before any work, 90 days on labor. Local Wolf technicians from Evanston to Hinsdale.'])

grp('Wolf > Steam Oven Repair', 'wolf/steam-oven-repair/', '34.00', 'Wolf', 'SteamOven',
    ['wolf steam oven repair', 'wolf convection steam oven repair', 'wolf steam oven not working',
     'wolf steam oven no steam', 'wolf steam oven service', 'wolf steam oven repair near me',
     'wolf steam oven descale problem', 'wolf steam oven leaking', 'wolf steam oven door repair',
     'wolf steam oven technician', 'wolf steam oven repair chicago'],
    ['Wolf Steam Oven Repair Chicago', 'Wolf Steam Oven Not Steaming?', 'Wolf Convection Steam Service'],
    ['Water Tank Not Detected?', 'Boiler & Pump Faults Fixed', 'Descale Alert Stuck On?',
     'Door Seal Leaking Steam?', 'Heating Elements Replaced', 'Plumbed & Tank Models'],
    ['Wolf convection steam oven dry, leaking or stuck on a descale warning? Boiler, pump and sensors tested.',
     'Tank and plumbed steam ovens. Door seals, elements, pumps and boards replaced with genuine parts.'],
    ['Steam ovens are specialist work. We quote the exact price at your home and back the labor for 90 days.',
     'Independent repair, not the factory. Same-day or next-day visits available in most of Chicagoland.'])

grp('Wolf > Outdoor Grill Repair', 'wolf/outdoor-grill-repair/', '30.00', 'Wolf', 'Grill',
    ['wolf grill repair', 'wolf outdoor grill repair', 'wolf bbq repair', 'wolf grill not lighting',
     'wolf grill igniter replacement', 'wolf grill burner replacement', 'wolf grill service',
     'wolf grill repair near me', 'wolf built in grill repair', 'wolf grill low flame', 'wolf grill technician',
     'wolf grill rotisserie repair', 'wolf grill repair chicago'],
    ['Wolf Grill Repair In Chicago', 'Wolf Grill Refusing To Light?', 'Wolf Built-In Grill Service'],
    ['Burners Rusted Or Clogged?', 'Igniters & Electrodes Replaced', 'Rotisserie Motor Dead?',
     'Low Flame Or Uneven Heat?', 'Natural Gas & Propane Grills', 'Spring & Fall Tune-Ups'],
    ['Wolf outdoor grill will not light or heats unevenly? Burners, igniters, valves and regulators serviced on site.',
     'Built-in Wolf grills, natural gas and propane. Rotisserie motors, side burners and knobs replaced with OEM parts.'],
    ['Get the grill ready for the season or fixed mid-summer. Exact price before work, 90 days on labor.',
     'Independent Wolf grill repair across Chicago, the North Shore and the western suburbs.'])

grp('Wolf > Brand & Areas', 'wolf/', '32.00', 'Wolf', 'Chicago',
    ['wolf appliance repair', 'wolf appliance repair near me', 'wolf repair', 'wolf repair near me',
     'wolf appliance service', 'wolf appliance technician', 'wolf repair service', 'wolf appliance repairman',
     'wolf oven and range repair', 'wolf kitchen appliance repair', 'wolf repair company', 'wolf service technician',
     'wolf appliance specialist', 'wolf repair cost', 'wolf appliance repair cost', 'wolf technician near me',
     'local wolf appliance repair', 'independent wolf repair', 'wolf appliance repair illinois',
     'wolf appliance repair suburbs', 'wolf appliance fix'],
    ['Wolf Appliance Repair Chicago', 'Wolf Repair Technicians Nearby', 'Wolf Service, All Chicagoland'],
    ['Ranges, Ovens, Tops & Grills', 'Independent Wolf Specialists', 'Evanston To Naperville',
     'Igniters To Control Boards', 'One Visit For Most Repairs', 'Lakeview, Winnetka, Oak Brook'],
    ['Wolf ranges, wall ovens, rangetops, cooktops, steam ovens and grills repaired at your home in Chicagoland.',
     'Independent Wolf specialists. Exact price approved before work, OEM parts, 90 days on labor, phone open 24/7.'],
    ['Local Wolf technicians from the Gold Coast to Lake Forest and Hinsdale. Same-day slots when the schedule allows.',
     'Name the model and the symptom. The diagnostic fee is quoted on the call and credited to the repair.'],
    area_brand='wolf', area_tpl=['wolf appliance repair {a}', 'wolf range repair {a}', 'wolf repair {a}'])

# ================================ VIKING ====================================
grp('Viking > Refrigerator Repair', 'viking/refrigerator-repair/', '36.00', 'Viking', 'Fridge',
    ['viking refrigerator repair', 'viking fridge repair', 'viking refrigerator repair near me',
     'viking refrigerator not cooling', 'viking fridge not cooling', 'viking built in refrigerator repair',
     'viking refrigerator service', 'viking refrigerator technician', 'viking refrigerator not working',
     'viking freezer not freezing', 'viking refrigerator leaking', 'viking refrigerator compressor',
     'viking refrigerator fan noise', 'viking refrigerator door gasket', 'viking fridge warm',
     'viking refrigerator repairman', 'viking 48 refrigerator repair', 'viking 36 refrigerator repair',
     'viking refrigerator repair chicago', 'viking fridge repair chicago'],
    ['Viking Fridge Repair Chicago', 'Viking Refrigerator Not Cold?', 'Viking Built-In Fridge Service'],
    ['Warm Fridge, Working Freezer?', 'Compressor & Fan Diagnosis', 'Leaks & Frost Traced To Source',
     'New Gaskets Fitted On Site', 'Pro & Designer Series Served', '36, 42 & 48 Inch Built-Ins'],
    ['Viking refrigerator warm, noisy or leaking? Fans, boards, sensors and the sealed system tested in order.',
     'Viking Professional and Designer built-ins, 36 to 48 inches. Gaskets, hinges and fans replaced with OEM parts.'],
    ['A Viking fridge losing cold is often one part. We find it, price it in writing and fix it that visit if stocked.',
     'Independent Viking repair across Chicago and the suburbs. 90 days on labor, phone answered around the clock.'])

grp('Viking > Range Repair', 'viking/range-repair/', '36.00', 'Viking', 'Range',
    ['viking range repair', 'viking range repair near me', 'viking stove repair', 'viking range not working',
     'viking range igniter replacement', 'viking range burner not lighting', 'viking oven not heating',
     'viking range oven not working', 'viking range service', 'viking range technician', 'viking gas range repair',
     'viking dual fuel range repair', 'viking range clicking', 'viking range door repair', 'viking range repairman',
     'viking range oven temperature', 'viking range self clean', 'viking 48 range repair', 'viking 36 range repair',
     'viking range repair chicago', 'viking stove repair chicago'],
    ['Viking Range Repair In Chicago', 'Viking Burner Will Not Light?', 'Viking Oven Running Cold?'],
    ['Igniter Glows, No Flame?', 'Oven Slow To Preheat?', 'Spark Modules & Valves Stocked',
     'Sagging Door Fixed In Place', 'Gas Or Dual Fuel, Both Served', 'Convection Fan Grinding?'],
    ['Viking range clicking, burner dead or oven not heating? Igniters, modules, elements and sensors on the van.',
     'Dual fuel and gas Viking ranges, 30 to 60 inches. Door hinges, glass and fans replaced with genuine parts.'],
    ['A Viking oven stuck at a low temp is usually an igniter or sensor. Confirmed first, then priced in writing.',
     'Gas smell? Call the utility first. For everything else on your Viking range, our line is open 24/7.'])

grp('Viking > Cooktop & Rangetop Repair', 'viking/cooktop-repair/', '34.00', 'Viking', 'Cooktop',
    ['viking cooktop repair', 'viking rangetop repair', 'viking cooktop not lighting', 'viking cooktop igniter',
     'viking cooktop repair near me', 'viking gas cooktop repair', 'viking induction cooktop repair',
     'viking cooktop clicking', 'viking cooktop service', 'viking rangetop not working', 'viking cooktop burner repair',
     'viking rangetop igniter', 'viking cooktop technician', 'viking cooktop repair chicago'],
    ['Viking Cooktop Repair Chicago', 'Viking Rangetop Stays Cold?', 'Viking Cooktop Burner Service'],
    ['Clicking That Never Stops?', 'One Burner Out? Rebuilt', 'Induction Zone Failing?',
     'Griddle Plate Not Heating?', 'Burner Valves & Knobs Stocked', 'Gas And Induction Models'],
    ['Viking cooktop or rangetop clicking, dead burner or weak flame? Igniters, modules and valves replaced on site.',
     'Gas and induction Viking cooktops. Griddles, burner caps, knobs and boards serviced with OEM parts.'],
    ['Exact price before any work, 90 days on labor. Independent Viking technicians across Chicagoland.',
     'Most cooktop repairs finish in one visit because the common parts ride along in the van.'])

grp('Viking > Wall Oven Repair', 'viking/wall-oven-repair/', '34.00', 'Viking', 'WallOven',
    ['viking wall oven repair', 'viking oven repair', 'viking oven repair near me', 'viking double oven repair',
     'viking oven not working', 'viking wall oven not heating', 'viking oven service', 'viking oven technician',
     'viking oven door repair', 'viking oven fan not working', 'viking oven won t turn on',
     'viking oven display not working', 'viking oven hinge repair', 'viking oven repair chicago'],
    ['Viking Wall Oven Fix, Chicago', 'Viking Oven Not Turning On?', 'Viking Double Oven Service'],
    ['Dead Display Or Lost Power?', 'Element & Sensor Replacement', 'Door Drops Or Will Not Close?',
     'Convection Fan Replaced', 'Error Codes Decoded On Site', 'Double Ovens Welcome'],
    ['Viking wall oven cold, erratic or dark? Relays, boards, elements and sensors tested at your home first.',
     'Single and double Viking ovens. Hinges, gaskets, glass and fans replaced with genuine parts, price agreed first.'],
    ['Independent Viking oven repair from Lincoln Park to Naperville. Labor backed for 90 days.'])

grp('Viking > Wine Cellar Repair', 'viking/wine-cellar-repair/', '34.00', 'Viking', 'Wine',
    ['viking wine cellar repair', 'viking wine cooler repair', 'viking wine fridge repair',
     'viking wine cooler not cooling', 'viking wine cellar not cooling', 'viking wine refrigerator repair',
     'viking wine cooler service', 'viking wine cooler repair near me', 'viking undercounter wine repair',
     'viking wine cooler not working', 'viking wine cellar repair chicago'],
    ['Viking Wine Cellar Repairs', 'Viking Wine Cooler Not Cold?', 'Viking Wine Fridge Service'],
    ['Temperature Climbing Daily?', 'Cooling Fan & Sensor Swaps', 'Door Seal Letting Heat In?',
     'Undercounter & Tall Cellars', 'Noisy Compressor Checked', 'Zones Reset To Target Temp'],
    ['Viking wine cellar warming or cycling loudly? Each zone measured, fault isolated, price agreed before work.',
     'Undercounter and full-height Viking wine units. Fans, sensors, seals and boards replaced with OEM parts.'],
    ['A warming cellar is a priority call. We take the first open slot so the collection stops drifting.',
     'Independent Viking repair across Chicago and the suburbs. 90 days on labor, phone open day and night.'])

grp('Viking > Ice Maker Repair', 'viking/ice-maker-repair/', '32.00', 'Viking', 'IceMaker',
    ['viking ice maker repair', 'viking ice maker not working', 'viking ice maker not making ice',
     'viking ice machine repair', 'viking undercounter ice maker repair', 'viking ice maker leaking',
     'viking ice maker service', 'viking ice maker repair near me', 'viking refrigerator ice maker not working',
     'viking ice maker frozen', 'viking ice maker repair chicago'],
    ['Viking Ice Maker Fixes', 'Viking Not Making Ice?', 'Viking Ice Machine Service'],
    ['Bin Empty, Light Blinking?', 'Water Valve & Line Checked', 'Undercounter Units Serviced',
     'Leaking Under The Ice Bin?', 'Harvest Cycle Stalled?', 'Clumped Or Cloudy Ice Solved'],
    ['Viking ice maker quiet, slow or leaking? Fill valve, line, mold and controls tested, repaired with OEM parts.',
     'Fridge ice makers and undercounter Viking ice machines. Written price first, 90 days on labor.'],
    ['Water pressure, filter and sensors checked so the fix lasts. Phone answered 24/7 across Chicagoland.',
     'Replacement ice maker assemblies installed when a rebuild is not worth your money. Honest call, every time.'])

grp('Viking > Brand & Areas', 'viking/', '32.00', 'Viking', 'Chicago',
    ['viking appliance repair', 'viking appliance repair near me', 'viking repair', 'viking repair near me',
     'viking appliance service', 'viking appliance technician', 'viking repair service', 'viking appliance repairman',
     'viking kitchen appliance repair', 'viking repair company', 'viking service technician',
     'viking appliance specialist', 'viking repair cost', 'viking appliance repair cost', 'viking technician near me',
     'local viking appliance repair', 'independent viking repair', 'viking appliance repair illinois',
     'viking appliance repair suburbs', 'viking range and refrigerator repair'],
    ['Viking Repair Across Chicago', 'Viking Technicians Near You', 'Viking Service In Chicagoland'],
    ['Ranges, Fridges, Ovens, Wine', 'Independent Viking Specialists', 'North Shore & Western Suburbs',
     'Professional Series Experts', 'Most Jobs Done In One Visit', 'River North To Hinsdale'],
    ['Viking ranges, refrigerators, ovens, cooktops, wine cellars and ice makers repaired at your home.',
     'Independent Viking specialists for Chicago and the suburbs. Price in writing first, OEM parts, 90 days on labor.'],
    ['Local Viking technicians from Lincoln Park to Lake Forest and Naperville. Same-day slots when open.',
     'Model and symptom on the call, diagnostic fee quoted up front and credited when you approve the repair.'],
    area_brand='viking', area_tpl=['viking appliance repair {a}', 'viking range repair {a}', 'viking repair {a}'])

# ================================= MIELE ====================================
grp('Miele > Washer Repair', 'miele/washer-dryer-repair/', '34.00', 'Miele', 'Washer',
    ['miele washer repair', 'miele washing machine repair', 'miele washer repair near me', 'miele washer not draining',
     'miele washer not spinning', 'miele washer leaking', 'miele washer door locked',
     'miele washer not starting', 'miele washer service', 'miele washer technician', 'miele w1 washer repair',
     'miele washing machine not working', 'miele washer repairman', 'miele washer drain pump',
     'miele washer banging', 'miele washer smells', 'miele washing machine service', 'miele washer repair chicago',
     'miele washing machine repair chicago'],
    ['Miele Washer Repair In Chicago', 'Miele Washing Machine Help', 'Miele W1 Washer Not Draining?'],
    ['Door Locked With Clothes In?', 'Drain Pump & Filter Cleared', 'Drum Banging On Spin?',
     'Error Code On The Display?', 'Water Left In The Drum?', 'Inlet Valves & Hoses Checked'],
    ['Miele washer stuck, not draining or flashing a fault? Pump, filter, door lock and board tested at your home.',
     'W1 and older Miele front-loaders. Bearings, pumps, valves and locks replaced with genuine parts, price first.'],
    ['Door locked with a load inside? We release it, find the cause and quote the repair before any work.',
     'Independent Miele repair across Chicago and the suburbs. 90 days on labor, phone answered 24/7.'])

grp('Miele > Dryer Repair', 'miele/washer-dryer-repair/', '34.00', 'Miele', 'Dryer',
    ['miele dryer repair', 'miele dryer not heating', 'miele dryer not drying', 'miele dryer repair near me',
     'miele heat pump dryer repair', 'miele dryer not starting', 'miele dryer service',
     'miele dryer technician', 'miele t1 dryer repair', 'miele dryer takes too long', 'miele dryer drum not turning',
     'miele dryer noise', 'miele dryer condenser problem', 'miele dryer water container full',
     'miele dryer repairman', 'miele dryer repair chicago', 'miele dryer not working'],
    ['Miele Dryer Repair In Chicago', 'Miele Dryer Blowing Cold?', 'Miele Heat Pump Dryer Service'],
    ['Load Still Damp After Hours?', 'Heat Pump & Condenser Faults', 'Drum Stopped Turning?',
     'Belt, Motor & Sensor Swaps', 'Container Full Light Stuck?', 'T1 And Older Miele Dryers'],
    ['Miele dryer running cold or taking three cycles? Heat pump, condenser, sensors and airflow checked on site.',
     'T1 heat pump and vented Miele dryers. Belts, motors, heaters and boards replaced with OEM parts, price first.'],
    ['Long dry times are usually airflow or a sensor. We confirm the cause and quote before touching a part.',
     'Independent Miele technicians from Evanston to Hinsdale. 90 days on labor, same-day slots when open.'])

grp('Miele > Oven & Steam Oven Repair', 'miele/oven-repair/', '34.00', 'Miele', 'Oven',
    ['miele oven repair', 'miele oven repair near me', 'miele oven not heating', 'miele oven not working',
     'miele steam oven repair', 'miele combi steam oven repair', 'miele oven service',
     'miele oven technician', 'miele oven door repair', 'miele wall oven repair', 'miele speed oven repair',
     'miele oven display not working', 'miele steam oven no steam', 'miele oven fan not working',
     'miele oven repairman', 'miele oven repair chicago'],
    ['Miele Oven Repair In Chicago', 'Miele Steam Oven Not Working?', 'Miele Wall Oven Service'],
    ['Oven Cold Or Cutting Out?', 'Combi Steam Boiler Faults', 'Shattered Door Glass Swapped',
     'Fault Code On The Panel?', 'Speed Ovens Serviced Too', 'Elements & Sensors Stocked'],
    ['Miele oven cold, stopping mid-bake or showing a fault? Boards, elements, sensors and door locks tested.',
     'Wall ovens, combi steam ovens and speed ovens. Boilers, pumps, hinges and fans replaced with genuine parts.'],
    ['Exact price before work, 90 days on labor. Independent Miele specialists for Chicago and the suburbs.',
     'A fault code tells us where to start, not what to charge. The quote comes after we confirm the part.'])

grp('Miele > Refrigerator Repair', 'miele/refrigerator-repair/', '34.00', 'Miele', 'Fridge',
    ['miele refrigerator repair', 'miele fridge repair', 'miele refrigerator not cooling', 'miele fridge not cooling',
     'miele refrigerator repair near me', 'miele built in refrigerator repair', 'miele mastercool repair',
     'miele refrigerator service', 'miele refrigerator technician', 'miele freezer not freezing',
     'miele refrigerator leaking', 'miele refrigerator ice maker not working',
     'miele fridge warm', 'miele refrigerator repair chicago'],
    ['Miele Fridge Repair In Chicago', 'Miele Fridge Not Cooling?', 'Miele MasterCool Service'],
    ['Warm Fridge Or Soft Freezer?', 'Fans, Boards & Sensors Tested', 'Water Pooling Inside?',
     'Integrated & Column Models', 'Ice Maker Stopped? Fixed', 'Simple Fixes Before Big Ones'],
    ['Miele fridge warming, leaking or beeping? Fans, sensors, boards and the sealed system tested in order.',
     'MasterCool columns and integrated Miele refrigerators. Gaskets, fans and ice makers replaced with OEM parts.'],
    ['Independent Miele repair across Chicagoland. Written price before work, 90 days on our labor.',
     'Panel-ready units stay in the cabinet. Most repairs happen in place without pulling the refrigerator.'])

grp('Miele > Wine Cooler Repair', 'miele/wine-cooler-repair/', '32.00', 'Miele', 'Wine',
    ['miele wine cooler repair', 'miele wine fridge repair', 'miele wine cooler not cooling',
     'miele wine refrigerator repair', 'miele wine storage repair', 'miele wine cooler service',
     'miele wine cooler repair near me', 'miele wine unit not working', 'miele wine cooler repair chicago'],
    ['Miele Wine Cooler Repairs', 'Miele Wine Fridge Not Cold?', 'Miele Wine Storage Service'],
    ['Zones Warming Up?', 'Humidity Control Failing?', 'Compressor & Fan Checked',
     'Door Seal Or Hinge Worn?', 'Integrated Or Freestanding', 'Set Points Restored'],
    ['Miele wine cooler warming or cycling loudly? Zones measured, fault isolated, exact price before any work.',
     'Built-in and freestanding Miele wine units. Fans, sensors, seals and boards replaced with genuine parts.'],
    ['Wine units are priority calls: first open slot so the bottles stop drifting. Phone answered 24/7.',
     'Independent Miele repair, Chicago and the suburbs. 90 days on labor, parts covered by their maker.'])

grp('Miele > Brand & Areas', 'miele/', '30.00', 'Miele', 'Chicago',
    ['miele appliance repair', 'miele appliance repair near me', 'miele repair', 'miele repair near me',
     'miele appliance service', 'miele appliance technician', 'miele repair service', 'miele appliance repairman',
     'miele repair company', 'miele service technician', 'miele appliance specialist', 'miele repair cost',
     'miele technician near me', 'local miele appliance repair', 'independent miele repair',
     'miele appliance repair illinois', 'miele appliance repair suburbs', 'miele laundry repair',
     'miele kitchen appliance repair'],
    ['Miele Appliance Repair Chicago', 'Miele Technicians Near You', 'Miele Service In Chicagoland'],
    ['Laundry, Ovens & Fridges', 'Independent Miele Specialists', 'Lakeview To Lake Forest',
     'Pumps To Control Boards', 'Most Repairs In A Single Trip', 'Oak Park, Hinsdale, Naperville'],
    ['Miele washers, dryers, ovens, steam ovens, refrigerators and wine units repaired at your home in Chicagoland.',
     'Independent Miele specialists. Written price before work, genuine parts, 90 days on labor, phone open 24/7.'],
    ['Local Miele technicians across Chicago, the North Shore and the western suburbs. Same-day slots when open.',
     'Tell us the model and the fault code. Diagnostic fee quoted on the call and credited to the repair.'],
    area_brand='miele', area_tpl=['miele appliance repair {a}', 'miele washer repair {a}', 'miele repair {a}'])

# =============================== THERMADOR ==================================
grp('Thermador > Refrigerator Repair', 'thermador/refrigerator-repair/', '36.00', 'Thermador', 'Fridge',
    ['thermador refrigerator repair', 'thermador fridge repair', 'thermador refrigerator not cooling',
     'thermador fridge not cooling', 'thermador refrigerator repair near me', 'thermador built in refrigerator repair',
     'thermador freedom refrigerator repair', 'thermador column refrigerator repair', 'thermador refrigerator service',
     'thermador refrigerator technician', 'thermador freezer not freezing', 'thermador refrigerator leaking',
     'thermador refrigerator ice maker not working', 'thermador fridge warm',
     'thermador refrigerator repair chicago', 'thermador fridge repair chicago'],
    ['Thermador Fridge Fix, Chicago', 'Thermador Refrigerator Warm?', 'Thermador Freedom Column Help'],
    ['Column Losing Cold Overnight?', 'Fans, Boards & Sensors Tested', 'Water Inside Or Underneath?',
     'Freedom Columns Our Specialty', 'Ice Maker Quit? Repaired', 'Cheap Causes Ruled Out First'],
    ['Thermador refrigerator warming, leaking or beeping? Fans, sensors, boards and sealed system tested in order.',
     'Freedom columns and Thermador built-ins. Gaskets, fans, boards and ice makers replaced with OEM parts.'],
    ['Independent Thermador repair across Chicagoland. Exact price before work, 90 days on our labor.',
     'Panel-ready columns stay put. Most repairs happen in the cabinet without pulling the unit.'])

grp('Thermador > Range Repair', 'thermador/range-repair/', '36.00', 'Thermador', 'Range',
    ['thermador range repair', 'thermador range repair near me', 'thermador stove repair', 'thermador range not working',
     'thermador range igniter', 'thermador burner not lighting', 'thermador range service',
     'thermador range technician', 'thermador pro range repair', 'thermador dual fuel range repair',
     'thermador gas range repair', 'thermador range clicking', 'thermador range door repair', 'thermador range repairman',
     'thermador range oven not working', 'thermador 48 range repair', 'thermador 36 range repair',
     'thermador range repair chicago', 'thermador stove repair chicago'],
    ['Thermador Range Repair Chicago', 'Thermador Burner Stays Out?', 'Thermador Pro Range Service'],
    ['Endless Sparking From Burner?', 'Oven Lagging Behind The Dial?', 'Igniters, Modules & Valves',
     'Griddle Or Grill Module Dead?', 'Every Pro Series Range Served', 'Oven Door Rebuilt On Site'],
    ['Thermador range clicking, Star burner dead or oven slow? Igniters, modules, elements and sensors on the van.',
     'Pro Grand and Pro Harmony ranges, 30 to 60 inches. Hinges, glass and fans replaced with genuine parts.'],
    ['Exact price agreed before work, 90 days on labor. Independent Thermador technicians across Chicago.',
     'Gas smell? Call the utility first. For anything else on your Thermador range, our line answers 24/7.'])

grp('Thermador > Cooktop Repair', 'thermador/cooktop-repair/', '34.00', 'Thermador', 'Cooktop',
    ['thermador cooktop repair', 'thermador induction cooktop repair', 'thermador gas cooktop repair',
     'thermador cooktop not working', 'thermador cooktop repair near me', 'thermador cooktop igniter',
     'thermador cooktop clicking', 'thermador rangetop repair', 'thermador induction not heating',
     'thermador freedom induction repair', 'thermador cooktop service', 'thermador cooktop glass replacement',
     'thermador cooktop technician', 'thermador cooktop repair chicago'],
    ['Thermador Cooktop Fix Chicago', 'Thermador Induction Cold?', 'Thermador Gas Cooktop Service'],
    ['Freedom Induction Acting Up?', 'Star Burners Rebuilt', 'Cracked Glass Replaced',
     'Clicking Igniters Silenced', 'Rangetops & Cooktops Alike', 'Controls Frozen Mid-Cook?'],
    ['Thermador induction zone out or gas burner clicking? Boards, coils, igniters and valves tested at your home.',
     'Freedom induction, gas cooktops and rangetops. Glass, panels and burner assemblies replaced with OEM parts.'],
    ['Independent Thermador repair, Chicago and the suburbs. Written price before work, 90 days on labor.',
     'Most cooktop faults are one part. We confirm it, quote it and usually fix it the same visit.'])

grp('Thermador > Wall Oven Repair', 'thermador/wall-oven-repair/', '34.00', 'Thermador', 'WallOven',
    ['thermador wall oven repair', 'thermador oven repair', 'thermador oven repair near me', 'thermador oven not heating',
     'thermador oven not working', 'thermador double oven repair', 'thermador oven service', 'thermador oven technician',
     'thermador oven door repair', 'thermador steam oven repair', 'thermador oven fan noise',
     'thermador oven display not working', 'thermador masterpiece oven repair', 'thermador oven won t turn on',
     'thermador oven repair chicago'],
    ['Thermador Oven Repair Chicago', 'Thermador Oven Running Cold?', 'Thermador Double Oven Service'],
    ['Display Dark Or Frozen?', 'Elements & Sensors Replaced', 'Steam Oven Boiler Faults',
     'Door Will Not Latch?', 'Masterpiece Series Experts', 'Error Codes Read On Site'],
    ['Thermador wall oven cold, erratic or showing a code? Boards, relays, elements and sensors tested first.',
     'Single, double and steam Thermador ovens. Hinges, gaskets, glass and fans replaced with genuine parts.'],
    ['Exact price before any work, 90 days on labor. Independent Thermador techs from Evanston to Naperville.',
     'Dinner ovens get priority. Same-day or next-day slots in most of Chicago and the suburbs when open.'])

grp('Thermador > Wine Column Repair', 'thermador/wine-column-repair/', '32.00', 'Thermador', 'Wine',
    ['thermador wine column repair', 'thermador wine cooler repair', 'thermador wine fridge repair',
     'thermador wine cooler not cooling', 'thermador wine refrigerator repair', 'thermador wine column not cooling',
     'thermador wine cooler service', 'thermador wine cooler repair near me', 'thermador wine preservation repair',
     'thermador wine column repair chicago'],
    ['Thermador Wine Column Fixes', 'Thermador Wine Unit Not Cold?', 'Thermador Wine Fridge Service'],
    ['Column Zones Drifting Up?', 'Fans, Sensors & Boards Tested', 'Door Seal Or Hinge Worn?',
     'Thermador Freedom Columns', 'Noisy Compressor Checked', 'Set Points Restored & Logged'],
    ['Thermador wine column warming or cycling loudly? Zones measured, fault isolated, exact price before work.',
     'Freedom wine columns and undercounter Thermador units. Fans, sensors, seals and boards replaced with OEM parts.'],
    ['Wine columns are priority calls: first open slot so the collection stops drifting. Phone open 24/7.',
     'Independent Thermador repair across Chicagoland. 90 days on labor, parts covered by their maker.'])

grp('Thermador > Brand & Areas', 'thermador/', '30.00', 'Thermador', 'Chicago',
    ['thermador appliance repair', 'thermador appliance repair near me', 'thermador repair', 'thermador repair near me',
     'thermador appliance service', 'thermador appliance technician', 'thermador repair service',
     'thermador appliance repairman', 'thermador repair company', 'thermador service technician',
     'thermador appliance specialist', 'thermador repair cost', 'thermador technician near me',
     'local thermador appliance repair', 'independent thermador repair', 'thermador appliance repair illinois',
     'thermador appliance repair suburbs', 'thermador kitchen appliance repair'],
    ['Thermador Repair In Chicago', 'Thermador Technicians Nearby', 'Thermador Service, Chicagoland'],
    ['Ranges, Columns, Ovens, Wine', 'No Factory Ties, Just Repairs', 'Gold Coast To Naperville',
     'Star Burners & Freedom Columns', 'Most Repairs In One Visit', 'Wilmette, Oak Brook, Glencoe'],
    ['Thermador ranges, refrigerator columns, cooktops, wall ovens and wine columns repaired at your home.',
     'Independent Thermador specialists for Chicago and the suburbs. Price in writing first, OEM parts, 90 days on labor.'],
    ['Local Thermador technicians from River North to Lake Forest and Hinsdale. Same-day slots when open.',
     'Model and symptom on the call, diagnostic fee quoted up front and credited when you approve the repair.'],
    area_brand='thermador', area_tpl=['thermador appliance repair {a}', 'thermador range repair {a}', 'thermador repair {a}'])

# ============================ LUXURY / GENERIC ==============================
grp('Luxury & Built-In > All Brands', '', '26.00', 'Luxury', 'Repair',
    ['luxury appliance repair', 'high end appliance repair', 'high end appliance repair near me',
     'luxury appliance repair near me', 'built in refrigerator repair', 'built in appliance repair',
     'premium appliance repair', 'luxury kitchen appliance repair', 'high end refrigerator repair',
     'built in refrigerator repair near me', 'high end appliance repair service', 'luxury appliance repair service',
     'high end appliance technician', 'luxury appliance technician', 'designer appliance repair',
     'professional appliance repair chicago', 'built in fridge repair', 'panel ready refrigerator repair',
     'integrated refrigerator repair', 'column refrigerator repair', 'luxury refrigerator repair',
     'high end range repair', 'high end oven repair', 'luxury range repair', 'pro range repair',
     'professional range repair near me', 'high end wine cooler repair', 'luxury appliance service',
     'high end appliance repair illinois', 'luxury appliance repair suburbs', 'luxury appliance repair north shore'],
    ['Chicago Luxury Appliance Pros', 'High-End Appliance Technicians', 'Built-In Fridge Repair Chicago'],
    ['Sub-Zero To Thermador Covered', 'Columns & Panel-Ready Units', 'Pro Ranges & Wall Ovens',
     'Five Premium Brands Only', 'Trained On Built-In Kitchens', 'Gold Coast To Naperville'],
    ['Sub-Zero, Wolf, Viking, Miele and Thermador repaired at your home across Chicago and the suburbs.',
     'Built-in refrigerators, pro ranges, wall ovens, cooktops and wine units. Exact price before work, OEM parts.'],
    ['Independent luxury appliance specialists. 90 days on labor, phone answered 24/7, same-day slots when open.',
     'Five brands, one phone line. Techs dispatched locally from Evanston to Hinsdale, stocked for common faults.'],
    area_brand='luxury', area_tpl=['luxury appliance repair {a}', 'high end appliance repair {a}'])

import descs
DESC_A, DESC_B = descs.DESC_A, descs.DESC_B
for _g in G:
    _g['dA'], _g['dB'] = descs.D[_g['name']]
assert set(descs.D) == {_g['name'] for _g in G}, set(descs.D) ^ {_g['name'] for _g in G}

# ----------------------------------------------------------------------------
# Campaign-level assets
# ----------------------------------------------------------------------------
SITELINKS = [
    ('Sub-Zero Fridge Service', BASE + 'sub-zero/refrigerator-repair/', 'Warm box, frost or water pooling.', 'Both cooling sides checked.'),
    ('Wolf Range & Oven Help', BASE + 'wolf/range-repair/', 'Burners, igniters, oven heat.', 'Dual fuel and all-gas models.'),
    ('Viking Repairs', BASE + 'viking/', 'Fridges, ranges, ovens, wine.', 'Professional and Designer series.'),
    ('Miele Washer & Dryer', BASE + 'miele/washer-dryer-repair/', 'Not draining, not drying, locked.', 'W1 washers and T1 dryers.'),
    ('Thermador Service', BASE + 'thermador/', 'Columns, Star burners, ovens.', 'Freedom and Masterpiece lines.'),
    ('Ice Maker Repairs', BASE + 'sub-zero/ice-maker-repair/', 'No ice, slow ice, hollow cubes.', 'Built-in and undercounter.'),
    ('Wine Fridge Service', BASE + 'sub-zero/wine-storage-repair/', 'Zones warming? Priority slot.', 'Columns and undercounter.'),
    ('What A Repair Costs', ROOT + 'pricing/', 'Diagnostic fee quoted on the call.', 'Credited when you approve.'),
    ('Labor Warranty Details', ROOT + 'warranty/', '90 days on labor, in plain words.', 'Parts by their supplier.'),
    ('Request A Technician', ROOT + 'contact/', 'Call any hour or send the form.', 'Dispatcher calls you back.'),
]
CALLOUTS = [
    'Upfront Written Quotes', '90 Days On Labor', 'Calls Taken Day & Night', 'OEM Replacement Parts',
    'Fee Credited To Repair', 'Locally Dispatched Techs', 'Columns & Built-Ins', 'Sub-Zero To Thermador',
    'Not A Factory Network', 'Book Online Or By Phone',
]

# ----------------------------------------------------------------------------
# Negatives: union of the old Chicago negatives + additions
# ----------------------------------------------------------------------------
EXTRA_NEG = [
    ('reviews', 'Campaign Negative Broad'), ('review', 'Campaign Negative Broad'),
    ('floor model', 'Campaign Negative Broad'), ('scratch and dent', 'Campaign Negative Broad'),
    ('liquidation', 'Campaign Negative Broad'), ('overstock', 'Campaign Negative Broad'),
    ('open box', 'Campaign Negative Broad'), ('refurb', 'Campaign Negative Broad'),
    ('angi', 'Campaign Negative Broad'), ('angies list', 'Campaign Negative Broad'),
    ('thumbtack', 'Campaign Negative Broad'), ('homeadvisor', 'Campaign Negative Broad'),
    ('nextdoor', 'Campaign Negative Broad'), ('sears', 'Campaign Negative Broad'),
    ('mr appliance', 'Campaign Negative Broad'), ('abt appliance', 'Campaign Negative Broad'),
    ('geek squad', 'Campaign Negative Broad'), ('asurion', 'Campaign Negative Broad'),
    ('trash compactor', 'Campaign Negative Broad'), ('compactor', 'Campaign Negative Broad'),
    ('warming drawer', 'Campaign Negative Broad'), ('wolf gourmet', 'Campaign Negative Broad'),
    ('miele vacuum', 'Campaign Negative Broad'), ('miele dishwasher', 'Campaign Negative Broad'),
    ('thermador dishwasher', 'Campaign Negative Broad'), ('viking dishwasher', 'Campaign Negative Broad'),
    ('cove dishwasher', 'Campaign Negative Broad'), ('wolf oven price', 'Campaign Negative Phrase'),
    ('viking range price', 'Campaign Negative Phrase'), ('thermador range price', 'Campaign Negative Phrase'),
    ('sub zero refrigerator price', 'Campaign Negative Phrase'), ('miele washer price', 'Campaign Negative Phrase'),
    ('how much does', 'Campaign Negative Phrase'), ('worth it', 'Campaign Negative Phrase'),
    ('vs sub zero', 'Campaign Negative Phrase'), ('tol appliances', 'Campaign Negative Phrase'),
    ('sterling home group', 'Campaign Negative Phrase'),
]

# ============================================================================
# Validation helpers
# ============================================================================
def L(s): return len(s)

old_h = set(l.strip().lower() for l in open('old_headlines.txt', encoding='utf-8') if l.strip())
old_d = set(l.strip().lower() for l in open('old_descriptions.txt', encoding='utf-8') if l.strip())
problems = []
near = []

def check_head(h):
    if L(h) > 30: problems.append(('H>30', h, L(h)))
    if '!' in h: problems.append(('H has !', h, 0))
    if h.lower() in old_h: problems.append(('H dup old', h, 0))
    for o in old_h:
        if difflib.SequenceMatcher(None, h.lower(), o).ratio() >= 0.82:
            near.append(('H', h, o))

def check_desc(d):
    if L(d) > 90: problems.append(('D>90', d, L(d)))
    if d.count('!') > 1: problems.append(('D !!', d, 0))
    if d.lower() in old_d: problems.append(('D dup old', d, 0))
    for o in old_d:
        if difflib.SequenceMatcher(None, d.lower(), o).ratio() >= 0.80:
            near.append(('D', d, o))

# ============================================================================
# Build main CSV
# ============================================================================
HEADER = next(csv.reader(open('main.csv', encoding='utf-8-sig')))
def row(**kw):
    r = {h: '' for h in HEADER}
    for k, v in kw.items():
        assert k in r, k
        r[k] = v
    return r

rows = []
rows.append(row(**{
    'Campaign': CAMPAIGN, 'Campaign Type': 'Search', 'Networks': 'Google search', 'Budget': BUDGET,
    'Budget type': 'Daily', 'EU political ads': "Doesn't have EU political ads", 'Languages': 'All',
    'Bid Strategy Type': 'Manual CPC', 'Bid Strategy Name': '', 'Target CPA': '', 'Ad Schedule': '[]',
    'Ad rotation': 'Optimize for clicks', 'Targeting method': 'Location of presence',
    'Exclusion method': 'Location of presence', 'Broad match keywords': 'Off', 'AI Max': 'Disabled',
    'Text customization': 'Disabled', 'Final URL expansion': 'Disabled',
    'Standard conversion goals': 'Account-level', 'Customer acquisition': 'Bid equally',
    'Pay for conversions': 'Disabled', 'Content exclusions': '[]', 'Final URL suffix': SUFFIX,
    'Custom parameters': '{_city}=chicago;{_src}=tlchi', 'Campaign Status': 'Paused',
}))

kw_total = 0
USED_KW = set()
ad_total = 0
all_heads = collections.Counter(); all_descs = collections.Counter()

for g in G:
    name = g['name']
    slug = re.sub(r'[^a-z0-9]+', '', name.lower())
    rows.append(row(**{'Campaign': CAMPAIGN, 'Ad Group': name, 'Max CPC': g['cpc'], 'Ad Group Type': 'Standard',
                       'Custom parameters': '{_grp}=' + slug, 'Campaign Status': 'Paused', 'Ad Group Status': 'Enabled'}))
    # keywords
    seen = set()
    for k in g['kws']:
        k = k.strip().lower()
        if k in seen or k in USED_KW: continue
        seen.add(k); USED_KW.add(k)
        for mt in ('Exact', 'Phrase'):
            rows.append(row(**{'Campaign': CAMPAIGN, 'Ad Group': name, 'Keyword': k, 'Criterion Type': mt,
                               'Campaign Status': 'Paused', 'Ad Group Status': 'Enabled', 'Status': 'Enabled'}))
            kw_total += 1
    if g['area_tpl']:
        for a in AREAS:
            for t in g['area_tpl']:
                k = t.format(a=a)
                if k in seen or k in USED_KW: continue
                seen.add(k); USED_KW.add(k)
                rows.append(row(**{'Campaign': CAMPAIGN, 'Ad Group': name, 'Keyword': k, 'Criterion Type': 'Exact',
                                   'Campaign Status': 'Paused', 'Ad Group Status': 'Enabled', 'Status': 'Enabled'}))
                kw_total += 1
    # ads
    assert len(g['pos1']) == 3 and len(g['spec']) == 6, name
    for variant in ('A', 'B'):
        trust = TRUST_A if variant == 'A' else TRUST_B
        local = LOCAL_A if variant == 'A' else LOCAL_B
        gdesc = DESC_A if variant == 'A' else DESC_B
        sdesc = g['dA'] if variant == 'A' else g['dB']
        # B swaps the order of pos1 so the two ads lead differently
        p1 = g['pos1'] if variant == 'A' else [g['pos1'][1], g['pos1'][0], g['pos1'][2]]
        heads = p1 + g['spec'] + trust + local[:2]
        heads = heads[:15]
        assert len(heads) == 15, (name, len(heads))
        assert len(set(heads)) == 15, (name, heads)
        descs = [sdesc[0], gdesc[0], sdesc[1], gdesc[1]]
        assert len(set(descs)) == 4
        for h in heads: check_head(h); all_heads[h] += 1
        for d in descs: check_desc(d); all_descs[d] += 1
        r = {'Campaign': CAMPAIGN, 'Ad Group': name, 'Final URL': g['url'], 'Ad type': 'Responsive search ad',
             'Path 1': g['p1'], 'Path 2': g['p2'], 'Campaign Status': 'Paused', 'Ad Group Status': 'Enabled',
             'Status': 'Enabled'}
        for i, h in enumerate(heads, 1):
            r[f'Headline {i}'] = h
            if i <= 2: r[f'Headline {i} position'] = '1'
        for i, d in enumerate(descs, 1):
            r[f'Description {i}'] = d
            if i == 1: r[f'Description {i} position'] = '1'
        if L(g['p1']) > 15 or L(g['p2']) > 15: problems.append(('path>15', name, 0))
        rows.append(row(**r))
        ad_total += 1

for text, url, d1, d2 in SITELINKS:
    if L(text) > 25: problems.append(('SL>25', text, L(text)))
    if L(d1) > 35 or L(d2) > 35: problems.append(('SLd>35', d1 + ' | ' + d2, 0))
    rows.append(row(**{'Campaign': CAMPAIGN, 'Final URL': url, 'Link Text': text,
                       'Description Line 1': d1, 'Description Line 2': d2, 'Campaign Status': 'Paused'}))
for c in CALLOUTS:
    if L(c) > 25: problems.append(('CO>25', c, L(c)))
    rows.append(row(**{'Campaign': CAMPAIGN, 'Callout text': c, 'Campaign Status': 'Paused'}))
rows.append(row(**{'Campaign': CAMPAIGN, 'Phone number': PHONE, 'Country': 'US', 'Campaign Status': 'Paused'}))

def write(path, header, rows_):
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows_:
            w.writerow([r.get(h, '') if isinstance(r, dict) else r for h in header] if isinstance(r, dict) else r)

write(f'{OUT}/TL_CHI_01_MAIN_campaign_adgroups_keywords_ads_assets.csv', HEADER, rows)

# ============================================================================
# Locations (unique from the old Chicago campaigns)
# ============================================================================
loc_rows = []
seen = set()
for r in csv.DictReader(open('loc.csv', encoding='utf-8-sig')):
    if not r['Campaign'].startswith('TOL-CHICAGO'): continue
    if r['Location ID'] in seen: continue
    seen.add(r['Location ID'])
    loc_rows.append([CAMPAIGN, r['Location'], r['Location ID'], 'Enabled'])
write(f'{OUT}/TL_CHI_02_LOCATIONS.csv', ['Campaign', 'Location', 'Location ID', 'Status'], loc_rows)

# ============================================================================
# Negatives
# ============================================================================
neg_rows = []
seen = set()
for r in csv.DictReader(open('neg.csv', encoding='utf-8-sig')):
    if not r['Campaign'].startswith('TOL-CHICAGO'): continue
    if r['Keyword'].lower() in ('sub zero','sub-zero','subzero','wolf','viking','miele','thermador'): continue
    key = (r['Keyword'].lower(), r['Criterion Type'])
    if key in seen: continue
    seen.add(key)
    neg_rows.append([CAMPAIGN, r['Keyword'], r['Criterion Type'], 'Enabled'])
for k, t in EXTRA_NEG:
    if (k, t) in seen: continue
    seen.add((k, t))
    neg_rows.append([CAMPAIGN, k, t, 'Enabled'])
# sanity: no negative may block one of our own keywords
own = [r['Keyword'] for r in rows if r['Keyword']]
neg_words = [(n[1].lower(), n[2]) for n in neg_rows]
conflicts = []
for k in set(own):
    toks = set(k.split())
    for nk, nt in neg_words:
        if nt.endswith('Broad') and set(nk.split()) <= toks: conflicts.append((k, nk))
        if nt.endswith('Phrase') and (' ' + nk + ' ') in (' ' + k + ' '): conflicts.append((k, nk))
write(f'{OUT}/TL_CHI_03_NEGATIVES.csv', ['Campaign', 'Keyword', 'Criterion Type', 'Status'], neg_rows)

# ============================================================================
# Report
# ============================================================================
print('ad groups:', len(G), '| keywords:', kw_total, '| ads:', ad_total, '| rows main:', len(rows))
print('locations:', len(loc_rows), '| negatives:', len(neg_rows))
print('unique headlines:', len(all_heads), '| unique descriptions:', len(all_descs))
print('\nPROBLEMS:', len(problems))
for p in problems: print('  ', p)
print('\nNEAR-DUPLICATES vs old (>=0.8):', len(near))
for n in near: print('  ', n)
print('\nNEGATIVE CONFLICTS:', len(conflicts))
for c in sorted(set(conflicts))[:60]: print('  ', c)
