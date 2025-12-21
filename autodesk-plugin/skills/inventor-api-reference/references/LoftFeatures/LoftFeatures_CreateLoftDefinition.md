# LoftFeatures.CreateLoftDefinition Method

Parent Object: [LoftFeatures](../LoftFeatures/LoftFeatures.md)

## Description

Method that creates a LoftDefinition object that defines the input definition for a loft feature.

## Remarks

The functionality provided by the resulting LoftDefinition object can also be used to define additional input data for creating the loft feature which includes the following: the boundary conditions for the starting and ending sections, a centerline or rails with any applicable boundary conditions, the mapping between the sections, an option to indicate whether the loft should be closed or not and an option to indicate whether tangent faces should be merged or not.

## Syntax

LoftFeatures.**CreateLoftDefinition**( ***Sections*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [LoftDefinition](../LoftDefinition/LoftDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Sections | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the sections for the loft. Valid objects for sections are Profile, Profile3D, EdgeLoop, EdgeCollection, SketchPoint, SketchPoint3D, WorkPoint and Vertex objects. If a point (SketchPoint, SketchPoint3D, WorkPoint or Vertex object) is used, it must be either the first section or the last section and there must be at least one other intermediate section which is not a point. If an EdgeCollection object is used it may contain either a single edge or a set of tangentially connected edges. The order of the sections within the ObjectCollection defines the fit order of the loft through the sections. The sections must be either all open or all closed; you cannot mix open and closed sections. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation or kSurfaceOperation. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |