# GeometricConstraints Object

## Description

The GeometricConstraints object provides access to all the geometric sketch constraints ( objects) in a sketch and provides methods to create additional geometric sketch constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddCoincident](../GeometricConstraints/GeometricConstraints_AddCoincident.md) | Method that creates a new coincident constraint between two entities. One of the input entities must be a sketch point. The other entity can be a point or any other type of sketch entity. |
| [AddCollinear](../GeometricConstraints/GeometricConstraints_AddCollinear.md) | Method that creates a new collinear constraint between the two input sketch entities. Valid objects for input include lines, ellipses, and elliptical arcs. Either the major or minor axis of an ellipse is used, depending on the value of the EllipseMajorAxis input argument. When an ellipse is used, the specified axis of the ellipse will become collinear to the other entity. This method will fail if the constraint overconstrains the sketch. |
| [AddConcentric](../GeometricConstraints/GeometricConstraints_AddConcentric.md) | Method that creates a new concentric constraint between the two input sketch entities. The two entities must be circles, arcs, ellipses, or elliptical arcs. This method will fail if the constraint overconstrains the sketch. |
| [AddEqualLength](../GeometricConstraints/GeometricConstraints_AddEqualLength.md) | Method that creates a new equal length constraint between the two input sketch lines. This method will fail if the constraint overconstrains the sketch. |
| [AddEqualRadius](../GeometricConstraints/GeometricConstraints_AddEqualRadius.md) | Method that creates a new equal radius constraint between the two input sketch entities. Valid input entities are circles and arcs. This method will fail if the constraint overconstrains the sketch. |
| [AddGround](../GeometricConstraints/GeometricConstraints_AddGround.md) | Method that creates a new ground constraint on the input sketch entity. This method will fail if the constraint overconstrains the sketch. |
| [AddHorizontal](../GeometricConstraints/GeometricConstraints_AddHorizontal.md) | Method that creates a new horizontal constraint on the input sketch entity. Valid input objects are lines, ellipses, and elliptical arcs. Either the major or minor axis of an ellipse is used depending on the value of the EllipseMajorAxis input argument. When an ellipse is used, the specified axis of the ellipse will become horizontal. This method will fail if the constraint overconstrains the sketch. |
| [AddHorizontalAlign](../GeometricConstraints/GeometricConstraints_AddHorizontalAlign.md) | Method that creates a new horizontal alignment constraint between two sketch points. This causes the two points to align along the same horizontal axis. This method will fail if the constraint overconstrains the sketch. |
| [AddMidpoint](../GeometricConstraints/GeometricConstraints_AddMidpoint.md) | Method that creates a new midpoint constraint between the point and line. This causes the input sketch point to be positioned at the midpoint of the input line. This method will fail if the constraint overconstrains the sketch. |
| [AddMidPointToArc](../GeometricConstraints/GeometricConstraints_AddMidPointToArc.md) | Creates a new midpoint constraint between the point and arc. |
| [AddParallel](../GeometricConstraints/GeometricConstraints_AddParallel.md) | Method that creates a new parallel constraint between the two input sketch entities. Valid objects for input include lines and ellipses. Either the major or minor axis of an ellipse is used depending on the values of UseEllipseMajorAxis input arguments. When an ellipse is used, the specified axis of the ellipse will become parallel to the other entity. This method will fail if the constraint overconstrains the sketch. |
| [AddPerpendicular](../GeometricConstraints/GeometricConstraints_AddPerpendicular.md) | Method that creates a new perpendicular constraint between the two input sketch entities. Valid objects for input include lines and ellipses. Either the major or minor axis of an ellipse is used depending on the value of EllipseMajorAxis input argument. When an ellipse is used, the specified axis of the ellipse will become perpendicular to the other entity. This method will fail if the constraint overconstrains the sketch. |
| [AddSmooth](../GeometricConstraints/GeometricConstraints_AddSmooth.md) | Method that creates a new smooth (G2-continuous) constraint. This method will fail if the constraint overconstrains the sketch. |
| [AddSymmetry](../GeometricConstraints/GeometricConstraints_AddSymmetry.md) | Method that creates a new symmetry constraint between the two input entities about the specified line. The two input entities must be of the same type. This method will fail if the constraint overconstrains the sketch. |
| [AddTangent](../GeometricConstraints/GeometricConstraints_AddTangent.md) | Method that creates a new tangent constraint. This method will fail if the constraint overconstrains the sketch. |
| [AddVertical](../GeometricConstraints/GeometricConstraints_AddVertical.md) | Method that creates a new vertical constraint on the input sketch entity. Valid input objects are lines and ellipses. Either the major or minor axis of an ellipse is used depending on the value of the UseEllipseMajorAxis input argument. When an ellipse is used, the specified axis of the ellipse will become vertical. This method will fail if the constraint overconstrains the sketch. |
| [AddVerticalAlign](../GeometricConstraints/GeometricConstraints_AddVerticalAlign.md) | Method that creates a new vertical alignment constraint between two sketch points. This causes the two points to align along the same vertical axis. This method will fail if the constraint overconstrains the sketch. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeometricConstraints/GeometricConstraints_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../GeometricConstraints/GeometricConstraints_Count.md) | Property that returns the number of items in the collection. |
| [Item](../GeometricConstraints/GeometricConstraints_Item.md) | Returns the specified geometric sketch constraint object from the collection. |
| [Type](../GeometricConstraints/GeometricConstraints_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.GeometricConstraints](../DrawingSketch/DrawingSketch_GeometricConstraints.md), [PlanarSketch.GeometricConstraints](../PlanarSketch/PlanarSketch_GeometricConstraints.md), [PlanarSketchProxy.GeometricConstraints](../PlanarSketchProxy/PlanarSketchProxy_GeometricConstraints.md), [Sketch.GeometricConstraints](../Sketch/Sketch_GeometricConstraints.md), [SketchBlockDefinition.GeometricConstraints](../SketchBlockDefinition/SketchBlockDefinition_GeometricConstraints.md), [SketchBlockDefinitionProxy.GeometricConstraints](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_GeometricConstraints.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sketch Spline](../../sample-programs/SketchSpline_Sample.md) | This sample demonstrates creating and manipulating a sketch spline. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |