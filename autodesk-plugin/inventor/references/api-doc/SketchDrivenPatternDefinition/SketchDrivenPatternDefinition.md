# SketchDrivenPatternDefinition Object

## Description

Part Sketch Driven Pattern Feature Definition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_Copy.md) | Method that returns a copy of the SketchDrivenPatternDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. |
| [AffectedOccurrences](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_AffectedOccurrences.md) | Read-write property that gets and sets the collection of occurrences that should participate in this feature. If this property is not set, all possible occurrences will participate. This property applies only to features in an assembly. |
| [Application](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [BasePoint](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_BasePoint.md) | Read-write property that gets and sets the geometry that defines the base point. When set this property, it can be a SketchPoint, SketchPoint3D, WorkPoint, GeometryIntent that indicates a point on geometry. If a GeometryIntent is provided, you can specify the mid-point of sketch line, start/end/mid-point of a linear edge, the center of a circular/elliptical edge, planar face center, the start/mid/end point of the axis of a cylindrical/conical face, or the center of torus/spherical face. |
| [ComputeType](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_ComputeType.md) | Read-write property that indicates the method of solution for the pattern. |
| [Operation](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_Operation.md) | Gets and sets the operation type. Valid values are kNewBodyOperation and kJoinOperation. |
| [ParentFeatures](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_ParentFeatures.md) | Read-write property that gets and sets the parent features of the pattern. The ObjectCollection returned by this property is a “tear off” and does not affect the pattern if its contents are modified. To change the which features are the parents of the pattern you need to use this property to set the parent features by providing an ObjectCollection that contains the desired set of parent features. |
| [PatternOfBody](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_PatternOfBody.md) | Read-only property that gets whether this pattern resulted from patterning the Surface Body. |
| [ReferenceFaces](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_ReferenceFaces.md) | Read-write property that gets and sets FaceCollection object to specify the reference faces. |
| [Sketch](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_Sketch.md) | Read-write property that gets and sets PlanarSketch or Sketch3D object that contains the sketch points to locate the pattern occurrences. |
| [Type](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[SketchDrivenPatternDefinition.Copy](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_Copy.md), [SketchDrivenPatternFeature.Definition](../SketchDrivenPatternFeature/SketchDrivenPatternFeature_Definition.md), [SketchDrivenPatternFeatureProxy.Definition](../SketchDrivenPatternFeatureProxy/SketchDrivenPatternFeatureProxy_Definition.md), [SketchDrivenPatternFeatures.CreateDefinition](../SketchDrivenPatternFeatures/SketchDrivenPatternFeatures_CreateDefinition.md)

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |