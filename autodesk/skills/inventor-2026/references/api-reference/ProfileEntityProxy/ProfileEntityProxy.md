# ProfileEntityProxy Object

Derived from: [ProfileEntity](../ProfileEntity/ProfileEntity.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../ProfileEntityProxy/ProfileEntityProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProfileEntityProxy/ProfileEntityProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfileEntityProxy/ProfileEntityProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ProfileEntityProxy/ProfileEntityProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Curve](../ProfileEntityProxy/ProfileEntityProxy_Curve.md) | Property that returns the geometry of the entity. The geometry is returned such that the entities are connected in a head-to-tail fashion. |
| [CurveType](../ProfileEntityProxy/ProfileEntityProxy_CurveType.md) | Property that returns the type of the curve referenced by the profile entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [EndSketchPoint](../ProfileEntityProxy/ProfileEntityProxy_EndSketchPoint.md) | Property that returns the that defines the end of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [NativeObject](../ProfileEntityProxy/ProfileEntityProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OpposedToSketchEntity](../ProfileEntityProxy/ProfileEntityProxy_OpposedToSketchEntity.md) | Property that returns a Boolean indicating if the parametric flow of the profile entity is in the same direction as the sketch entity it was derived from. |
| [Parent](../ProfileEntityProxy/ProfileEntityProxy_Parent.md) | Property that returns the parent ProfilePath of the entity. |
| [SketchEntity](../ProfileEntityProxy/ProfileEntityProxy_SketchEntity.md) | Property that returns the sketch entity this profile entity was derived from. |
| [StartSketchPoint](../ProfileEntityProxy/ProfileEntityProxy_StartSketchPoint.md) | Property that gets the that defines the start of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [Type](../ProfileEntityProxy/ProfileEntityProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
