# MapPointCurve Object

## Description

The MapPointCurve object is used to define a set of mapping points between sections in a loft feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MapPointCurve/MapPointCurve_Delete.md) | Method that deletes this set of mapping points for a loft. |
| [GetPosition](../MapPointCurve/MapPointCurve_GetPosition.md) | Method that gets the position of the specified map point along the input entity. |
| [GetPositionPoint](../MapPointCurve/MapPointCurve_GetPositionPoint.md) | Method that returns the position of the specified map point in 3D space. |
| [SetPosition](../MapPointCurve/MapPointCurve_SetPosition.md) | Method that sets the position of the map point. The entity implicitly defines which section the point is for. The position of the map points is defined using a 3D coordinate point. If a map point already exists for the section the input entity is a member of, the current map point will be replaced. |
| [SetPositionUsingPoint](../MapPointCurve/MapPointCurve_SetPositionUsingPoint.md) | Method that sets the position of the map point using a 3D coordinate. The index corresponds with the section of the same index. If a map point already exists for the section the input entity is a member of, the current map point will be replaced. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MapPointCurve/MapPointCurve_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [PointCount](../MapPointCurve/MapPointCurve_PointCount.md) | Property that specifies the number of MapPoints in the set. |
| [Type](../MapPointCurve/MapPointCurve_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[MapPointCurves.AddMapCurve](../MapPointCurves/MapPointCurves_AddMapCurve.md), [MapPointCurves.Item](../MapPointCurves/MapPointCurves_Item.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |