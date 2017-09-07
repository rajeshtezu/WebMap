# WebMap

A world web map using folium and pandas. Python script generates an HTML file which is created using html, css, javascript.
Web Map contains following:  
* A base world map
* On top of base world map a layer of markers, which indicates volcanoes in USA. Green color represents elevation less than 1000 m,
Orange color represents elevation between 1000 m and 3000, and Red for elevation more than 3000 m.
* On top of that there is a Population layer which is also color coded. Green with less population than Orange than Red.

### Clone the project
```
git clone https://github.com/rajeshtezu90/WebMap.git
```
### install requirements
```
pip3 install -r requirements.txt
```
### Running the code
```
python3 webmap.py
```
