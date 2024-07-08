# Path to the CSV file for the first uncleaned scrape
CSV_UNFILTERED = '../tables/bird_recordings_unfiltered.csv'
# Path to the CSV file for the filtered table
CSV_FILTERED = '../tables/bird_recordings_filtered.csv'



# Path to the CSV file used for the heatmap
CSV_FILE_PATH_HEATMAP = CSV_UNFILTERED
# Path to the CSV file used for the statistics
CSV_FILE_PATH_STATS = CSV_FILTERED

HEATMAP_FILE = '../heatmaps/bird_recordings_heatmap.html'

# Statistics thresholds and parameters
MIN_RECORDINGS_THRESHOLD = 50
FIGURE_SIZE = (10, 6)
BAR_COLOR = 'blue'
ROTATION = 90


#Model to be used in predict.py
TEST_MODEL = '../model/bird_sound_model_final.keras'

# Additional statistics
SPECIES_WITH_MAX_LATITUDE = 'species_with_max_latitude'
SPECIES_WITH_MIN_LONGITUDE = 'species_with_min_longitude'
AVERAGE_LATITUDE = 'average_latitude'
AVERAGE_LONGITUDE = 'average_longitude'
