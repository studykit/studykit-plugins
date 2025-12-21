# SketchFixedSplines3D Object

## Description

The SketchFixedSplines3D object provides access to all the objects in a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchFixedSplines3D/SketchFixedSplines3D_Add.md) | Method that creates a fixed spline based on an input NURBS definition. |
| [AddByEdge](../SketchFixedSplines3D/SketchFixedSplines3D_AddByEdge.md) | Method that creates a fixed spline based on an input transient Edge object. This capability is useful because some edges are defined precisely using a procedural algorithm. Converting these to a NURBS curves results in an approximation of the procedural curve. The SketchFixedSpline3D object created with this method has the full accuracy of the procedural curve without any approximation. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchFixedSplines3D/SketchFixedSplines3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchFixedSplines3D/SketchFixedSplines3D_Count.md) | Property that specifies the number of items in the collection. |
| [Item](../SketchFixedSplines3D/SketchFixedSplines3D_Item.md) | Method that returns the specified SketchFixedSpline3D object from the collection. |
| [Type](../SketchFixedSplines3D/SketchFixedSplines3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.SketchFixedSplines3D](../Sketch3D/Sketch3D_SketchFixedSplines3D.md), [Sketch3DProxy.SketchFixedSplines3D](../Sketch3DProxy/Sketch3DProxy_SketchFixedSplines3D.md)

## Version

Introduced in version 9
