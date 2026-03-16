# trace generated using paraview version 5.13.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get script's path https://stackoverflow.com/a/9350788
import os
basedir=os.path.dirname(os.path.realpath(__file__))
# create a new 'Open FOAM Reader'
cyltrifoam = OpenFOAMReader(registrationName='qwerty.foam', FileName=basedir+'/qwerty.foam')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
cyltrifoamDisplay = Show(cyltrifoam, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cyltrifoamDisplay.Representation = 'Surface'

# reset view to fit data
#renderView1.ResetCamera(False, 0.9)

# show color bar/color legend
cyltrifoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get color transfer function/color map for 'alphawater'
alphawaterLUT = GetColorTransferFunction('alphawater')

# get opacity transfer function/opacity map for 'alphawater'
alphawaterPWF = GetOpacityTransferFunction('alphawater')

# get 2D transfer function for 'p'
#pTF2D = GetTransferFunction2D('p')

# Properties modified on renderView1
renderView1.CenterOfRotation = [0.0005999999848427251, 0.0005999999848427251, 0.0005999999993946403]
renderView1.CameraPosition = [0.001576778975710421, 0.0012048896296690957, 0.001018934266735576]
renderView1.CameraFocalPoint = [0.0005999999848427251, 0.0005999999848427251, 0.0005999999993946403]
renderView1.CameraViewUp = [-0.20517048664203427, -0.3113275099484762, 0.9278902160063724]
renderView1.CameraViewAngle = 33.18385650224215
renderView1.CameraParallelScale = 0.0003193512187499912

#Load a camera configuration
renderView1.CenterOfRotation = [0.0005999999848427251, 0.0005999999848427251, 0.0005999999993946403]
renderView1.CameraPosition = [0.001576778975710421, 0.0012048896296690957, 0.001018934266735576]
renderView1.CameraFocalPoint = [0.0005999999848427251, 0.0005999999848427251, 0.0005999999993946403]
renderView1.CameraViewUp = [-0.20517048664203427, -0.3113275099484762, 0.9278902160063724]
renderView1.CameraViewAngle = 33.18385650224215
renderView1.CameraParallelScale = 0.0003193512187499912

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# split cell
layout1.SplitVertical(2, 0.5)

# split cell
layout1.SplitVertical(6, 0.5)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
#renderView2.AxesGrid = 'Grid Axes 3D Actor'
#renderView2.StereoType = 'Crystal Eyes'
#renderView2.CameraFocalDisk = 1.0
#renderView2.LegendGrid = 'Legend Grid Actor'
#renderView2.PolarGrid = 'Polar Grid Actor'

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=5)

# resize frame
layout1.SetSplitFraction(2, 0.333333333333333333333333333)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
#renderView3.AxesGrid = 'Grid Axes 3D Actor'
#renderView3.StereoType = 'Crystal Eyes'
#renderView3.CameraFocalDisk = 1.0
#renderView3.LegendGrid = 'Legend Grid Actor'
#renderView3.PolarGrid = 'Polar Grid Actor'

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView3, layout=layout1, hint=13)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
#renderView4.AxesGrid = 'Grid Axes 3D Actor'
#renderView4.StereoType = 'Crystal Eyes'
#renderView4.CameraFocalDisk = 1.0
#renderView4.LegendGrid = 'Legend Grid Actor'
#renderView4.PolarGrid = 'Polar Grid Actor'

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView4, layout=layout1, hint=14)

# set active view
SetActiveView(renderView2)

# Properties modified on renderView2
renderView2.CenterOfRotation = [0.0003000000142492354, 0.0006000000284984708, 0.0006000000284984708]
renderView2.CameraPosition = [0.0037758483531908694, 0.0006000000284984708, 0.0004983924999217112]
renderView2.CameraFocalPoint = [0.0003000000142492354, 0.0006000000284984708, 0.0006000000284984708]
renderView2.CameraViewUp = [0.029219958080419817, 0.0, 0.9995730058628928]
renderView2.CameraViewAngle = 23.410852713178294
renderView2.CameraParallelScale = 0.0009000000427477062

#Load a camera configuration
renderView2.CenterOfRotation = [0.0003000000142492354, 0.0006000000284984708, 0.0006000000284984708]
renderView2.CameraPosition = [0.0037758483531908694, 0.0006000000284984708, 0.0004983924999217112]
renderView2.CameraFocalPoint = [0.0003000000142492354, 0.0006000000284984708, 0.0006000000284984708]
renderView2.CameraViewUp = [0.029219958080419817, 0.0, 0.9995730058628928]
renderView2.CameraViewAngle = 23.410852713178294
renderView2.CameraParallelScale = 0.0009000000427477062

