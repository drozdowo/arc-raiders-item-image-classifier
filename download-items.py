import os
import requests
from urllib.parse import urlparse
import re

items0 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/3/31/Advanced_ARC_Powercell.png/revision/latest?cb=20251017211003",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9b/Advanced_Electrical_Components.png/revision/latest?cb=20251031161616",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Advanced_Mechanical_Components.png/revision/latest?cb=20251018110145",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/47/Agave.png/revision/latest?cb=20251101173334",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a8/Agave_Juice.png/revision/latest?cb=20251103185208",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/03/Air_Freshener.png/revision/latest?cb=20251102000555",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/95/Alarm_Clock.png/revision/latest?cb=20251018124756",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f5/Antiseptic.png/revision/latest?cb=20251019025103",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/fc/Apricot.png/revision/latest?cb=20251031214626",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a6/ARC_Alloy.png/revision/latest?cb=20251017194039",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/dc/ARC_Circuitry.png/revision/latest?cb=20251019023050",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e9/ARC_Coolant.png/revision/latest?cb=20251017200845",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/29/ARC_Flex_Rubber.png/revision/latest?cb=20251019224937",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/ad/ARC_Motion_Core.png/revision/latest?cb=20251017193506",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/02/ARC_Performance_Steel.png/revision/latest?cb=20251018182411",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/df/ARC_Powercell.png/revision/latest?cb=20251030175812",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/72/ARC_Synthetic_Resin.png/revision/latest?cb=20251017201105",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0f/ARC_Thermo_Lining.png/revision/latest?cb=20251018201805",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/51/Assorted_Seeds.png/revision/latest?cb=20251030175558",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Bastion_Cell.png/revision/latest?cb=20251101235108",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6d/Battery.png/revision/latest?cb=20251017220232",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/fa/Bicycle_Pump.png/revision/latest?cb=20251018124904",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/01/Bloated_Tuna_Can.png/revision/latest?cb=20251030175248",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/46/Bombardier_Cell.png/revision/latest?cb=20251103110839",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/63/Breathtaking_Snow_Globe.png/revision/latest?cb=20251101173138",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/17/Broken_Flashlight.png/revision/latest?cb=20251019030210",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/93/Broken_Guidance_System.png/revision/latest?cb=20251018124649",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/3b/Broken_Handheld_Radio.png/revision/latest?cb=20251018214209",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/18/Broken_Taser.png/revision/latest?cb=20251030230120",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a5/Burned_ARC_Circuity.png/revision/latest?cb=20251017224237",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a6/Camera_Lens.png/revision/latest?cb=20251017220149",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/58/Candle_Holder.png/revision/latest?cb=20251019023130",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5f/Canister.png/revision/latest?cb=20251017234228",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/82/Cat_Bed.png/revision/latest?cb=20251030230250",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/92/Chemicals.png/revision/latest?cb=20251103114525",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/33/Coffee_Pot.png/revision/latest?cb=20251105050123",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/3d/Complex_Gun_Parts.png/revision/latest?cb=20251017200159",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/40/Coolant.png/revision/latest?cb=20251019022815",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/7f/Cooling_Coil.png/revision/latest?cb=20251018214413",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/13/Cooling_Fan.png/revision/latest?cb=20251018124546",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9a/Cracked_Bioscanner.png/revision/latest?cb=20251017201323",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/fc/Crude_Explosives.png/revision/latest?cb=20251017220117",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8e/Crumpled_Plastic_Bottle.png/revision/latest?cb=20251102060239",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9e/Damaged_ARC_Motion_Core.png/revision/latest?cb=20251018190625",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/58/Damaged_ARC_Powercell.png/revision/latest?cb=20251120190805",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d8/Damaged_Fireball_Burner.png/revision/latest?cb=20251018181312",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1f/Damaged_Heat_Sink.png/revision/latest?cb=20251018124446",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/96/Damaged_Hornet_Driver.png/revision/latest?cb=20251101164625",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/3a/Damaged_Rocketeer_Driver.png/revision/latest?cb=20251019023918",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d6/Damaged_Tick_Pod.png/revision/latest?cb=20251118141540",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e6/Damaged_Wasp_Driver.png/revision/latest?cb=20251120185310",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4d/Dart_Board.png/revision/latest?cb=20251101235455",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/7c/Deflated_Football.png/revision/latest?cb=20251017215928",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/37/Degraded_ARC_Rubber.png/revision/latest?cb=20251019024151",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1a/Diving_Goggles.png/revision/latest?cb=20251017201540",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c5/Dog_Collar.png/revision/latest?cb=20251017201659",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d0/Dried_Out_ARC_Resin.png/revision/latest?cb=20251019160040",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4e/Duct_Tape.png/revision/latest?cb=20251017215833",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Durable_Cloth.png/revision/latest?cb=20251017224200",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Electrical_Components.png/revision/latest?cb=20251018001702",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e1/Empty_Wine_Bottle.png/revision/latest?cb=20251018124240",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1b/Exodus_Modules.png/revision/latest?cb=20251019111209",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/91/Expired_Pasta.png/revision/latest?cb=20251030230437",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/ba/Expired_Respirator.png/revision/latest?cb=20251019035546",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/11/Explosive_Compound.png/revision/latest?cb=20251017202136",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2b/Fabric.png/revision/latest?cb=20251103114359",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0c/Faded_Photograph.png/revision/latest?cb=20251019030429",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Fertilizer.png/revision/latest?cb=20251103114050",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/44/Film_Reel.png/revision/latest?cb=20251031030223",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/94/Fine_Wristwatch.png/revision/latest?cb=20251101173825",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8b/Fireball_Burner.png/revision/latest?cb=20251017215746",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b6/Flow_Controller.png/revision/latest?cb=20251114120421",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/36/Frequency_Modulation_Box.png/revision/latest?cb=20251114120712",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/29/Fried_Motherboard.png/revision/latest?cb=20251018183445",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/81/FryingPanPNG.png/revision/latest?cb=20251101184322",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/88/Garlic_Press.png/revision/latest?cb=20251018182748",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/37/Geiger_Counter.png/revision/latest?cb=20251114144007",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0d/Great_Mullein.png/revision/latest?cb=20251018105757",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0f/Headphones.png/revision/latest?cb=20251030175043",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/33/Heavy_Gun_Parts.png/revision/latest?cb=20251106015823",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/bb/Hornet_Driver.png/revision/latest?cb=20251017202417",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e8/HouseholdCleanerPNG.png/revision/latest?cb=20251105051024",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4b/Humidifier.png/revision/latest?cb=20251019121059",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Ice_Cream_Scooper.png/revision/latest?cb=20251017215720",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a0/Impure_ARC_Coolant.png/revision/latest?cb=20251031014137",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Industrial_Battery.png/revision/latest?cb=20251017202635",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/66/Industrial_Charger.png/revision/latest?cb=20251018190809",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/38/Industrial_Magnet.png/revision/latest?cb=20251018001236",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e7/Ion_Sputter.png/revision/latest?cb=20251114115859",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e5/Laboratory_Reagents.png/revision/latest?cb=20251017202857",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ef/Lances_Mixtape.png/revision/latest?cb=20251018124400",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a0/Leaper_Pulse_Unit.png/revision/latest?cb=20251017200509",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/35/Lemon.png/revision/latest?cb=20251031172634",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Light_Gun_Parts.png/revision/latest?cb=20251106020115",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2c/Light_Bulb.png/revision/latest?cb=20251102000400",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8c/Magnet.png/revision/latest?cb=20251017224039",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5e/Magnetic_Accelerator.png/revision/latest?cb=20251019210950",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a2/Magnetron.png/revision/latest?cb=20251114160447",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/24/Matriarch_Reactor.png/revision/latest?cb=20251114003948",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/94/Mechanical_Components.png/revision/latest?cb=20251017225852",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9a/Medium_Gun_Parts.png/revision/latest?cb=20251018202459",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/62/Metal_Brackets.png/revision/latest?cb=20251018190513",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/89/Metal_Parts.png/revision/latest?cb=20251017210517",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2c/Microscope.png/revision/latest?cb=20251114120938",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9f/Mini_Centrifuge.png/revision/latest?cb=20251114111845",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0f/Mod_Components.png/revision/latest?cb=20251017224442",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/64/Moss.png/revision/latest?cb=20251017233839",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0f/Motor.png/revision/latest?cb=20251103111529",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8c/Mushroom.png/revision/latest?cb=20251018214820",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/74/Music_Box.png/revision/latest?cb=20251031214507",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/90/Music_Album.png/revision/latest?cb=20251030230551",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/51/Number_Plate.png/revision/latest?cb=20251017223932",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Oil.png/revision/latest?cb=20251017215553",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f3/Olives.png/revision/latest?cb=20251031172750",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/53/Painted_Box.png/revision/latest?cb=20251018124205",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Plastic_Parts.png/revision/latest?cb=20251017210329",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e2/Playing_Cards.png/revision/latest?cb=20251102161321",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c0/Pottery.png/revision/latest?cb=20251030174902",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6e/Polluted_Air_Filter.png/revision/latest?cb=20251018190712",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c6/Pop_Trigger.png/revision/latest?cb=20251017214952",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5f/Portable_TV.png/revision/latest?cb=20251017203154",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2b/Poster_Of_Natural_Wonders.png/revision/latest?cb=20251101235727",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/77/Power_Bank.png/revision/latest?cb=20251017203344",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f8/Power_Cable.png/revision/latest?cb=20251019025658",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b7/PowerRod.png/revision/latest?cb=20251103112207",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/80/Prickly_Pear.png/revision/latest?cb=20251101085304",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4e/Processor.png/revision/latest?cb=20251018202024",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/04/Projector.png/revision/latest?cb=20251101185504",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6b/Queen_Reactor.png/revision/latest?cb=20251107045522",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/31/Radio.png/revision/latest?cb=20251017203552",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b6/Radio_Relay.png/revision/latest?cb=20251114112628",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2c/Resin.png/revision/latest?cb=20251103111701",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6d/Recorder.png/revision/latest?cb=20251105052420",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1a/Red_Coral_Jewelry.png/revision/latest?cb=20251102162334",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f4/Remote_Control.png/revision/latest?cb=20251018183824",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a8/Ripped_Safety_Vest.png/revision/latest?cb=20251017215442",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/53/Rocketeet_Driver.png/revision/latest?cb=20251102155406",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8a/Rocket_Thruster.png/revision/latest?cb=20251122141321",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/57/Roots.png/revision/latest?cb=20251030230741",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b4/Rope.png/revision/latest?cb=20251018183918",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/77/Rosary.png/revision/latest?cb=20251102000010",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e4/Rotary_Encoder.png/revision/latest?cb=20251114112855",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/df/Rubber_Duck.png/revision/latest?cb=20251018124112",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1a/Rubber_Pad.png/revision/latest?cb=20251017203903",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/93/Rubber_Parts.png/revision/latest?cb=20251107101823",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9b/Ruined_Accordon.png/revision/latest?cb=20251101000302",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ee/Ruined_Baton.png/revision/latest?cb=20251018182900",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/7c/Ruined_Handcuffs.png/revision/latest?cb=20251018181859",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5c/Ruined_Parachute.png/revision/latest?cb=20251018181747",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cb/Ruined_Riot_Shield.png/revision/latest?cb=20251018183034",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c2/Ruined_Tactical_Vest.png/revision/latest?cb=20251018133957",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/bf/Rusted_Bolts.png/revision/latest?cb=20251017223831",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cf/Rusted_Gear.png/revision/latest?cb=20251017224333",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1a/Rusted_Shut_Medical_Kit.png/revision/latest?cb=20251102083926",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/30/Rusted_Tools.png/revision/latest?cb=20251017204135",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/33/Rusty_ARC_Steel.png/revision/latest?cb=20251019024635",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d8/Sample_Cleaner.png/revision/latest?cb=20251114144328",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9c/Sensors.png/revision/latest?cb=20251018131556",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/91/Sentinel_Firing_Core.png/revision/latest?cb=20251103113548",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b1/Shredder_Gryo.png/revision/latest?cb=20251114144935",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/de/Signal_Amplifier.png/revision/latest?cb=20251114182313",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/90/Silver_Teaspoon_Set.png/revision/latest?cb=20251102000807",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/da/Simple_Gun_Parts.png/revision/latest?cb=20251018111316",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/07/SnitchScannerPNG.png/revision/latest?cb=20251107084933",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ee/Speaker_Component.png/revision/latest?cb=20251017204352",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0e/Spectrometer.png/revision/latest?cb=20251114144554",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ee/Spectrum_Analyizer.png/revision/latest?cb=20251114120116",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/58/Spotter_Relay.png/revision/latest?cb=20251018181630",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/29/SpringCushionPNG.png/revision/latest?cb=20251101183755",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8a/Statuette.png/revision/latest?cb=20251101173502",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/db/Steel_Spring.png/revision/latest?cb=20251017215346",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a9/Surveyor_Vault.png/revision/latest?cb=20251019210905",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8e/Synthesized_Fuel.png/revision/latest?cb=20251022001344",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/17/Syringe.png/revision/latest?cb=20251017204737",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/35/Tattered_ARC_Lining.png/revision/latest?cb=20251022001931",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c4/Tattered_Clothes.png/revision/latest?cb=20251018181427",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a8/Telemetry_Transceiver.png/revision/latest?cb=20251114144831",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9a/Thermostat.png/revision/latest?cb=20251019025847",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/95/Tick_Pod.png/revision/latest?cb=20251017215236",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/50/Toaster.png/revision/latest?cb=20251019025608",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cc/Torn_Book.png/revision/latest?cb=20251030175412",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/af/Torn_Blanket.png/revision/latest?cb=20251018201522",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f1/Turbo_Pump.png/revision/latest?cb=20251103111348",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/37/Unusable_Weapon.png/revision/latest?cb=20251101045758",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6e/Vase.png/revision/latest?cb=20251102162532",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a4/Very_Comfortable_Pillow.png/revision/latest?cb=20251102000155",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/26/Volcanic_Rock.png/revision/latest?cb=20251019023713",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c7/Voltage_Converter.png/revision/latest?cb=20251017205004",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/30/Wasp_Driver.png/revision/latest?cb=20251017205624",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/48/Water_Filter.png/revision/latest?cb=20251017205208",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/28/Water_Pump.png/revision/latest?cb=20251017205359",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/39/Wires.png/revision/latest?cb=20251017215155",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f5/Antiseptic.png/revision/latest?cb=20251019025103",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a6/ARC_Alloy.png/revision/latest?cb=20251017194039",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6d/Battery.png/revision/latest?cb=20251017220232",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Durable_Cloth.png/revision/latest?cb=20251017224200",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Fertilizer.png/revision/latest?cb=20251103114050",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0d/Great_Mullein.png/revision/latest?cb=20251018105757",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/bb/Hornet_Driver.png/revision/latest?cb=20251017202417",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a0/Leaper_Pulse_Unit.png/revision/latest?cb=20251017200509",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b6/Flow_Controller.png/revision/latest?cb=20251114120421",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b7/PowerRod.png/revision/latest?cb=20251103112207",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/53/Rocketeet_Driver.png/revision/latest?cb=20251102155406",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/39/Wires.png/revision/latest?cb=20251017215155",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/07/SnitchScannerPNG.png/revision/latest?cb=20251107084933",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a9/Surveyor_Vault.png/revision/latest?cb=20251019210905",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/17/Syringe.png/revision/latest?cb=20251017204737",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/30/Wasp_Driver.png/revision/latest?cb=20251017205624",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/28/Water_Pump.png/revision/latest?cb=20251017205359",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a2/Magnetron.png/revision/latest?cb=20251114160447",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c5/Dog_Collar.png/revision/latest?cb=20251017201659",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/35/Lemon.png/revision/latest?cb=20251031172634",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/fc/Apricot.png/revision/latest?cb=20251031214626",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/80/Prickly_Pear.png/revision/latest?cb=20251101085304",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f3/Olives.png/revision/latest?cb=20251031172750",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/82/Cat_Bed.png/revision/latest?cb=20251030230250",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8c/Mushroom.png/revision/latest?cb=20251018214820",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a4/Very_Comfortable_Pillow.png/revision/latest?cb=20251102000155",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/89/Metal_Parts.png/revision/latest?cb=20251017210517",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/93/Rubber_Parts.png/revision/latest?cb=20251107101823",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/30/Rusted_Tools.png/revision/latest?cb=20251017204135",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/94/Mechanical_Components.png/revision/latest?cb=20251017225852",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/30/Wasp_Driver.png/revision/latest?cb=20251017205624",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cf/Rusted_Gear.png/revision/latest?cb=20251017224333",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Advanced_Mechanical_Components.png/revision/latest?cb=20251018110145",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/91/Sentinel_Firing_Core.png/revision/latest?cb=20251103113548",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Plastic_Parts.png/revision/latest?cb=20251017210329",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2b/Fabric.png/revision/latest?cb=20251103114359",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f8/Power_Cable.png/revision/latest?cb=20251019025658",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Electrical_Components.png/revision/latest?cb=20251018001702",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/bb/Hornet_Driver.png/revision/latest?cb=20251017202417",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Industrial_Battery.png/revision/latest?cb=20251017202635",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9b/Advanced_Electrical_Components.png/revision/latest?cb=20251031161616",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Bastion_Cell.png/revision/latest?cb=20251101235108",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/92/Chemicals.png/revision/latest?cb=20251103114525",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a6/ARC_Alloy.png/revision/latest?cb=20251017194039",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8e/Synthesized_Fuel.png/revision/latest?cb=20251022001344",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/fc/Crude_Explosives.png/revision/latest?cb=20251017220117",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c6/Pop_Trigger.png/revision/latest?cb=20251017214952",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e5/Laboratory_Reagents.png/revision/latest?cb=20251017202857",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/11/Explosive_Compound.png/revision/latest?cb=20251017202136",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/53/Rocketeet_Driver.png/revision/latest?cb=20251102155406",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9a/Cracked_Bioscanner.png/revision/latest?cb=20251017201323",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Durable_Cloth.png/revision/latest?cb=20251017224200",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/95/Tick_Pod.png/revision/latest?cb=20251017215236",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1a/Rusted_Shut_Medical_Kit.png/revision/latest?cb=20251102083926",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f5/Antiseptic.png/revision/latest?cb=20251019025103",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a9/Surveyor_Vault.png/revision/latest?cb=20251019210905",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1f/Damaged_Heat_Sink.png/revision/latest?cb=20251018124446",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/07/SnitchScannerPNG.png/revision/latest?cb=20251107084933",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/29/Fried_Motherboard.png/revision/latest?cb=20251018183445",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a0/Leaper_Pulse_Unit.png/revision/latest?cb=20251017200509",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/df/ARC_Powercell.png/revision/latest?cb=20251030175812",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/50/Toaster.png/revision/latest?cb=20251019025608",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/ad/ARC_Motion_Core.png/revision/latest?cb=20251017193506",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8b/Fireball_Burner.png/revision/latest?cb=20251017215746",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0f/Motor.png/revision/latest?cb=20251103111529",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/dc/ARC_Circuitry.png/revision/latest?cb=20251019023050",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/46/Bombardier_Cell.png/revision/latest?cb=20251103110839",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/93/Rubber_Parts.png/revision/latest?cb=20251107101823",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/89/Metal_Parts.png/revision/latest?cb=20251017210517",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a6/ARC_Alloy.png/revision/latest?cb=20251017194039",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/25/Durable_Cloth.png/revision/latest?cb=20251017224200",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6d/Battery.png/revision/latest?cb=20251017220232",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Electrical_Components.png/revision/latest?cb=20251018001702",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/39/Wires.png/revision/latest?cb=20251017215155",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9c/Sensors.png/revision/latest?cb=20251018131556",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/db/Steel_Spring.png/revision/latest?cb=20251017215346",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9b/Advanced_Electrical_Components.png/revision/latest?cb=20251031161616",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4b/Humidifier.png/revision/latest?cb=20251019121059",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2c/Light_Bulb.png/revision/latest?cb=20251102000400",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/13/Cooling_Fan.png/revision/latest?cb=20251018124546",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a0/Leaper_Pulse_Unit.png/revision/latest?cb=20251017200509",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5e/Magnetic_Accelerator.png/revision/latest?cb=20251019210950",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1b/Exodus_Modules.png/revision/latest?cb=20251019111209"
]

items = [
  "https://static.wikia.nocookie.net/arc-raiders/images/8/88/Aphelion.png/revision/latest?cb=20251122123900",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/86/Anvil_I.png/revision/latest?cb=20251021193917",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/88/Arpeggio_1.png/revision/latest?cb=20251022201753",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e1/Bettina_1.png/revision/latest?cb=20251104001701",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/19/Bobcat_I.png/revision/latest?cb=20251106012231",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e8/Burletta_I.png/revision/latest?cb=20251021194234",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/96/Equalizer.png/revision/latest?cb=20251109013823",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6c/Ferro_I.png/revision/latest?cb=20251021194623",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/00/Hairpin_I.png/revision/latest?cb=20251021194555",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/44/Hullcracker_1.png/revision/latest?cb=20251104001735",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/dc/IL_Toro_I.png/revision/latest?cb=20251021194056",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/68/Jupiter.png/revision/latest?cb=20251109013920",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/56/Kettle_I.png/revision/latest?cb=20251021194721",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/81/Osprey.png/revision/latest?cb=20251031020121",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f7/Rattler_1.png/revision/latest?cb=20251021182304",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/36/Renegade_1.png/revision/latest?cb=20251104001753",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9c/Sticher_I.png/revision/latest?cb=20251021193847",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/3f/Tempest_I.png/revision/latest?cb=20251105061405",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/64/Torrente_1.png/revision/latest?cb=20251104001811",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ef/Venator_I.png/revision/latest?cb=20251108050534"
]

