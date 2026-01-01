# ProfileEntity Object

## Description

The ProfileEntity object represents a curve within a profile path.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../ProfileEntity/ProfileEntity_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProfileEntity/ProfileEntity_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfileEntity/ProfileEntity_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Curve](../ProfileEntity/ProfileEntity_Curve.md) | Property that returns the geometry of the entity. The geometry is returned such that the entities are connected in a head-to-tail fashion. |
| [CurveType](../ProfileEntity/ProfileEntity_CurveType.md) | Property that returns the type of the curve referenced by the profile entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [EndSketchPoint](../ProfileEntity/ProfileEntity_EndSketchPoint.md) | Property that returns the that defines the end of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [OpposedToSketchEntity](../ProfileEntity/ProfileEntity_OpposedToSketchEntity.md) | Property that returns a Boolean indicating if the parametric flow of the profile entity is in the same direction as the sketch entity it was derived from. |
| [Parent](../ProfileEntity/ProfileEntity_Parent.md) | Property that returns the parent ProfilePath of the entity. |
| [SketchEntity](../ProfileEntity/ProfileEntity_SketchEntity.md) | Property that returns the sketch entity this profile entity was derived from. |
| [StartSketchPoint](../ProfileEntity/ProfileEntity_StartSketchPoint.md) | Property that gets the that defines the start of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [Type](../ProfileEntity/ProfileEntity_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ProfileEntityProxy.NativeObject](../ProfileEntityProxy/ProfileEntityProxy_NativeObject.md), [ProfilePath.Item](../ProfilePath/ProfilePath_Item.md), [ProfilePathProxy.Item](../ProfilePathProxy/ProfilePathProxy_Item.md)

## Derived Classes

[ProfileEntityProxy](../ProfileEntityProxy/ProfileEntityProxy.md)

## Version

Introduced in version 5
