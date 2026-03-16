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
#cyltrifoamDisplay = Show(cyltrifoam, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
#cyltrifoamDisplay.Representation = 'Surface'

# reset view to fit data
#renderView1.ResetCamera()

# show color bar/color legend
#cyltrifoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
#renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=cyltrifoam)

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]
slice1.SliceType.Origin = [6e-4,6e-4,6e-4]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'

# hide data in view
#Hide(cyltrifoam, renderView1)

# show color bar/color legend
#slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'alpha.water'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(2200, 1552)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0006000000284984708, 0.0006000000284984708, 0.0033424892359685625]
renderView1.CameraFocalPoint = [0.0006000000284984708, 0.0006000000284984708, 0.0006000000284984708]
renderView1.CameraParallelScale = 0.0010392305339021258

#import pdb; pdb.set_trace()

# save animation
SaveAnimation(filename=basedir+'/anim2d/qwerty.png', viewOrLayout=renderView1, ImageResolution=[1100, 776], FrameWindow=[0, 119])
#SaveAnimation(filename=basedir+'/anim2d/qwerty.avi', viewOrLayout=renderView1, ImageResolution=[1100, 776], FrameWindow=[0, 119])

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
renderView1.CameraPosition = [0.0006000000284984708, 0.0006000000284984708, 0.0033424892359685625]
renderView1.CameraFocalPoint = [0.0006000000284984708, 0.0006000000284984708, 0.0006000000284984708]
renderView1.CameraParallelScale = 0.0010392305339021258
