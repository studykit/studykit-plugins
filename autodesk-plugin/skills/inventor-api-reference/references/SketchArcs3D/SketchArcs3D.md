# SketchArcs3D Object

## Description

The SketchArcs3D object provides access to all the sketch arcs ( objects, including bends) in a 3D sketch and provides methods to create additional bends. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAsBend](../SketchArcs3D/SketchArcs3D_AddAsBend.md) | Method that creates a new bend feature based on the two input lines. |
| [AddByCenterStartEndPoint](../SketchArcs3D/SketchArcs3D_AddByCenterStartEndPoint.md) | Method that creates a new sketch arc defined by a center point and two points defining the start and end. Method that creates a new sketch arc defined by a center point and two points defining the start and end. |
| [AddByCenterStartSweepAngle](../SketchArcs3D/SketchArcs3D_AddByCenterStartSweepAngle.md) | Method that creates a new sketch arc using the input point and angles. |
| [AddByThreePoints](../SketchArcs3D/SketchArcs3D_AddByThreePoints.md) | Method that creates a new sketch arc that passes through the three input points. All the points must lie on the same plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchArcs3D/SketchArcs3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchArcs3D/SketchArcs3D_Count.md) | Property that returns the number of items in the collection. |
| [Item](../SketchArcs3D/SketchArcs3D_Item.md) | Returns the specified SketchArc3D object from the collection. |
| [Type](../SketchArcs3D/SketchArcs3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.SketchArcs3D](../Sketch3D/Sketch3D_SketchArcs3D.md), [Sketch3DProxy.SketchArcs3D](../Sketch3DProxy/Sketch3DProxy_SketchArcs3D.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |