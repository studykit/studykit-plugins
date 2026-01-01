# FaceShellProxy Object

Derived from: [FaceShell](../FaceShell/FaceShell.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../FaceShellProxy/FaceShellProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FaceShellProxy/FaceShellProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FaceShellProxy/FaceShellProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../FaceShellProxy/FaceShellProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Edges](../FaceShellProxy/FaceShellProxy_Edges.md) | Gets the referenced by this FaceShell. |
| [Faces](../FaceShellProxy/FaceShellProxy_Faces.md) | Property that returns a collection object generated as a result of the feature. |
| [IsClosed](../FaceShellProxy/FaceShellProxy_IsClosed.md) | Indicates whether the FaceShell is closed. |
| [IsPointInside](../FaceShellProxy/FaceShellProxy_IsPointInside.md) | Property that returns a constant indicating whether the specified point is inside, on or outside the body. |
| [IsVoid](../FaceShellProxy/FaceShellProxy_IsVoid.md) | Indicates whether the FaceShell is a void. |
| [NativeObject](../FaceShellProxy/FaceShellProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../FaceShellProxy/FaceShellProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../FaceShellProxy/FaceShellProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [SurfaceBody](../FaceShellProxy/FaceShellProxy_SurfaceBody.md) | Property that returns the surface body for this face shell. |
| [TransientKey](../FaceShellProxy/FaceShellProxy_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../FaceShellProxy/FaceShellProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Volume](../FaceShellProxy/FaceShellProxy_Volume.md) | Property that returns the volume of the component in database units. |

## Version

Introduced in version 4
