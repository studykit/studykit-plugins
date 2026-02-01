# DrawingCurveSegment Object

## Description

The DrawingCurveSegment object represents a single segment of a drawing curve.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingCurveSegment/DrawingCurveSegment_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EndPoint](../DrawingCurveSegment/DrawingCurveSegment_EndPoint.md) | Property that returns the end point of the curve segment in sheet space. This property returns Nothing for circular segments. |
| [Geometry](../DrawingCurveSegment/DrawingCurveSegment_Geometry.md) | Read-only property that returns a 2d geometry object that represents this drawing curve segment in sheet space. The true drawing curve is 3d geometry and this is a flattened 2d version. As a result the geometry type can be different. For example a 3d circle can flatten to a 2d ellipse or a line if the circle is viewed completely on edge. There isn’t any expected correlation between the parameterization of this curve and the original 3d curve. |
| [GeometryType](../DrawingCurveSegment/DrawingCurveSegment_GeometryType.md) | Read-only property that returns the type of the geometry object that will be returned by the Geometry property. |
| [HiddenLine](../DrawingCurveSegment/DrawingCurveSegment_HiddenLine.md) | Property that returns whether this segment represents the hidden portion of a line. This is only applicable for drawing views with hidden lines and always returns False otherwise. |
| [Layer](../DrawingCurveSegment/DrawingCurveSegment_Layer.md) | Gets and sets the layer associated with this object. |
| [Parent](../DrawingCurveSegment/DrawingCurveSegment_Parent.md) | Property that returns the parent drawing curve. |
| [StartPoint](../DrawingCurveSegment/DrawingCurveSegment_StartPoint.md) | Property that returns the start point of the curve segment in sheet space. This property returns Nothing for circular segments. |
| [Type](../DrawingCurveSegment/DrawingCurveSegment_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../DrawingCurveSegment/DrawingCurveSegment_Visible.md) | Gets and sets whether this object is graphically visible. |

## Accessed From

[DrawingCurveSegments.Item](../DrawingCurveSegments/DrawingCurveSegments_Item.md)

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
