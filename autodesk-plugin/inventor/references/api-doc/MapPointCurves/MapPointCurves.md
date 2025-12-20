# MapPointCurves Object

## Description

The MapPointCurves object represents a collection of objects, used to define mapping points between sections in a loft feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddMapCurve](../MapPointCurves/MapPointCurves_AddMapCurve.md) | Method that creates a new MapPointCurve. This method is only valid for MapPointCurves objects that were created using the LoftFeatures.CreateMapCurves. A error will occur if you use this method for a MapPointCurves object obtained from an existing LoftFeature object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MapPointCurves/MapPointCurves_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../MapPointCurves/MapPointCurves_Count.md) | Property that returns the number of MapPointCurve objects in the collection. |
| [Item](../MapPointCurves/MapPointCurves_Item.md) | Method that returns the specified MapPointCurve object from the collection. |
| [Type](../MapPointCurves/MapPointCurves_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[LoftDefinition.MapPointCurves](../LoftDefinition/LoftDefinition_MapPointCurves.md), [LoftFeatures.CreateMapCurves](../LoftFeatures/LoftFeatures_CreateMapCurves.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |