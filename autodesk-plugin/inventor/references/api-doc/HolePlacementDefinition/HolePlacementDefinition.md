# HolePlacementDefinition Object

## Description

The HolePlacementDefinition object is the base class that defines the placement method for hole features.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HolePlacementDefinition/HolePlacementDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../HolePlacementDefinition/HolePlacementDefinition_Parent.md) | Property that returns the parent PartFeature of the definition. This property returns Nothing in the case where the definition object is created using one of the Create methods on the HoleFeatures object. |
| [Type](../HolePlacementDefinition/HolePlacementDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HoleFeature.PlacementDefinition](../HoleFeature/HoleFeature_PlacementDefinition.md), [HoleFeatureProxy.PlacementDefinition](../HoleFeatureProxy/HoleFeatureProxy_PlacementDefinition.md)

## Derived Classes

[ConcentricHolePlacementDefinition](../ConcentricHolePlacementDefinition/ConcentricHolePlacementDefinition.md), [LinearHolePlacementDefinition](../LinearHolePlacementDefinition/LinearHolePlacementDefinition.md), [PointHolePlacementDefinition](../PointHolePlacementDefinition/PointHolePlacementDefinition.md), [SketchHolePlacementDefinition](../SketchHolePlacementDefinition/SketchHolePlacementDefinition.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |