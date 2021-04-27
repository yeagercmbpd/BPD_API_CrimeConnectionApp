config={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "data_2"
          ],
          "id": "34fnsmyev",
          "name": [],
          "type": None,
          "value": None,
          "enlarged": False,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "kknyztc",
          "type": "arc",
          "config": {
            "dataId": "data_2",
            "label": "Connect",
            "color": [
              82,
              163,
              83
            ],
            "columns": {
              "lat0": "LatitudeStart",
              "lng0": "LongitudeStart",
              "lat1": "LatitudeFinish",
              "lng1": "LongitudeFinish"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "thickness": 5.7,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "sizeRange": [
                0,
                10
              ],
              "targetColor": [
                227,
                26,
                26
              ]
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "data_2": [
              {
                "name": "Unnamed: 0",
                "format": None
              },
              {
                "name": "index",
                "format": None
              },
              {
                "name": "antecedentsEach",
                "format": None
              },
              {
                "name": "consequentsEach",
                "format": None
              },
              {
                "name": "City_x",
                "format": None
              },
              {
                "name": "confidence",
                "format": None
              },
              {
                "name": "lift",
                "format": None
              },
              {
                "name": "support",
                "format": None
              },
            ],
            "unnamed": [
              {
                "name": "Unnamed: 0",
                "format": None
              },
              {
                "name": "index",
                "format": None
              },
              {
                "name": "antecedentsEach",
                "format": None
              },
              {
                "name": "consequentsEach",
                "format": None
              },
              {
                "name": "City_x",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": -2.8163265306122423,
      "dragRotate": True,
      "latitude": 39.32658881983414,
      "longitude": -76.61325852525803,
      "pitch": 52.56028031282507,
      "zoom": 11.498463449319415,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
