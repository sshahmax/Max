# -*- coding: utf-8 -*-
# Descriptions (<= 90 chars). Key = ad group name -> (dA[2], dB[2])
DESC_A = [
    'Local techs from Evanston to Naperville. Exact price agreed before any work begins.',
    'Diagnostic fee quoted when you book, credited to the repair. 90 days on labor.',
]
DESC_B = [
    'Independent repair company, not a factory network. Genuine parts, 90 days on labor.',
    'Phone answered day and night. Same or next-day openings across most of Chicagoland.',
]

D = {
'Sub-Zero > Fridge Repair': (
    ['Sub-Zero running warm, sweating or humming? Both cooling circuits tested one by one.',
     'Gaskets, hinges, fans and boards replaced in your kitchen. Sealed system confirmed first.'],
    ['Service light on, temps swinging, door drifting open: we find the real cause, then quote.',
     'Columns, built-ins and drawers. Common Sub-Zero parts stocked, so most jobs take one trip.']),
'Sub-Zero > Not Cooling': (
    ['Fridge warm while the freezer holds? That points to one circuit. We test it and show you.',
     'Dirty condenser, iced coil, dead fan or bad board: checked in order, fixed with OEM parts.'],
    ['Stopped cooling after an outage or storm? Often a quick fix. We tell you before you pay.',
     'Warm box, long run times, frost in odd places: diagnosed at home, priced before work.']),
'Sub-Zero > Freezer Repair': (
    ['Soft ice cream, frost sheets or an alarm that keeps chiming? Defrost system checked first.',
     'Drawers, columns and bottom freezers. Heaters, thermostats, fans and seals replaced.'],
    ['A freezer losing cold overnight usually has one bad part. Found, quoted, fixed that visit.',
     'Frost is a symptom, not the problem. We trace it to the seal, heater or sensor and fix it.']),
'Sub-Zero > Ice Maker Repair': (
    ['No ice, slow ice or cloudy cubes? Fill valve, inlet line, mold heater and controls tested.',
     'Built-in ice makers and UC-15 undercounter units. New assembly if rebuild is not worth it.'],
    ['Ice maker frozen solid or leaking under the bin? Genuine parts, price approved first.',
     'Water pressure, filter, ejector arm and sensor checked so the fix holds. 90 days on labor.']),
'Sub-Zero > Wine Storage Repair': (
    ['Wine column drifting warm or cycling loudly? Each zone measured, fault isolated, quoted.',
     'Undercounter wine fridges and tall columns. Fans, sensors, boards and seals replaced.'],
    ['Your bottles belong at a steady 55. We restore both zones and show you the reading.',
     'Wine storage gets the first open slot so the collection stops warming. Call any hour.']),
'Sub-Zero > Leaks & Frost': (
    ['Water on the floor or under the drawers? Usually a blocked or frozen drain. Cleared fast.',
     'Condensation, frost patches and drips start at seals, heaters or drains. We fix the cause.'],
    ['Catch a leak early and the floor survives. Drain tools, heaters and gaskets on the van.',
     'A Sub-Zero should never sweat or drip. Bad part found, quoted in writing, then repaired.']),
'Sub-Zero > Compressor & Sealed System': (
    ['Compressor hot, clicking or silent? We prove it is the compressor before quoting the job.',
     'Leak found, system evacuated, part replaced, recharged, verified. Price agreed first.'],
    ['A sealed-system job is a big decision. Exact figure and a straight repair-or-replace call.',
     'Dual-compressor built-ins: one side can fail alone. We fix only that side, nothing more.']),
'Sub-Zero > Installation & Replacement': (
    ['New Sub-Zero or replacing a tired one? Removal, set, leveling, panels and water line done.',
     'Columns and classic built-ins fitted flush, doors aligned, cooling verified before we go.'],
    ['Cutout, power and water checked before install day, so the unit goes in once, and right.',
     'Flat install price agreed up front. Old unit removed, new one tested and running.']),
'Sub-Zero > Series & Models': (
    ['BI-36, BI-42, BI-48, IT and IC columns, PRO 48: we know each series and its common parts.',
     'Older 500, 600 and 700 series units are worth keeping. Right parts sourced, quoted first.'],
    ['Model number on the inside wall? Read it to the dispatcher. The tech brings likely parts.',
     'Classic, Designer, PRO and undercounter drawers repaired at home. 90 days on labor.']),
'Sub-Zero > Brand & Areas': (
    ['Sub-Zero fridges, freezers, ice makers and wine units repaired at home across Chicagoland.',
     'Independent Sub-Zero specialists. Written price first, OEM parts, 90 days on labor.'],
    ['Gold Coast to Lake Forest and out to Naperville: local techs, stocked vans, fast slots.',
     'Tell us the model and symptom. Diagnostic quoted on the phone, repair price before work.']),

'Wolf > Range Repair': (
    ['Wolf range clicking, burner dead or oven never reaching temp? Igniters and valves stocked.',
     'Dual fuel and all-gas Wolf ranges, 30 to 60 inches. Elements, sensors, fans and hinges.'],
    ['Heats unevenly or will not hold temperature? Usually a sensor or element. OEM parts.',
     'Gas smell? Call the gas company first. For everything else on your Wolf range, call us.']),
'Wolf > Wall Oven Repair': (
    ['Wolf wall oven cold, slow or showing an error? Boards, elements and sensors tested.',
     'Single and double ovens, M, E and L series. Hinges, glass, gaskets and fans replaced.'],
    ['A dark display is not always a dead board. Power, relays and panel checked before a quote.',
     'Dinner ovens are a priority. Same or next-day slots in most of Chicago and the suburbs.']),
'Wolf > Rangetop Repair': (
    ['Wolf rangetop clicking nonstop, one burner dead or flames low? Igniters, valves stocked.',
     'Griddle and charbroiler modules, sealed burners and knobs serviced in place. Price first.'],
    ['Constant sparking usually means moisture or a cracked igniter. Diagnosed and fixed fast.',
     'Independent Wolf rangetop repair across Chicago and the suburbs. 90 days on labor.']),
'Wolf > Cooktop Repair': (
    ['Wolf induction zone cold or gas burner refusing to light? Boards, coils, igniters tested.',
     'Gas, electric and induction Wolf cooktops. Glass tops, touch panels and burners replaced.'],
    ['An induction cooktop flashing an error is often a generator board. Confirmed, then quoted.',
     'Written price before any work, 90 days on labor. Local Wolf techs, Evanston to Hinsdale.']),
'Wolf > Steam Oven Repair': (
    ['Wolf steam oven dry, leaking or stuck on a descale warning? Boiler, pump, sensors tested.',
     'Tank and plumbed steam ovens. Door seals, elements, pumps and boards replaced, OEM parts.'],
    ['Steam ovens are specialist work. Exact price quoted at your home, labor backed 90 days.',
     'Independent repair, not the factory. Same or next-day visits in most of Chicagoland.']),
'Wolf > Outdoor Grill Repair': (
    ['Wolf grill will not light or heats unevenly? Burners, igniters, valves, regulators fixed.',
     'Built-in Wolf grills, natural gas and propane. Rotisserie motors, side burners and knobs.'],
    ['Grill ready for the season or fixed mid-summer. Exact price first, 90 days on labor.',
     'Independent Wolf grill repair across Chicago, the North Shore and the western suburbs.']),
'Wolf > Brand & Areas': (
    ['Wolf ranges, wall ovens, rangetops, cooktops, steam ovens and grills repaired at home.',
     'Independent Wolf specialists. Price approved first, OEM parts, 90 days on labor.'],
    ['Local Wolf techs from the Gold Coast to Lake Forest and Hinsdale. Same-day when open.',
     'Name the model and the symptom. Diagnostic fee quoted on the call, credited to the repair.']),

'Viking > Refrigerator Repair': (
    ['Viking fridge warm, noisy or leaking? Fans, boards, sensors and sealed system tested.',
     'Viking Professional and Designer built-ins, 36 to 48 inches. Gaskets and fans replaced.'],
    ['A Viking fridge losing cold is often one part. Found, priced in writing, fixed that visit.',
     'Independent Viking repair across Chicago and the suburbs. 90 days on labor, phone 24/7.']),
'Viking > Range Repair': (
    ['Viking range clicking, burner dead or oven not heating? Igniters and sensors stocked.',
     'Dual fuel and gas Viking ranges, 30 to 60 inches. Hinges, glass and fans replaced.'],
    ['Viking oven stuck at a low temp? Usually an igniter or sensor. Confirmed, then priced.',
     'Gas smell? Call the utility first. For everything else on your Viking range, call us.']),
'Viking > Cooktop & Rangetop Repair': (
    ['Viking cooktop clicking, dead burner or weak flame? Igniters, modules and valves replaced.',
     'Gas and induction Viking cooktops. Griddles, burner caps, knobs and boards serviced.'],
    ['Exact price before any work, 90 days on labor. Independent Viking techs in Chicagoland.',
     'Most cooktop repairs finish in one visit because the common parts ride along in the van.']),
'Viking > Wall Oven Repair': (
    ['Viking wall oven cold, erratic or dark? Relays, boards, elements and sensors tested.',
     'Single and double Viking ovens. Hinges, gaskets, glass and fans replaced, price first.'],
    ['We decode the error, confirm the bad part and quote in writing before touching anything.',
     'Independent Viking oven repair from Lincoln Park to Naperville. Labor backed for 90 days.']),
'Viking > Wine Cellar Repair': (
    ['Viking wine cellar warming or cycling loudly? Each zone measured, fault isolated, quoted.',
     'Undercounter and full-height Viking wine units. Fans, sensors, seals and boards replaced.'],
    ['A warming cellar is a priority call. First open slot so the collection stops drifting.',
     'Viking wine units serviced from Lincoln Park to Lake Forest. 90 days on labor, phone 24/7.']),
'Viking > Ice Maker Repair': (
    ['Viking ice maker quiet, slow or leaking? Fill valve, line, mold and controls tested.',
     'Fridge ice makers and undercounter Viking ice machines. Written price first, 90-day labor.'],
    ['Water pressure, filter and sensors checked so the fix lasts. Phone answered 24/7.',
     'New ice maker assembly installed when a rebuild is not worth your money. Honest call.']),
'Viking > Brand & Areas': (
    ['Viking ranges, fridges, ovens, cooktops, wine cellars and ice makers repaired at home.',
     'Independent Viking specialists for Chicagoland. Price in writing first, 90 days on labor.'],
    ['Local Viking techs from Lincoln Park to Lake Forest and Naperville. Same-day when open.',
     'Model and symptom on the call, diagnostic quoted up front and credited when you approve.']),

'Miele > Washer Repair': (
    ['Miele washer stuck, not draining or flashing a fault? Pump, filter, lock and board tested.',
     'W1 and older Miele front-loaders. Bearings, pumps, valves and locks replaced, OEM parts.'],
    ['Door locked with a load inside? We release it, find the cause and quote before any work.',
     'Independent Miele repair across Chicago and the suburbs. 90 days on labor, phone 24/7.']),
'Miele > Dryer Repair': (
    ['Miele dryer running cold or taking three cycles? Heat pump, condenser and airflow checked.',
     'T1 heat pump and vented Miele dryers. Belts, motors, heaters and boards replaced.'],
    ['Long dry times are usually airflow or a sensor. Cause confirmed and quoted before work.',
     'Independent Miele techs from Evanston to Hinsdale. 90 days on labor, same-day when open.']),
'Miele > Oven & Steam Oven Repair': (
    ['Miele oven cold, stopping mid-bake or showing a fault? Boards, elements, sensors tested.',
     'Wall ovens, combi steam and speed ovens. Boilers, pumps, hinges and fans replaced.'],
    ['Exact price before work, 90 days on labor. Independent Miele specialists for Chicagoland.',
     'A fault code tells us where to start, not what to charge. Quote after we confirm the part.']),
'Miele > Refrigerator Repair': (
    ['Miele fridge warming, leaking or beeping? Fans, sensors, boards and sealed system tested.',
     'MasterCool columns and integrated Miele fridges. Gaskets, fans and ice makers replaced.'],
    ['Independent Miele repair across Chicagoland. Written price before work, 90 days on labor.',
     'Panel-ready units stay in the cabinet. Most repairs happen in place, nothing pulled out.']),
'Miele > Wine Cooler Repair': (
    ['Miele wine cooler warming or cycling loudly? Zones measured, fault isolated, then quoted.',
     'Built-in and freestanding Miele wine units. Fans, sensors, seals and boards replaced.'],
    ['Wine units are priority calls: first open slot so the bottles stop drifting. Phone 24/7.',
     'Independent Miele repair, Chicago and the suburbs. 90 days on labor, parts by their maker.']),
'Miele > Brand & Areas': (
    ['Miele washers, dryers, ovens, steam ovens, fridges and wine units repaired at your home.',
     'Independent Miele specialists. Written price first, genuine parts, 90 days on labor.'],
    ['Local Miele techs across Chicago, the North Shore and west suburbs. Same-day when open.',
     'Tell us the model and fault code. Diagnostic quoted on the call, credited to the repair.']),

'Thermador > Refrigerator Repair': (
    ['Thermador fridge warming, leaking or beeping? Fans, sensors, boards, sealed system tested.',
     'Freedom columns and Thermador built-ins. Gaskets, fans, boards and ice makers replaced.'],
    ['Independent Thermador repair in Chicagoland. Exact price before work, 90 days on labor.',
     'Panel-ready columns stay put. Most repairs happen in the cabinet without pulling the unit.']),
'Thermador > Range Repair': (
    ['Thermador range clicking, Star burner dead or oven slow? Igniters and sensors stocked.',
     'Pro Grand and Pro Harmony ranges, 30 to 60 inches. Hinges, glass and fans replaced.'],
    ['Exact price agreed before work, 90 days on labor. Independent Thermador techs in Chicago.',
     'Gas smell? Call the utility first. For anything else on your Thermador range, call us.']),
'Thermador > Cooktop Repair': (
    ['Thermador induction zone out or gas burner clicking? Boards, coils and igniters tested.',
     'Freedom induction, gas cooktops and rangetops. Glass, panels and burners replaced.'],
    ['Independent Thermador repair, Chicago and suburbs. Written price first, 90 days on labor.',
     'Most cooktop faults are one part. We confirm it, quote it and usually fix it that visit.']),
'Thermador > Wall Oven Repair': (
    ['Thermador wall oven cold, erratic or showing a code? Boards, relays and elements tested.',
     'Single, double and steam Thermador ovens. Hinges, gaskets, glass and fans replaced.'],
    ['Exact price before any work, 90 days on labor. Thermador techs, Evanston to Naperville.',
     'Dinner ovens get priority. Same or next-day slots in most of Chicago and the suburbs.']),
'Thermador > Wine Column Repair': (
    ['Thermador wine column warming or cycling loudly? Zones measured, fault isolated, quoted.',
     'Freedom wine columns and undercounter Thermador units. Fans, sensors, seals and boards.'],
    ['Wine columns are priority calls: first open slot so the collection stops drifting.',
     'Independent Thermador repair across Chicagoland. 90 days on labor, parts by their maker.']),
'Thermador > Brand & Areas': (
    ['Thermador ranges, fridge columns, cooktops, wall ovens and wine columns repaired at home.',
     'Independent Thermador specialists in Chicagoland. Price in writing first, 90-day labor.'],
    ['Local Thermador techs from River North to Lake Forest and Hinsdale. Same-day when open.',
     'Give us the model and the symptom. Diagnostic quoted up front, credited once you approve.']),

'Luxury & Built-In > All Brands': (
    ['Sub-Zero, Wolf, Viking, Miele and Thermador repaired at your home across Chicagoland.',
     'Built-in fridges, pro ranges, wall ovens, cooktops and wine units. Exact price first.'],
    ['Independent luxury appliance specialists. 90 days on labor, phone 24/7, fast openings.',
     'Five brands, one phone line. Techs dispatched locally from Evanston to Hinsdale.']),
}
