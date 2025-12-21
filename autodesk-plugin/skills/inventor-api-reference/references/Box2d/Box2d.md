# Box2d Object

## Description

The Box2d object is a mathematical utility object that represents a rectangle whose edges are always parallel to the x-y axes. A common use of the Box2d object is as a means of passing the range box information of a 2d entity and interacting with that range box.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Contains](../Box2d/Box2d_Contains.md) | Determines whether the specified point is contained within this Box. |
| [Copy](../Box2d/Box2d_Copy.md) | Creates a copy of this Box2d object. The result is entirely independent and can be edited without affecting the original Box2d object. |
| [Expand](../Box2d/Box2d_Expand.md) | Expands the Box on all sides by the specified distance. |
| [Extend](../Box2d/Box2d_Extend.md) | Extends the Box to include the specified point. |
| [GetBoxData](../Box2d/Box2d_GetBoxData.md) | Get the data defining this Box. |
| [IsDisjoint](../Box2d/Box2d_IsDisjoint.md) | Determines whether this Box intersects the specified Box. A return value of True indicates that the box do not intersect. |
| [PutBoxData](../Box2d/Box2d_PutBoxData.md) | Method that sets the data defining this Box. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [MaxPoint](../Box2d/Box2d_MaxPoint.md) | Property that gets and sets the maximum corner of the box. |
| [MinPoint](../Box2d/Box2d_MinPoint.md) | Property that gets and sets the minimum corner of the box. |

## Accessed From

[BendNote.RangeBox](../BendNote/BendNote_RangeBox.md), [Border.RangeBox](../Border/Border_RangeBox.md), [Box2d.Copy](../Box2d/Box2d_Copy.md), [ChamferNote.RangeBox](../ChamferNote/ChamferNote_RangeBox.md), [Curve2dEvaluator.RangeBox](../Curve2dEvaluator/Curve2dEvaluator_RangeBox.md), [CustomTable.RangeBox](../CustomTable/CustomTable_RangeBox.md), [DefaultBorder.RangeBox](../DefaultBorder/DefaultBorder_RangeBox.md), [DimensionText.RangeBox](../DimensionText/DimensionText_RangeBox.md), [DrawingNote.RangeBox](../DrawingNote/DrawingNote_RangeBox.md), [DrawingViewHatchArea.RangeBox](../DrawingViewHatchArea/DrawingViewHatchArea_RangeBox.md), [DrawingViewHatchRegion.RangeBox](../DrawingViewHatchRegion/DrawingViewHatchRegion_RangeBox.md), [DrawingViewLabel.RangeBox](../DrawingViewLabel/DrawingViewLabel_RangeBox.md), [GeneralNote.RangeBox](../GeneralNote/GeneralNote_RangeBox.md), [HoleTable.RangeBox](../HoleTable/HoleTable_RangeBox.md), [HoleTag.RangeBox](../HoleTag/HoleTag_RangeBox.md), [ImportedDWGComponent.Crop](../ImportedDWGComponent/ImportedDWGComponent_Crop.md), [ImportedDWGComponentProxy.Crop](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_Crop.md), [LeaderNote.RangeBox](../LeaderNote/LeaderNote_RangeBox.md), [PartsList.RangeBox](../PartsList/PartsList_RangeBox.md), [PunchNote.RangeBox](../PunchNote/PunchNote_RangeBox.md), [RevisionCloud.RangeBox](../RevisionCloud/RevisionCloud_RangeBox.md), [RevisionTable.RangeBox](../RevisionTable/RevisionTable_RangeBox.md), [SketchArc.RangeBox](../SketchArc/SketchArc_RangeBox.md), [SketchArcProxy.RangeBox](../SketchArcProxy/SketchArcProxy_RangeBox.md), [SketchCircle.RangeBox](../SketchCircle/SketchCircle_RangeBox.md), [SketchCircleProxy.RangeBox](../SketchCircleProxy/SketchCircleProxy_RangeBox.md), [SketchCircularPattern.RangeBox](../SketchCircularPattern/SketchCircularPattern_RangeBox.md), [SketchControlPointSpline.RangeBox](../SketchControlPointSpline/SketchControlPointSpline_RangeBox.md), [SketchControlPointSplineProxy.RangeBox](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_RangeBox.md), [SketchEllipse.RangeBox](../SketchEllipse/SketchEllipse_RangeBox.md), [SketchEllipseProxy.RangeBox](../SketchEllipseProxy/SketchEllipseProxy_RangeBox.md), [SketchEllipticalArc.RangeBox](../SketchEllipticalArc/SketchEllipticalArc_RangeBox.md), [SketchEllipticalArcProxy.RangeBox](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_RangeBox.md), [SketchEntity.RangeBox](../SketchEntity/SketchEntity_RangeBox.md), [SketchEquationCurve.RangeBox](../SketchEquationCurve/SketchEquationCurve_RangeBox.md), [SketchEquationCurveProxy.RangeBox](../SketchEquationCurveProxy/SketchEquationCurveProxy_RangeBox.md), [SketchFixedSpline.RangeBox](../SketchFixedSpline/SketchFixedSpline_RangeBox.md), [SketchFixedSplineProxy.RangeBox](../SketchFixedSplineProxy/SketchFixedSplineProxy_RangeBox.md), [SketchLine.RangeBox](../SketchLine/SketchLine_RangeBox.md), [SketchLineProxy.RangeBox](../SketchLineProxy/SketchLineProxy_RangeBox.md), [SketchOffsetSpline.RangeBox](../SketchOffsetSpline/SketchOffsetSpline_RangeBox.md), [SketchOffsetSplineProxy.RangeBox](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_RangeBox.md), [SketchPoint.RangeBox](../SketchPoint/SketchPoint_RangeBox.md), [SketchPointProxy.RangeBox](../SketchPointProxy/SketchPointProxy_RangeBox.md), [SketchRectangularPattern.RangeBox](../SketchRectangularPattern/SketchRectangularPattern_RangeBox.md), [SketchSpline.RangeBox](../SketchSpline/SketchSpline_RangeBox.md), [SketchSplineHandle.RangeBox](../SketchSplineHandle/SketchSplineHandle_RangeBox.md), [SketchSplineHandleProxy.RangeBox](../SketchSplineHandleProxy/SketchSplineHandleProxy_RangeBox.md), [SketchSplineProxy.RangeBox](../SketchSplineProxy/SketchSplineProxy_RangeBox.md), [SurfaceEvaluator.ParamRangeRect](../SurfaceEvaluator/SurfaceEvaluator_ParamRangeRect.md), [TextBox.RangeBox](../TextBox/TextBox_RangeBox.md), [TextBoxProxy.RangeBox](../TextBoxProxy/TextBoxProxy_RangeBox.md), [TitleBlock.RangeBox](../TitleBlock/TitleBlock_RangeBox.md), [TransientGeometry.CreateBox2d](../TransientGeometry/TransientGeometry_CreateBox2d.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |