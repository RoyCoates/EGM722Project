# Imports the required packages
import os
import pandas as pd               # Used for data handling
import geopandas as gpd           # Core for spatial data operations
import matplotlib.pyplot as plt   # For creating the bar chart
import folium                     # Main mapping library
from folium.plugins import MeasureControl  # For measurement tool
from folium import FeatureGroup, TileLayer  # For layer control and base maps


#Load the required Shapefiles stored in the data_file file
def load_geospatial_data() -> tuple:
    """Loads all geospatial datasets from specified file paths.

    Returns:
        tuple: Contains 6 GeoDataFrames in this order:
            (MarkerPosts, Filter_Drains, Gully, Junctions,
             Lighting_Column, Boundary)
    """
    # These are the shapefiles stored in the "data_files" file that we want to display on the map
    MarkerPosts = gpd.read_file('data_files/MarkerPost_100M.shp')
    Filter_Drains = gpd.read_file('data_files/FD_Filter_Drain.shp')
    Gully = gpd.read_file('data_files/GY_Gully.shp')
    Junctions = gpd.read_file('data_files/Junctions.shp')
    Lighting_Column = gpd.read_file('data_files/LP_Lighting_Point.shp')
    Boundary = gpd.read_file('data_files/MMaRC_B_Boundary.shp')

    return MarkerPosts, Filter_Drains, Gully, Junctions, Lighting_Column, Boundary

# The shapefiles are in ITM. This will convert them to WGS84 so they can be used with open street map
def convert_to_wgs84(*gdfs: gpd.GeoDataFrame) -> tuple:
    """Converts GeoDataFrames to WGS84 (EPSG:4326) coordinate system.

    Args:
        *gdfs: Variable number of GeoDataFrames to convert

    Returns:
        tuple: Converted GeoDataFrames in same order as input
    """
    return [gdf.to_crs("EPSG:4326") for gdf in gdfs]

# Create a Bar Chart from the Lighting Data showing the number of Lighting Columns Scheduled for Change at each Junction

def create_bar_chart(lighting_data: gpd.GeoDataFrame, top_n: int = 10) -> None:
    """Generates a bar chart comparing total vs scheduled lighting column upgrades."""
    junction_counts = lighting_data.groupby('Junction').agg(
        Total_Lamps=('Unique_Ass', 'count'),
        Lamps_to_Change=('ScheduledF', lambda x: (x == 'Yes').sum())
    ).reset_index().sort_values('Lamps_to_Change', ascending=False)

    plt.figure(figsize=(14, 7))
    ax = plt.subplot(111)
    colors = ['#ff7f0e', '#2ca02c']

    junction_counts.head(top_n).plot(
        x='Junction',
        y=['Total_Lamps', 'Lamps_to_Change'],
        kind='bar',
        ax=ax,
        color=colors,
        edgecolor='black'
    )

    plt.title('No. of Lighting Columns Scheduled for Change at Each Junction',
             fontsize=16, pad=20)
    plt.xlabel('Junction ID', fontsize=12, labelpad=15)
    plt.ylabel('Number of Lighting Columns', fontsize=12, labelpad=15)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3,
                    fontsize=10, color='black', fmt='%d')

    plt.legend(['Total Lighting Columns', 'Scheduled for Upgrade'],
              fontsize=12, bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()

# To run the code
if __name__ == "__main__":
    # Load and prepare data
    raw_data = load_geospatial_data()
    wgs84_data = convert_to_wgs84(*raw_data)
    MarkerPosts, Filter_Drains, Gully, Junctions, Lighting_Column, Boundary = wgs84_data

    # Create and display the bar chart
    create_bar_chart(Lighting_Column)

    # Create base map that zooms into Junction 5 - The first junction that works are scheduled for.
    m = folium.Map(
        location=[52.5856, -8.7211],
        zoom_start=18,
        tiles="Esri.WorldImagery"
    )

    # Add OpenStreetMap as an additional base layer. The basemaps can be changed
    TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)

    # Add the Boundary polygon
    Boundary.explore(
        m=m,
        color='red',
        style_kwds={'fill': False},
        name='MMaRC_B_Boundary'
    )

    # Add the Gully points
    Gully.explore(
        m=m,
        marker_kwds={
            'radius': 5,
            'fill': True,
            'fillColor': 'yellow',
            'color': 'black',
            'weight': 1.5,
            'fillOpacity': 1
        },
        name='Gully'
    )

    # Add the Filter Drains lines
    Filter_Drains.explore(
        m=m,
        color='blue',
        style_kwds={'weight': 1.5},
        name='Filter Drains'
    )

    # Add the Junctions and Junction Labels
    for idx, row in Junctions.iterrows():
        if not row.geometry.is_empty and pd.notnull(row['Junction_N']):
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=folium.Icon(
                    color='lightred',
                    icon='map-pin',
                    prefix='fa',
                    icon_size=(25, 25)
                )
            ).add_to(m)

            # Junction Label
            label = folium.DivIcon(
                html=f"""<div style="
                    color: lightred;
                    font-size: 20px;
                    font-weight: bold;
                    position: absolute;
                    transform: translate(-50%, -125%);
                    z-index: 9999;">{row['Junction_N']}</div>"""
            )
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=label,
                icon_size=(0, 0)
            ).add_to(m)

    # Add the Lighting Columns
    Lighting_Column.explore(
        m=m,
        column='ScheduledF',
        categorical=True,
        categories=['Yes', 'No'],
        cmap=['green', 'orange'],
        marker_kwds={'radius': 7},
        name='Lighting Columns'
    )

    # Add the Marker Posts
    MarkerPosts.explore(
        m=m,
        color='red',
        marker_kwds={'radius': 5},
        name='Marker Posts'
    )

    # Create a Legend for the map using CSS classes
    legend_html = """
    <div class="legend-container">
        <h4 class="legend-title">Legend</h4>

        <div class="legend-item">
            <i class="fa fa-map-pin legend-icon junction-icon"></i>
            <span>Junctions</span>
        </div>

        <div class="legend-item">
            <div class="legend-line boundary-line"></div>
            <span>Boundary</span>
        </div>

        <div class="legend-item">
            <div class="legend-icon gully-icon"></div>
            <span>Gully</span>
        </div>

        <div class="legend-item">
            <div class="legend-line drain-line"></div>
            <span>Filter Drains</span>
        </div>

        <div class="legend-item">
            <div class="legend-icon lamp-upgraded"></div>
            <span>Lighting Columns To Be Upgraded</span>
        </div>

        <div class="legend-item">
            <div class="legend-icon lamp-existing"></div>
            <span>Lighting Columns to Remain As Is</span>
        </div>

        <div class="legend-item">
            <div class="legend-icon marker-icon"></div>
            <span>Marker Posts - M20</span>
        </div>

        <style>
            .legend-container {
                position: fixed; 
                bottom: 50px; 
                left: 50px; 
                z-index: 1000;
                background: white;
                border: 2px solid grey;
                border-radius: 5px;
                padding: 10px;
                font-size: 12px;
                max-width: 250px;
            }

            .legend-title {
                margin: 0 0 5px 0;
                font-size: 14px;
            }

            .legend-item {
                display: flex;
                align-items: center;
                margin-bottom: 5px;
            }

            .legend-icon {
                width: 20px;
                height: 20px;
                margin-right: 5px;
                border: 1px solid black;
                border-radius: 50%;
            }

            .junction-icon {
                color: lightred;
                font-size: 18px;
                border: none;
            }

            .legend-line {
                width: 20px;
                height: 0;
                margin-right: 5px;
            }

            .boundary-line { border: 2px solid red; }
            .drain-line { border-bottom: 2px solid blue; }
            .gully-icon { background: yellow; }
            .lamp-upgraded { background: green; }
            .lamp-existing { background: orange; }
            .marker-icon { background: red; }
        </style>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    # Add the labels for Lighting Columns
    for idx, row in Lighting_Column.iterrows():
        if not row.geometry.is_empty and pd.notnull(row['Unique_Ass']):
            label_color = 'green' if row['ScheduledF'] == 'Yes' else 'orange'
            label = folium.DivIcon(
                html=f"""<div style="
                    color: {label_color};
                    font-size: 12px;
                    font-weight: bold;
                    position: absolute;
                    transform: translate(-50%, -100%);
                    z-index: 9999;">{row['Unique_Ass']}</div>"""
            )
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=label,
                icon_size=(0, 0)
            ).add_to(m)

    # Add the Marker Post labels
    for idx, row in MarkerPosts.iterrows():
        if not row.geometry.is_empty and pd.notnull(row['mVal']):
            label = folium.DivIcon(
                html=f"""<div style="
                    color: white;
                    font-size: 12px;
                    font-weight: bold;
                    transform: translate(-50%, -100%);
                    z-index: 9999;">{row['mVal']}</div>"""
            )
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=label,
                icon_size=(0, 0)
            ).add_to(m)

    # Add the Gully labels
    for idx, row in Gully.iterrows():
        if not row.geometry.is_empty and pd.notnull(row['Unique_Ass']):
            label = folium.DivIcon(
                html=f"""<div style="
                    color: black;
                    font-size: 10px;
                    font-weight: bold;
                    transform: translate(-50%, -100%);
                    z-index: 9999;">{row['Unique_Ass']}</div>"""
            )
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=label,
                icon_size=(0, 0)
            ).add_to(m)

    # Add the Filter Drains labels
    for idx, row in Filter_Drains.iterrows():
        if not row.geometry.is_empty and pd.notnull(row['Unique_Ass']):
            centroid = row.geometry.centroid
            label = folium.DivIcon(
                html=f"""<div style="
                    color: blue;
                    font-size: 12px;
                    font-weight: bold;
                    transform: translate(-50%, -100%);
                    z-index: 9999;">{row['Unique_Ass']}</div>"""
            )
            folium.Marker(
                location=[centroid.y, centroid.x],
                icon=label,
                icon_size=(0, 0)
            ).add_to(m)

    # Add a distance tool to the map. This will allow the user to measure distances between the different assets.
    MeasureControl(position="bottomleft", primary_length_unit="meters").add_to(m)
    folium.LayerControl().add_to(m)

    # Save the map and open it in the browser
    m.save("M20_Lighting_Columns_and_Drainage_Assets.html")
    import webbrowser
    webbrowser.open("M20_Lighting_Columns_and_Drainage_Assets.html")


    # This section will create a table showing the estimated savings per Junction as a result of the Upgraded Lighting Columns
    def create_savings_table(lighting_data: gpd.GeoDataFrame, top_n: int = 10) -> None:
        """Generates the Lighting Column Upgrade Projected Savings table."""
        # Savings calculation
        SAVINGS_PER_LAMP_PER_HOUR = 0.15  # Separate analysis indicates a 15 cent saving per hour of use
        HOURS_PER_DAY = 8 # Lamps are set to run for 8 hours per day
        DAYS_PER_YEAR = 365

        # Process data and calculate savings
        junction_counts = lighting_data.groupby('Junction').agg(
            Total_Lamps=('Unique_Ass', 'count'),
            Lamps_to_Change=('ScheduledF', lambda x: (x == 'Yes').sum())
        ).reset_index().sort_values('Lamps_to_Change', ascending=False)

        # Calculate annual savings
        junction_counts['Annual_Savings'] = (
                junction_counts['Lamps_to_Change'] *
                SAVINGS_PER_LAMP_PER_HOUR *
                HOURS_PER_DAY *
                DAYS_PER_YEAR
        )

        # Prepare table data
        table_data = junction_counts[['Junction', 'Lamps_to_Change', 'Annual_Savings']].head(top_n)
        table_data['Annual_Savings'] = table_data['Annual_Savings'].round(2).apply(lambda x: f'€{x:,.2f}')

        # Create figure with just the table
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.axis('off')  # Hide axes

        # Create the table
        table = plt.table(
            cellText=table_data.values,
            colLabels=['Junction', 'No. of Upgraded Lighting_Columns', 'Annual Savings'],
            colColours=['#f0f0f0', '#f0f0f0', '#f0f0f0'],
            cellLoc='center',
            loc='center',
            bbox=[0, 0, 1, 1]
        )

        # Style table
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)

        plt.show()


    # Generate the table
    create_savings_table(Lighting_Column)

    # Create a CSV file of the Lighting_Point Data
    pd.DataFrame(Lighting_Column.drop(columns='geometry')).to_csv(
        r'C:\Users\royco\OneDrive - Ulster University\Documents\GitHub\EGM722Project\lighting_column_data.csv',
        index=False
    )
    os.makedirs(r'C:\Users\royco\OneDrive - Ulster University\Documents\GitHub\EGM722Project', exist_ok=True)