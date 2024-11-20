import pyautogui
import keyboard
import time

# List of invasive plants
invasive_plants = {
    "Alternanthera philoxeroides": "Aligatorska alternantera",
    "Ambrosia artemisiifolia": "Ambrozija /pelinolistna ambrozija / žvrklja",
    "Acer negundo": "Amerikanski javor",
    "Lysichiton americanus": "Ameriški lizihiton",
    "Parthenium hysterophorus": "Ameriški ščetinasti vratič",
    "Cortaderia jubata": "Andska pampaška trava",
    "Myriophyllum aquaticum": "Brazilski rmanec",
    "Gunnera tinctoria": "Čilenska gunera",
    "Buddleja davidii": "Davidova budleja, tudi metuljnik",
    "Erigeron annuus": "Enoletna suholetnica",
    "Humulus scandens": "Enoletni hmelj",
    "Spiraea japonica": "Japonska medvejka",
    "Lygodium japonicum": "Japonska vzpenjava praprot",
    "Fallopia japonica": "Japonski dresnik",
    "Solidago canadensis sp.": "Kanadska zlata rozga",
    "Lespedeza cuneata": "Kitajska grmasta detelja",
    "Triadica sebifera": "Kitajski lojevec",
    "Lagarosiphon major": "Kodrasta vodna zel",
    "Pueraria montana var. lobata": "Kudzu",
    "Prosopis juliflora": "Mehiški meskit",
    "Lupinus polyphyllus": "Mnogolistni volčji bob",
    "Phytolacca americana": "Navadna barvilnica",
    "Aster spp.": "Nebine, astre",
    "Rhus typhina": "Octovec",
    "Solidago gigantea": "Orjaška zlata rozga",
    "Heracleum mantegazzianum": "Orjaški dežen",
    "Heracleum persicum": "Perzijski dežen",
    "Hydrocotyle ranunculoides": "Plavajoči popnjak",
    "Ludwigia peploides": "Plazeča ludvigija",
    "Microstegium vimineum": "Pletarska hoduljevka",
    "Persicaria perfoliata/Polygonum perfoliatum": "Plezajoča dresen",
    "Myriophyllum heterophyllum": "Raznolistni rmanec",
    "Robinia pseudoacacia": "Robinija",
    "Rudbeckia sp.": "Rudbekija",
    "Asclepias syriaca": "Sirska svilnica",
    "Heracleum sosnowskyi": "Sosnovskijev dežen",
    "Pennisetum setaceum": "Ščetinasta perjanka",
    "Berberis thunbergii": "Thunbergov češmin",
    "Helianthus tuberosus": "Topinambur",
    "Ehrharta calycina": "Trajna guboplevka",
    "Cardiospermum grandiflorum": "Velika korinda",
    "Ailanthus altissima": "Veliki pajesen",
    "Salvinia molesta": "Veliki plavček",
    "Ludwigia grandiflora": "Velikocvetna ludvigija",
    "Andropogon virginicus": "Viržinski kršin",
    "Eichornia crassipes": "Vodna hijacinta",
    "Elodea canadensis": "Vodna kuga ali račja zel",
    "Pistia stratiotes": "Vodna solata",
    "Acacia saligna": "Vrbolistna akacija",
    "Baccharis halimifolia": "Vzhodni bakaris",
    "Elodea nuttallii": "Zahodna račja zel",
    "Cabomba caroliniana": "Zelena kabomba",
    "Impatiens glandulifera": "Žlezava nedotika"
}

# Creating a Python dictionary from the provided list
species_in_inaturalist = {
    "Acacia saligna": "Vrbasta Akacija",
    "Acer negundo": "Amerikanski Javor",
    "Ailanthus altissima": "Veliki Pajesen",
    "Alternanthera philoxeroides": None,
    "Ambrosia artemisiifolia": "Pelinolistna Žvrklja",
    "Andropogon virginicus": "Kompleks",
    "Asclepias syriaca": "Sirska Svilnica",
    "Baccharis halimifolia": None,
    "Berberis thunbergii": "Thunbergov Češmin",
    "Buddleja davidii": "Davidova Budleja",
    "Cabomba caroliniana": None,
    "Cardiospermum grandiflorum": None,
    "Cenchrus setaceus": None,
    "Cortaderia jubata": None,
    "Ehrharta calycina": None,
    "Elodea canadensis": "Vodna Kuga",
    "Elodea nuttallii": None,
    "Erigeron annuus": "Enoletna Suholetnica",
    "Gunnera tinctoria": None,
    "Helianthus tuberosus": "Topinambur",
    "Heracleum mantegazzianum": "Kompleks",
    "Heracleum persicum": None,
    "Heracleum sosnowskyi": None,
    "Humulus scandens": None,
    "Hydrocotyle ranunculoides": None,
    "Impatiens glandulifera": "Žlezava Nedotika",
    "Lagarosiphon major": None,
    "Lespedeza cuneata": None,
    "Ludwigia grandiflora": None,
    "Ludwigia peploides": None,
    "Lupinus polyphyllus": "Mnogolistni Volčji Bob",
    "Lygodium japonicum": None,
    "Lysichiton americanus": None,
    "Microstegium vimineum": None,
    "Myriophyllum aquaticum": None,
    "Myriophyllum heterophyllum": None,
    "Neltuma juliflora": None,
    "Parthenium hysterophorus": None,
    "Phytolacca americana": "Navadna Barvilnica",
    "Pistia stratiotes": None,
    "Pontederia crassipes": None,
    "Reynoutria japonica": "Japonski Dresnik",
    "Rhus typhina": "Octovec",
    "Robinia pseudoacacia": "Robinija",
    "Rudbeckia fulgida var. speciosa": None,
    "Salvinia molesta": None,
    "Solidago gigantea": "Orjaška Zlata Rozga",
    "Spiraea japonica": None,
    "Triadica sebifera": None
}


print(len(invasive_plants))

'''
# To find current mouse positions

while True:
    if keyboard.is_pressed("esc"):  # Check if the 'Esc' key is pressed
        print("Script stopped by user.")
        break
    window_x, window_y = pyautogui.position()
    print(f"x={window_x}, y={window_y}")
'''

# Delay for setup
print("Navigate to the website and place the mouse over the input window.")
time.sleep(5)

# Gather the current mouse position
window_x, window_y = pyautogui.position()
print(f"Mouse position recorded at: x={window_x}, y={window_y}")

dropdown_x = window_x 
dropdown_y = window_y + 40

# Confirmation message and delay before starting
print("Starting the automation in 5 seconds...")
time.sleep(5)

# Loop through the list of plants
for plant in invasive_plants:

    if keyboard.is_pressed("esc"):  # Check if the 'Esc' key is pressed
        print("Script stopped by user.")
        break

    # Click on the recorded location
    pyautogui.click(window_x, window_y)
    time.sleep(0.5)  # Wait to ensure the click is registered

    # Type the plant name
    pyautogui.typewrite(plant)
    time.sleep(1.5)  # Wait briefly before pressing Enter

    # Click dropdown
    pyautogui.click(dropdown_x, dropdown_y)
    time.sleep(1)  # Wait before moving to the next element
