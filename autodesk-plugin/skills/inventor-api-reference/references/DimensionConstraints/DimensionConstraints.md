# DimensionConstraints Object

## Description

The DimensionConstraints object provides access to all the dimension sketch constraints ( objects) in a sketch and provides methods to create additional dimension sketch constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddArcLength](../DimensionConstraints/DimensionConstraints_AddArcLength.md) | Method that creates a new arc length dimension on the input arc. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch. |
| [AddDiameter](../DimensionConstraints/DimensionConstraints_AddDiameter.md) | Method that creates a new diameter dimension constraint on the input circle or arc. |
| [AddEllipseRadius](../DimensionConstraints/DimensionConstraints_AddEllipseRadius.md) | Method that creates a new dimension constraint defining the major or minor radius of the ellipse. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch. |
| [AddOffset](../DimensionConstraints/DimensionConstraints_AddOffset.md) | Method that creates a new offset dimension constraint between two entities. |
| [AddOffsetSpline](../DimensionConstraints/DimensionConstraints_AddOffsetSpline.md) | Creates a new offsetSpline dimension constraint between offset spline and the original spline. |
| [AddRadius](../DimensionConstraints/DimensionConstraints_AddRadius.md) | Method that creates a new radius dimension constraint on the input circle or arc. |
| [AddTangentDistance](../DimensionConstraints/DimensionConstraints_AddTangentDistance.md) | Method that creates a new tangent distance dimension constraint between the two input entities. The input entities can consist of two circles or a line and a circle. Arcs can also be used in place of the circles. |
| [AddThreePointAngle](../DimensionConstraints/DimensionConstraints_AddThreePointAngle.md) | Method that creates a new angular dimension constraint between three points. |
| [AddTwoLineAngle](../DimensionConstraints/DimensionConstraints_AddTwoLineAngle.md) | Method that creates a new angular dimension constraint between two lines. |
| [AddTwoPointDistance](../DimensionConstraints/DimensionConstraints_AddTwoPointDistance.md) | Method that creates a new linear dimension constraint between two points. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DimensionConstraints/DimensionConstraints_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DimensionConstraints/DimensionConstraints_Count.md) | Property that returns the number of items in this collection. |
| [Item](../DimensionConstraints/DimensionConstraints_Item.md) | Returns the specified sketch dimension constraint object from the collection. |
| [Type](../DimensionConstraints/DimensionConstraints_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.DimensionConstraints](../DrawingSketch/DrawingSketch_DimensionConstraints.md), [PlanarSketch.DimensionConstraints](../PlanarSketch/PlanarSketch_DimensionConstraints.md), [PlanarSketchProxy.DimensionConstraints](../PlanarSketchProxy/PlanarSketchProxy_DimensionConstraints.md), [Sketch.DimensionConstraints](../Sketch/Sketch_DimensionConstraints.md), [SketchBlockDefinition.DimensionConstraints](../SketchBlockDefinition/SketchBlockDefinition_DimensionConstraints.md), [SketchBlockDefinitionProxy.DimensionConstraints](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_DimensionConstraints.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |