from config import *

copy_gz("historical_dc_original", "historical_dc_copy")
dfo = get_df("historical_dc_copy")
dfc = get_df("historical_dc_original")
load_db(dfc, 'historical_dc_copy')