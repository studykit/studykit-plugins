# WorkSurface Object

## Description

The WorkSurface object represents a work surface, which is a type of work feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../WorkSurface/WorkSurface_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WorkSurface/WorkSurface_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkSurface/WorkSurface_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Exported](../WorkSurface/WorkSurface_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Parent](../WorkSurface/WorkSurface_Parent.md) | Property that returns the parent  object from whom this object can logically be reached. |
| [SurfaceBodies](../WorkSurface/WorkSurface_SurfaceBodies.md) | Property that returns the surface bodies associated with this work surface. A work surface can contain more than one surface body. |
| [Translucent](../WorkSurface/WorkSurface_Translucent.md) | Specifies the translucency of the work surface. |
| [Type](../WorkSurface/WorkSurface_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkSurface/WorkSurface_Visible.md) | Specifies the visibility of the work surface. |

## Accessed From

[WorkSurfaceProxy.NativeObject](../WorkSurfaceProxy/WorkSurfaceProxy_NativeObject.md), [WorkSurfaces.Item](../WorkSurfaces/WorkSurfaces_Item.md)

## Derived Classes

[WorkSurfaceProxy](../WorkSurfaceProxy/WorkSurfaceProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |

## Version

Introduced in version 6