items2 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4d/Vertical_Grip_I.png/revision/latest?cb=20251023192033",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b5/Angled_Grip_I.png/revision/latest?cb=20251023191821",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d1/Stable_Stock_1.png/revision/latest?cb=20251018223535",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4f/Muzzle_Brake_I.png/revision/latest?cb=20251023191948",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5f/Compensator_I.png/revision/latest?cb=20251103202418",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/07/Shotgun_Choke_I.png/revision/latest?cb=20251023192012",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9c/Extended_Light_Mag_1.png/revision/latest?cb=20251018223434",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/44/Extended_Medium_Mag_I.png/revision/latest?cb=20251023192146",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/9b/Extended_Shotgun_Mag_I.png/revision/latest?cb=20251023191914",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/66/Vertical_Grip_2.png/revision/latest?cb=20251018220054",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b4/Stable_Stock_II.png/revision/latest?cb=20251103203600",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/23/Muzzle_Brake_II.png/revision/latest?cb=20251111231804",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f7/Silencer_I.png/revision/latest?cb=20251103203836",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/63/Shotgun_Choke_II.png/revision/latest?cb=20251103204040",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cf/Extended_Light_Mag_II.png/revision/latest?cb=20251103204420",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0a/Compensator_II.png/revision/latest?cb=20251103204639",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/50/Extended_Medium_Mag_II.png/revision/latest?cb=20251103195746",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4f/Extended_Shotgun_Mag_II.png/revision/latest?cb=20251103195919",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/20/Vertical_Grip_III.png/revision/latest?cb=20251111232103",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0f/Angled_Grip_III.png/revision/latest?cb=20251103205211",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/eb/Stable_Stock_III.png/revision/latest?cb=20251103195130",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cb/Lightweight_Stock.png/revision/latest?cb=20251104202749",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4b/Padded_Stock.png/revision/latest?cb=20251103205441",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a2/Muzzle_Brake_III.png/revision/latest?cb=20251104202616",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f1/Compensator_3.png/revision/latest?cb=20251129130508",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c0/Silencer_II.png/revision/latest?cb=20251103195559",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/3e/Silencer_III.png/revision/latest?cb=20251031143554",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2f/Extended_Barrel.png/revision/latest?cb=20251111082553",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/36/Shotgun_Choke_III.png/revision/latest?cb=20251110003008",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4d/Shotgun_Silencer.png/revision/latest?cb=20251104202940",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/a1/Extended_Medium_Mag_III.png/revision/latest?cb=20251110002748",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/71/Kinetic_Converter.png/revision/latest?cb=20251018215742",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ef/Anvil_Splitter.png/revision/latest?cb=20251104013322"
]

items3 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/2/24/Blaze_Grenade.png/revision/latest?cb=20251018223728",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c7/Deadline.png/revision/latest?cb=20251113113219",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/22/Explosive_Mine.png/revision/latest?cb=20251107064337",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8b/Fireball_Burner.png/revision/latest?cb=20251017215746",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/fe/Gas_Grenade.png/revision/latest?cb=20251107064229",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/ce/Gas_Mine.png/revision/latest?cb=20251113113239",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/14/Heavy_Fuse_Grenade.png/revision/latest?cb=20251018223820",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/bb/Hornet_Driver.png/revision/latest?cb=20251017202417",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5a/Jolt_Mine.png/revision/latest?cb=20251018224033",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4c/Light_Impact_Grenade.png/revision/latest?cb=20251023193326",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/19/Lil_Smoke_Grenade.png/revision/latest?cb=20251107064119",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/77/Lure_Grenade.png/revision/latest?cb=20251107062410",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/92/Lure_Grenade_Trap.png/revision/latest?cb=20251113131138",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/af/Pulse_Mine.png/revision/latest?cb=20251113113301",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/35/Seeker_Grenade.png/revision/latest?cb=20251114124101",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/18/Showstopper.png/revision/latest?cb=20251021010744",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5f/Shrapnel_Grenade.png/revision/latest?cb=20251019025229",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d5/Smoke_Grenade.png/revision/latest?cb=20251023193441",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/ac/Smoke_Grenade_Trap.png/revision/latest?cb=20251107061320",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/77/Snap_Blast_Grenade.png/revision/latest?cb=20251018224130",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/07/SnitchScannerPNG.png/revision/latest?cb=20251107084933",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8e/Synthesized_Fuel.png/revision/latest?cb=20251022001344",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/40/Tagging_grenade.png/revision/latest?cb=20251109072249",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/89/Trailblazer.png/revision/latest?cb=20251114161237",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/09/Trigger_Nade.png/revision/latest?cb=20251108210320",
  "https://static.wikia.nocookie.net/arc-raiders/images/3/30/Wasp_Driver.png/revision/latest?cb=20251017205624",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/24/Wolfpack.png/revision/latest?cb=20251021010959",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/4c/Light_Impact_Grenade.png/revision/latest?cb=20251023193326",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/19/Lil_Smoke_Grenade.png/revision/latest?cb=20251107064119",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/af/Blaze_Grenade_Trap.png/revision/latest?cb=20251122090531",
  "https://static.wikia.nocookie.net/arc-raiders/images/a/ac/Smoke_Grenade_Trap.png/revision/latest?cb=20251107061320",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/92/Lure_Grenade_Trap.png/revision/latest?cb=20251113131138"
]

items4 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/2/22/Light_Ammo.png/revision/latest?cb=20251023192357",
  "https://static.wikia.nocookie.net/arc-raiders/images/d/d3/Medium_Ammo.png/revision/latest?cb=20251023190631",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6f/Heavy_Ammo.png/revision/latest?cb=20251023190604",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/61/Shotgun_Ammo.png/revision/latest?cb=20251023192306"
]

items5 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cf/Free_Loadout_Augment.png/revision/latest?cb=20251018220835",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/79/Looting_MK_1.png/revision/latest?cb=20251018220906",
  "https://static.wikia.nocookie.net/arc-raiders/images/b/b5/Tactical_Mk1.png/revision/latest?cb=20251104003825",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/72/Combat_MK_1.png/revision/latest?cb=20251018220431",
  "https://static.wikia.nocookie.net/arc-raiders/images/8/8d/Looting_MK2.png/revision/latest?cb=20251104002824",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2b/Tactical_Mk2.png/revision/latest?cb=20251104003844",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f7/Combat_Mk2.png/revision/latest?cb=20251104003900",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/e6/Looting_MK_Survivor.png/revision/latest?cb=20251104002954",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/24/Looting_MK3_Cautious.png/revision/latest?cb=20251104002936",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6c/Tactical_Mk3_Healing.png/revision/latest?cb=20251104002920",
  "https://static.wikia.nocookie.net/arc-raiders/images/e/ec/Combat_MK3_Aggresive.png/revision/latest?cb=20251104002857"
]

items6 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/4/40/Light_Shield.png/revision/latest?cb=20251023201155",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/41/Medium_Shield.png/revision/latest?cb=20251023201610",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/f9/Heavy_Shield.png/revision/latest?cb=20251105051729"
]

items7 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/7/74/Binoculars.png/revision/latest?cb=20251023194600",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cb/Barricade_Kit.png/revision/latest?cb=20251018224705",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/68/Door_Blocker.png/revision/latest?cb=20251018224750",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5c/Noisemaker.png/revision/latest?cb=20251023194111",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/06/Photoelectric_Cloak.png/revision/latest?cb=20251105051902",
  "https://static.wikia.nocookie.net/arc-raiders/images/6/6d/Recorder.png/revision/latest?cb=20251105052420",
  "https://static.wikia.nocookie.net/arc-raiders/images/f/ff/Remote_Raider_Flare.png/revision/latest?cb=20251023193349",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/56/Snap_Hook.png/revision/latest?cb=20251108205608",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c7/Zip_Line.png/revision/latest?cb=20251105053335",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/27/Green_Light_Stick.png/revision/latest?cb=20251023194001",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/cc/Blue_Light_Stick.png/revision/latest?cb=20251023193940",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/93/Red_Light_Stick.png/revision/latest?cb=20251023194027",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1f/Yellow_Light_Stick.png/revision/latest?cb=20251023194050"
]

items8 = [
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1b/Adrenaline_Shot.png/revision/latest?cb=20251018224349",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0c/Bandage.png/revision/latest?cb=20251018224237",
  "https://static.wikia.nocookie.net/arc-raiders/images/5/5f/Defibrillator.png/revision/latest?cb=20251018224548",
  "https://static.wikia.nocookie.net/arc-raiders/images/2/2b/Fabric.png/revision/latest?cb=20251103114359",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c5/Herbal_Bandage.png/revision/latest?cb=20251022204651",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/44/Shield_Recharger.png/revision/latest?cb=20251022204737",
  "https://static.wikia.nocookie.net/arc-raiders/images/9/99/Sterilized_Bandage.png/revision/latest?cb=20251022204802",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c9/Surge_Shield_Recharger.png/revision/latest?cb=20251023201545",
  "https://static.wikia.nocookie.net/arc-raiders/images/7/7d/Vita_Shot.png/revision/latest?cb=20251105055941",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1d/Vita_Spray.png/revision/latest?cb=20251105055537",
  "https://static.wikia.nocookie.net/arc-raiders/images/1/1b/Adrenaline_Shot.png/revision/latest?cb=20251018224349",
  "https://static.wikia.nocookie.net/arc-raiders/images/0/0c/Bandage.png/revision/latest?cb=20251018224237",
  "https://static.wikia.nocookie.net/arc-raiders/images/c/c5/Herbal_Bandage.png/revision/latest?cb=20251022204651",
  "https://static.wikia.nocookie.net/arc-raiders/images/4/44/Shield_Recharger.png/revision/latest?cb=20251022204737"
]

items_all = set(items0 + items + items2 + items3 + items4 + items5 + items6 + items7 + items8)

def sanitize_folder_name(name):
    """Remove file extension and sanitize the name for folder creation"""
    # Remove .png extension
    name = re.sub(r'\.png$', '', name, flags=re.IGNORECASE)
    # Replace spaces and special characters
    name = name.replace(' ', '_')
    return name

def download_image(url, base_path='./arc-raiders-items'):
    """Download image from URL and save to appropriate folder"""
    try:
        # Parse the URL to get the filename
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.split('/')
        
        # Get the image filename (before /revision/)
        filename = None
        for i, part in enumerate(path_parts):
            if part.endswith('.png'):
                filename = part
                break
        
        if not filename:
            print(f"Could not extract filename from {url}")
            return False
        
        # Create folder name from filename
        folder_name = sanitize_folder_name(filename)
        folder_path = os.path.join(base_path, folder_name)
        
        # Create folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Download the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Save the image
        image_path = os.path.join(folder_path, '1.png')
        with open(image_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Downloaded {filename} to {folder_name}/")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to download {url}: {e}")
        return False
    except Exception as e:
        print(f"✗ Error processing {url}: {e}")
        return False

def main():
    print(f"Starting download of {len(items_all)} items...")
    print("-" * 60)
    
    successful = 0
    failed = 0
    
    for url in items_all:
        if download_image(url):
            successful += 1
        else:
            failed += 1
    
    print("-" * 60)
    print(f"Download complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    main()
