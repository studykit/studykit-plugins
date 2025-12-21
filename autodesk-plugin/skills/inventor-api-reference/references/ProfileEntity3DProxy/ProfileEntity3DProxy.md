# ProfileEntity3DProxy Object

Derived from: [ProfileEntity3D](../ProfileEntity3D/ProfileEntity3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../ProfileEntity3DProxy/ProfileEntity3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProfileEntity3DProxy/ProfileEntity3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfileEntity3DProxy/ProfileEntity3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ProfileEntity3DProxy/ProfileEntity3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Curve](../ProfileEntity3DProxy/ProfileEntity3DProxy_Curve.md) | Property that returns the geometry of the entity. The geometry is returned such that the entities are connected in a head-to-tail fashion. |
| [CurveType](../ProfileEntity3DProxy/ProfileEntity3DProxy_CurveType.md) | Property that returns the type of the curve referenced by the profile entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [EndSketchPoint](../ProfileEntity3DProxy/ProfileEntity3DProxy_EndSketchPoint.md) | Property that gets the that defines the end of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [NativeObject](../ProfileEntity3DProxy/ProfileEntity3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OpposedToSketchEntity](../ProfileEntity3DProxy/ProfileEntity3DProxy_OpposedToSketchEntity.md) | Property that returns a Boolean indicating if the parametric flow of the profile entity is in the same direction as the sketch entity it was derived from. |
| [Parent](../ProfileEntity3DProxy/ProfileEntity3DProxy_Parent.md) | Property that returns the parent ProfilePath3D of the entity. |
| [SketchEntity](../ProfileEntity3DProxy/ProfileEntity3DProxy_SketchEntity.md) | Property that gets the sketch entity this profile entity was derived from. |
| [StartSketchPoint](../ProfileEntity3DProxy/ProfileEntity3DProxy_StartSketchPoint.md) | Property that gets the that defines the start of the profile entity. This property is not valid in the case where the curve is a periodic curve, i.e. circle, ellipse, etc. |
| [Type](../ProfileEntity3DProxy/ProfileEntity3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
