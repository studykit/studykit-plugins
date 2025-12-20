# PointHolePlacementDefinition Object

Derived from: [HolePlacementDefinition](../HolePlacementDefinition/HolePlacementDefinition.md) Object

## Description

The PointHolePlacementDefinition object defines the placement of a hole feature using a work point.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PointHolePlacementDefinition/PointHolePlacementDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Direction](../PointHolePlacementDefinition/PointHolePlacementDefinition_Direction.md) | Property that indicates the entity that defines the hole axis direction. This can be a planar Face object or a WorkPlane object with which the axis of the hole is perpendicular, or an Edge or WorkAxis object with which the axis of the hole is parallel. |
| [Parent](../PointHolePlacementDefinition/PointHolePlacementDefinition_Parent.md) | Property that returns the parent PartFeature of the definition. This property returns Nothing in the case where the definition object is created using one of the Create methods on the HoleFeatures object. |
| [Point](../PointHolePlacementDefinition/PointHolePlacementDefinition_Point.md) | Property that indicates the point that defines the hole center. This can only be a WorkPoint. |
| [Type](../PointHolePlacementDefinition/PointHolePlacementDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HoleFeatures.CreatePointPlacementDefinition](../HoleFeatures/HoleFeatures_CreatePointPlacementDefinition.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |