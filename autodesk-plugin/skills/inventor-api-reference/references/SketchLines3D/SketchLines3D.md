# SketchLines3D Object

## Description

The SketchLines3D object provides access to all of the objects in a sketch and provides methods to create additional sketch lines. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByTwoPoints](../SketchLines3D/SketchLines3D_AddByTwoPoints.md) | Method that creates a new sketch line based on the two input points. The new sketch line is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchLines3D/SketchLines3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchLines3D/SketchLines3D_Count.md) | Property that returns the number of items in the collection. |
| [Item](../SketchLines3D/SketchLines3D_Item.md) | Returns the specified SketchLine3D object from the collection. |
| [Type](../SketchLines3D/SketchLines3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.SketchLines3D](../Sketch3D/Sketch3D_SketchLines3D.md), [Sketch3DProxy.SketchLines3D](../Sketch3DProxy/Sketch3DProxy_SketchLines3D.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |