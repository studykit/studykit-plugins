# PathEntityProxy Object

Derived from: [PathEntity](../PathEntity/PathEntity.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../PathEntityProxy/PathEntityProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PathEntityProxy/PathEntityProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContainingOccurrence](../PathEntityProxy/PathEntityProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Curve](../PathEntityProxy/PathEntityProxy_Curve.md) | Property that returns the geometry of the entity. The geometry is returned such that the entities are connected in a head-to-tail fashion. |
| [CurveType](../PathEntityProxy/PathEntityProxy_CurveType.md) | Property that returns the type of the curve referenced by the path entity. This property allows you to determine what type of object will be returned by the Curve property. |
| [NativeObject](../PathEntityProxy/PathEntityProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OpposedToSketchEntity](../PathEntityProxy/PathEntityProxy_OpposedToSketchEntity.md) | Property that returns a Boolean indicating if the parametric flow of the path entity is in the same direction as the sketch entity it was derived from. |
| [Parent](../PathEntityProxy/PathEntityProxy_Parent.md) | Property that returns the parent Path of the entity. |
| [SketchEntity](../PathEntityProxy/PathEntityProxy_SketchEntity.md) | Property that gets the sketch entity (2D or 3D) this entity was derived from. |
| [Type](../PathEntityProxy/PathEntityProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |