import folium
import pandas
import json

volcano_data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])
name = list(volcano_data["NAME"])

# function to assign the color according to the elevation range
def color_map(elevation):
    colors = ["green", "orange", "red"]
    if elevation < 1000.0:
        return colors[0]
    elif elevation < 3000.0:
        return colors[1]
    else:
        return colors[2]

# map object
map = folium.Map(location=[lat[1], lon[1]], tiles = 'Mapbox Bright', zoom_start = 5)
fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    # popup object
    pop = folium.Popup(nm + " " + str(el) + " m", parse_html=True)
    # circle markers for each volcano
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                    radius=8,
                                    popup=pop ,
                                    fill=True,
                                    fill_color=color_map(el),
                                    fill_opacity = 0.8,
                                    color='grey'))


# adding the country demarcations using GeoJson data and add population based coloring
fgp = folium.FeatureGroup(name = "Population")
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000
                            else 'orange' if x['properties']['POP2005'] <= 20000000
                            else 'red' }
geojson_data = data=open('world.json', 'r', encoding='utf-8-sig').read()
fgp.add_child(folium.GeoJson(geojson_data, style_function=style_function))

map.add_child(fgv)
map.add_child(fgp)
map.save("map.html")
