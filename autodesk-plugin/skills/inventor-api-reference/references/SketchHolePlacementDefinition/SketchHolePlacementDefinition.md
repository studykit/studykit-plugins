# SketchHolePlacementDefinition Object

Derived from: [HolePlacementDefinition](../HolePlacementDefinition/HolePlacementDefinition.md) Object

## Description

The SketchHolePlacementDefinition object defines the placement of a hole feature using sketch points.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchHolePlacementDefinition/SketchHolePlacementDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [HoleCenterPoints](../SketchHolePlacementDefinition/SketchHolePlacementDefinition_HoleCenterPoints.md) | Gets and sets the set of sketch points that define the centers of the holes of this feature. |
| [Parent](../SketchHolePlacementDefinition/SketchHolePlacementDefinition_Parent.md) | Property that returns the parent PartFeature of the definition. This property returns Nothing in the case where the definition object is created using one of the Create methods on the HoleFeatures object. |
| [Type](../SketchHolePlacementDefinition/SketchHolePlacementDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HoleFeatures.CreateSketchPlacementDefinition](../HoleFeatures/HoleFeatures_CreateSketchPlacementDefinition.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |