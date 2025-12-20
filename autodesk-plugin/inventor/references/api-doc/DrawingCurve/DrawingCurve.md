# DrawingCurve Object

## Description

The DrawingCurve object represents a curve within a drawing view that resulted from a model (including sketch entities).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCustomLineType](../DrawingCurve/DrawingCurve_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [SetCustomLineType](../DrawingCurve/DrawingCurve_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingCurve/DrawingCurve_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CenterPoint](../DrawingCurve/DrawingCurve_CenterPoint.md) | Property that returns the center point of the curve in sheet space. This property returns the center for arcs and circles and Nothing if the curve does not have a center. |
| [Color](../DrawingCurve/DrawingCurve_Color.md) | Gets and sets the color for the curve. |
| [CurveType](../DrawingCurve/DrawingCurve_CurveType.md) | Property that returns the type of the underlying curve geometry that this curve is defined by. |
| [EdgeType](../DrawingCurve/DrawingCurve_EdgeType.md) | Property that returns the edge type of this curve. Possible return values are kThreadEdge, kBendUpEdge, kBendDownEdge, kBendExtentEdge, kPunchDownEdge, kPunchUpEdge, kTangentEdge, kContourRollEdge, and kUnknownEdge. |
| [EndPoint](../DrawingCurve/DrawingCurve_EndPoint.md) | Property that returns the end point of the curve in sheet space. This property returns Nothing for circular curves. |
| [Evaluator2D](../DrawingCurve/DrawingCurve_Evaluator2D.md) | Property that returns the Curve2dEvaluator object for this curve in sheet space. |
| [Evaluator3D](../DrawingCurve/DrawingCurve_Evaluator3D.md) | Property that returns the CurveEvaluator object for this curve in 3d model view space. |
| [LineType](../DrawingCurve/DrawingCurve_LineType.md) | Gets and sets the line type override for the curve. |
| [LineWeight](../DrawingCurve/DrawingCurve_LineWeight.md) | Gets and sets the line weight override for the curve. |
| [MidPoint](../DrawingCurve/DrawingCurve_MidPoint.md) | Property that returns the mid point of the curve in sheet space. This property returns the mid point for linear curves and arcs. |
| [ModelGeometry](../DrawingCurve/DrawingCurve_ModelGeometry.md) | Property that returns the corresponding geometry from the model. This property returns Nothing in the case the model is not available. |
| [Parent](../DrawingCurve/DrawingCurve_Parent.md) | Property that returns the parent drawing view of the curve. |
| [ProjectedCurveType](../DrawingCurve/DrawingCurve_ProjectedCurveType.md) | Property that returns the curve type of the drawing curve projected onto the sheet. For instance, if a circular drawing curve shows up as a linear curve on the sheet, this property returns kLineSegmentCurve2d. |
| [Segments](../DrawingCurve/DrawingCurve_Segments.md) | Property that returns the collection of the selectable segments representing this curve. |
| [StartPoint](../DrawingCurve/DrawingCurve_StartPoint.md) | Property that returns the start point of the curve in sheet space. This property returns Nothing for circular curves. |
| [Type](../DrawingCurve/DrawingCurve_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendNote.BendEdge](../BendNote/BendNote_BendEdge.md), [DetailDrawingView.AuxiliaryOrientationEdge](../DetailDrawingView/DetailDrawingView_AuxiliaryOrientationEdge.md), [DrawingCurveSegment.Parent](../DrawingCurveSegment/DrawingCurveSegment_Parent.md), [DrawingCurvesEnumerator.Item](../DrawingCurvesEnumerator/DrawingCurvesEnumerator_Item.md), [DrawingView.AuxiliaryOrientationEdge](../DrawingView/DrawingView_AuxiliaryOrientationEdge.md), [SectionDrawingView.AuxiliaryOrientationEdge](../SectionDrawingView/SectionDrawingView_AuxiliaryOrientationEdge.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |