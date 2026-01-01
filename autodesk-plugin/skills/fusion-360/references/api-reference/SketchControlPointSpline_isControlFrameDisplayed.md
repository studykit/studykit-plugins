# SketchControlPointSpline.isControlFrameDisplayed Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Gets and sets if the control frame of the curve is currently displayed. Using this property is useful to be able to determine if the controlPoints and controlFrameLines properties will return useful information or not and if the addControlPoint method will succeed or not.

## Remarks

There are cases where Fusion creates a control point spline but does not display the control frame. An example is when you create an offset of a spline.