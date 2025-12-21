# ProfileEntity3D Object

## Description

The ProfileEntity3D object represents a curve within a 3D profile path.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../ProfileEntity3D/ProfileEntity3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProfileEntity3D/ProfileEntity3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfileEntity3D/ProfileEntity3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Curve](../ProfileEntity3D/ProfileEntity3D_Curve.md) | Property that returns the geometry of the entity. The geometry is returned such that the entities are connected in a head-to-tail fashion. |
| [CurveType](../ProfileEntity3D/ProfileEntity3D_CurveType.md) | Property that returns the type of the curve referenced by the profile entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [EndSketchPoint](../ProfileEntity3D/ProfileEntity3D_EndSketchPoint.md) | Property that gets the that defines the end of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [OpposedToSketchEntity](../ProfileEntity3D/ProfileEntity3D_OpposedToSketchEntity.md) | Property that returns a Boolean indicating if the parametric flow of the profile entity is in the same direction as the sketch entity it was derived from. |
| [Parent](../ProfileEntity3D/ProfileEntity3D_Parent.md) | Property that returns the parent ProfilePath3D of the entity. |
| [SketchEntity](../ProfileEntity3D/ProfileEntity3D_SketchEntity.md) | Property that gets the sketch entity this profile entity was derived from. |
| [StartSketchPoint](../ProfileEntity3D/ProfileEntity3D_StartSketchPoint.md) | Property that gets the that defines the start of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [Type](../ProfileEntity3D/ProfileEntity3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ProfileEntity3DProxy.NativeObject](../ProfileEntity3DProxy/ProfileEntity3DProxy_NativeObject.md), [ProfilePath3D.Item](../ProfilePath3D/ProfilePath3D_Item.md), [ProfilePath3DProxy.Item](../ProfilePath3DProxy/ProfilePath3DProxy_Item.md)

## Derived Classes

[ProfileEntity3DProxy](../ProfileEntity3DProxy/ProfileEntity3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |