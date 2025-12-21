# WorkSurfaceProxy Object

Derived from: [WorkSurface](../WorkSurface/WorkSurface.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../WorkSurfaceProxy/WorkSurfaceProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WorkSurfaceProxy/WorkSurfaceProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkSurfaceProxy/WorkSurfaceProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../WorkSurfaceProxy/WorkSurfaceProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Exported](../WorkSurfaceProxy/WorkSurfaceProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [NativeObject](../WorkSurfaceProxy/WorkSurfaceProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../WorkSurfaceProxy/WorkSurfaceProxy_Parent.md) | Property that returns the parent  object from whom this object can logically be reached. |
| [SurfaceBodies](../WorkSurfaceProxy/WorkSurfaceProxy_SurfaceBodies.md) | Property that returns the surface bodies associated with this work surface. A work surface can contain more than one surface body. |
| [Translucent](../WorkSurfaceProxy/WorkSurfaceProxy_Translucent.md) | Specifies the translucency of the work surface. |
| [Type](../WorkSurfaceProxy/WorkSurfaceProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkSurfaceProxy/WorkSurfaceProxy_Visible.md) | Specifies the visibility of the work surface. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |