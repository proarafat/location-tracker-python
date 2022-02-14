import folium

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('bangladesh_geojson_adm0_whole_bangladesh_outline.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[24.806, 89.3138],popup="this is were Mahasthangar is located  "))

map=folium.Map(location=[24.806,89.3138],zoom_start=5)

map.add_child(fg)
map.save("click.html")