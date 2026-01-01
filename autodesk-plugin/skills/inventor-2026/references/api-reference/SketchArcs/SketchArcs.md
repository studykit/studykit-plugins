# SketchArcs Object

## Description

The SketchArcs object provides access to all the objects in a sketch and provides methods to create additional sketch arcs. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByCenterStartEndPoint](../SketchArcs/SketchArcs_AddByCenterStartEndPoint.md) | Method that creates a new sketch arc defined by a center point and two points defining the start and end. The input points can be a combination of existing sketch points or Point2d objects. In the case where a sketch points is input, the arc will be attached to the sketch point. The sweep direction of the arc from the start to end point is determined by the CounterClockwise argument. The radius of the arc is determined by the start point. If the input for the start point is a sketch point, the arc will be tied to the sketch point. The second point, whether it is a sketch point or coordinate point defines the sweep of the arc. In the case where a sketch point is input and it is on the arc, the arc will be tied to the sketch point. |
| [AddByCenterStartSweepAngle](../SketchArcs/SketchArcs_AddByCenterStartSweepAngle.md) | Method that creates a new sketch arc using the input point and angles. |
| [AddByFillet](../SketchArcs/SketchArcs_AddByFillet.md) | Method that creates a new sketch arc as a fillet between two sketch entities. |
| [AddByThreePoints](../SketchArcs/SketchArcs_AddByThreePoints.md) | Method that creates a new sketch arc that passes through the three input points. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchArcs/SketchArcs_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchArcs/SketchArcs_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SketchArcs/SketchArcs_Item.md) | Returns the specified SketchArcobject from the collection. |
| [Type](../SketchArcs/SketchArcs_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.SketchArcs](../DrawingSketch/DrawingSketch_SketchArcs.md), [PlanarSketch.SketchArcs](../PlanarSketch/PlanarSketch_SketchArcs.md), [PlanarSketchProxy.SketchArcs](../PlanarSketchProxy/PlanarSketchProxy_SketchArcs.md), [Sketch.SketchArcs](../Sketch/Sketch_SketchArcs.md), [SketchBlockDefinition.SketchArcs](../SketchBlockDefinition/SketchBlockDefinition_SketchArcs.md), [SketchBlockDefinitionProxy.SketchArcs](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchArcs.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 5