# set active view
SetActiveView(renderView3)

# set active view
SetActiveView(renderView2)

# Properties modified on renderView2
renderView2.CenterOfRotation = [0.0006000000284984708, 0.0003000000142492354, 0.0006000000284984708]
renderView2.CameraPosition = [0.0006000000284984708, 0.003777333154054335, 0.0006000000284984708]
renderView2.CameraFocalPoint = [0.0006000000284984708, 0.0003000000142492354, 0.0006000000284984708]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraViewAngle = 23.67601246105919

#Load a camera configuration
renderView2.CenterOfRotation = [0.0006000000284984708, 0.0003000000142492354, 0.0006000000284984708]
renderView2.CameraPosition = [0.0006000000284984708, 0.003777333154054335, 0.0006000000284984708]
renderView2.CameraFocalPoint = [0.0006000000284984708, 0.0003000000142492354, 0.0006000000284984708]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraViewAngle = 23.67601246105919

# set active view
SetActiveView(renderView4)

# Properties modified on renderView4
renderView4.CenterOfRotation = [0.0006000000284984708, 0.0006000000284984708, 0.0003000000142492354]
renderView4.CameraPosition = [0.0006000000284984708, 0.0006000000284984708, 0.003777333154054335]
renderView4.CameraFocalPoint = [0.0006000000284984708, 0.0006000000284984708, 0.0003000000142492354]
renderView4.CameraViewAngle = 23.360655737704917
renderView4.CameraParallelScale = 0.0009000000427477062

#Load a camera configuration
renderView4.CenterOfRotation = [0.0006000000284984708, 0.0006000000284984708, 0.0003000000142492354]
renderView4.CameraPosition = [0.0006000000284984708, 0.0006000000284984708, 0.003777333154054335]
renderView4.CameraFocalPoint = [0.0006000000284984708, 0.0006000000284984708, 0.0003000000142492354]
renderView4.CameraViewAngle = 23.360655737704917
renderView4.CameraParallelScale = 0.0009000000427477062

# set active view
SetActiveView(renderView2)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=cyltrifoam)

# toggle interactive widget visibility (only when running from the GUI)
#HideInteractiveWidgets(proxy=clip1.ClipType)

# show data in view
clip1Display = Show(clip1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# reset view to fit data
#renderView2.ResetCamera(False, 0.9)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView3)

# set active source
SetActiveSource(cyltrifoam)

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=cyltrifoam)

# toggle interactive widget visibility (only when running from the GUI)
#HideInteractiveWidgets(proxy=clip2.ClipType)

# Properties modified on clip2.ClipType
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'

# reset view to fit data
#renderView3.ResetCamera(False, 0.9)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView3, True)

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# set active view
SetActiveView(renderView4)

# set active source
SetActiveSource(cyltrifoam)

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=cyltrifoam)

# toggle interactive widget visibility (only when running from the GUI)
#HideInteractiveWidgets(proxy=clip3.ClipType)

# Properties modified on clip3.ClipType
clip3.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip3Display = Show(clip3, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'

# reset view to fit data
#renderView4.ResetCamera(False, 0.9)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView4, True)

# update the view to ensure updated data information
renderView3.Update()

# update the view to ensure updated data information
renderView4.Update()

# set active view
SetActiveView(renderView2)

# Properties modified on renderView2
renderView2.CameraPosition = [0.0037758483531908694, 0.0006000000284984708, 0.0004983924999217112]
renderView2.CameraViewUp = [0.029219958080419817, 0.0, 0.9995730058628928]
renderView2.CameraViewAngle = 23.410852713178294

#Load a camera configuration
renderView2.CameraPosition = [0.0037758483531908694, 0.0006000000284984708, 0.0004983924999217112]
renderView2.CameraViewUp = [0.029219958080419817, 0.0, 0.9995730058628928]
renderView2.CameraViewAngle = 23.410852713178294

# set active view
SetActiveView(renderView3)

# set active view
SetActiveView(renderView4)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView3)

# Properties modified on renderView3
renderView3.CameraPosition = [0.0006000000284984708, 0.003777333154054335, 0.0006000000284984708]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraViewAngle = 23.67601246105919

#Load a camera configuration
renderView3.CameraPosition = [0.0006000000284984708, 0.003777333154054335, 0.0006000000284984708]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraViewAngle = 23.67601246105919

# set active view
SetActiveView(renderView4)

# Properties modified on renderView4
renderView4.CameraViewAngle = 23.360655737704917

#Load a camera configuration
renderView4.CameraViewAngle = 23.360655737704917

# set active source
SetActiveSource(cyltrifoam)

# create a new 'Iso Volume'
isoVolume1 = IsoVolume(registrationName='IsoVolume1', Input=cyltrifoam)

# Properties modified on isoVolume1
isoVolume1.InputScalars = ['POINTS', 'alpha.water']
isoVolume1.ThresholdRange = [0.75, 2.0]

# show data in view
isoVolume1Display = Show(isoVolume1, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
isoVolume1Display.Representation = 'Surface'

# show color bar/color legend
isoVolume1Display.SetScalarBarVisibility(renderView4, True)

# update the view to ensure updated data information
renderView4.Update()

# get 2D transfer function for 'alphawater'
#alphawaterTF2D = GetTransferFunction2D('alphawater')

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(isoVolume1)

# show data in view
isoVolume1Display_1 = Show(isoVolume1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
isoVolume1Display_1.Representation = 'Surface'

# show color bar/color legend
isoVolume1Display_1.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(cyltrifoam, renderView1)

# set active view
SetActiveView(renderView4)

# hide data in view
Hide(isoVolume1, renderView4)

# set active view
SetActiveView(renderView1)

# rescale color and/or opacity maps used to exactly fit the current data range
isoVolume1Display_1.RescaleTransferFunctionToDataRange(False, True)

ColorBy(isoVolume1Display_1, ('POINTS', 'alpha.water'))

# Properties modified on isoVolume1
isoVolume1.ThresholdRange = [0.01, 2.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView4.Update()

# Rescale transfer function
alphawaterLUT.RescaleTransferFunction(0.009999984875321388, 1.0)

# Rescale transfer function
alphawaterPWF.RescaleTransferFunction(0.009999984875321388, 1.0)

# Properties modified on isoVolume1
isoVolume1.ThresholdRange = [0.5, 2.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView4.Update()

# Properties modified on isoVolume1
isoVolume1.ThresholdRange = [0.75, 2.0]

HideScalarBarIfNotNeeded(pLUT, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView4.Update()

# rescale color and/or opacity maps used to exactly fit the current data range
isoVolume1Display_1.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
alphawaterLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
alphawaterPWF.RescaleTransferFunction(0.0, 1.0)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(clip1)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView2, True)

# set active view
SetActiveView(renderView3)

# set active source
SetActiveSource(clip2)

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView3)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView3, True)

# set active view
SetActiveView(renderView4)

# set active source
SetActiveSource(clip3)

# set scalar coloring
ColorBy(clip3Display, ('POINTS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView4)

# rescale color and/or opacity maps used to include current data range
clip3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView4, True)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2200, 1552)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.002030102105372118, 0.0014856189138330146, 0.0012133616602085042]
renderView1.CameraFocalPoint = [0.0006, 0.0006, 0.0006]
renderView1.CameraViewUp = [-0.20517048664203427, -0.3113275099484762, 0.9278902160063724]
renderView1.CameraViewAngle = 33.18385650224215
renderView1.CameraParallelScale = 0.0003193512187499912

# current camera placement for renderView2
renderView2.CameraPosition = [0.003, 0.0006, 0.0006]
renderView2.CameraFocalPoint = [0.0006, 0.0006, 0.0006]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraViewAngle = 30.0
renderView2.CameraParallelScale = 0.0009

# current camera placement for renderView3
renderView3.CameraPosition = [0.0006, 0.003, 0.0006]
renderView3.CameraFocalPoint = [0.0006, 0.0006, 0.0006]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraViewAngle = 30.0 
renderView3.CameraParallelScale = 0.0009

# current camera placement for renderView4
renderView4.CameraPosition = [0.0006, 0.0006, 0.003]
renderView4.CameraFocalPoint = [0.0006, 0.0006, 0.0006]
renderView4.CameraViewAngle = 30.0 
renderView4.CameraParallelScale = 0.0009

# save animation
SaveAnimation(filename=basedir+'/anim3d/qwerty.png', viewOrLayout=layout1, ImageResolution=[2200, 1552], FrameWindow=[0, 119])

##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
