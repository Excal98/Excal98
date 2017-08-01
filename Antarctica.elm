myShapes = [background, landscape]

background = group [
  rect 300 128
    |> filled sky
  ]

landscape = group [
  mountain
    |> filled mountain_grey
    |> move (-56, -65)
  ,mountain
    |> filled mountain_grey
    |> move (36, -70)
    |> scale 1.15
  ,snowcap
    |> filled snow
    |> move (-56, 21.5)
  ,snowcap
    |> filled snow
    |> move (39,30.5)
    |> scale 1.15
    |> mirrorX
    |> rotate (degrees 5)
  ,mountain_cracks
    |> filled mountain_grey_dark
  ,dunes 
    |> filled snow
    |> move (-34, -62)
  ,dunes 
    |> filled snow
    |> move (27, -65)
  ,dunes
    |> filled snow
    |> move (50, -68)
  ,dunes
    |> filled snow
    |> move (-74, -69)
  ,shadow
    |> filled snow_shade
    |> move (-34, -62)
  ,shadow
    |> filled snow_shade
    |> move (27, -65)
  ,shadow
    |> filled snow_shade
    |> move (50, -68)
  ]

snowcap = polygon [(-9, 0),(-6, -1),(-4, 2),(-2, -1),(1, 1),(4, -3),(6, -1),(9, 2),(12, 0),(0, 21)]
mountain = polygon [(-56, 0),(0, 105),(76,0)]
mountain_cracks = polygon [(0, 0),(-3, -6),(-1, -10),(-2, -16),(0, -20),(2, -17),(1, -12),(3, -7)]
dunes = curve (-50, 0) [Pull(20, 50) (60, 0)]
shadow = curve (30, 0) [Pull(20, 40) (60, 0)]

mountain_grey_dark = rgb 168 168 173
mountain_grey = rgb 187 187 193
snow = rgb 250 250 255
snow_shade = rgb 232 232 249
sky = rgb 135 206 235

