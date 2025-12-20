# PathEntity Object

## Description

The PathEntity object represents a curve within a path.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../PathEntity/PathEntity_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PathEntity/PathEntity_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Curve](../PathEntity/PathEntity_Curve.md) | Property that returns the geometry of the entity. The geometry is returned such that the entities are connected in a head-to-tail fashion. |
| [CurveType](../PathEntity/PathEntity_CurveType.md) | Property that returns the type of the curve referenced by the path entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [OpposedToSketchEntity](../PathEntity/PathEntity_OpposedToSketchEntity.md) | Property that returns a Boolean indicating if the parametric flow of the path entity is in the same direction as the sketch entity it was derived from. |
| [Parent](../PathEntity/PathEntity_Parent.md) | Property that returns the parent Path of the entity. |
| [SketchEntity](../PathEntity/PathEntity_SketchEntity.md) | Property that gets the sketch entity (2D or 3D) this entity was derived from. |
| [Type](../PathEntity/PathEntity_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Path.Item](../Path/Path_Item.md), [PathEntityProxy.NativeObject](../PathEntityProxy/PathEntityProxy_NativeObject.md), [PathProxy.Item](../PathProxy/PathProxy_Item.md)

## Derived Classes

[PathEntityProxy](../PathEntityProxy/PathEntityProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |