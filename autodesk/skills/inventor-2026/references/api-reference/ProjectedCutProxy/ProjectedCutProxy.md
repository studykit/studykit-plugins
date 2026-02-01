# ProjectedCutProxy Object

Derived from: [ProjectedCut](../ProjectedCut/ProjectedCut.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../ProjectedCutProxy/ProjectedCutProxy_BreakLink.md) | Method that breaks the link between the projected cut edges and the model. |
| [Delete](../ProjectedCutProxy/ProjectedCutProxy_Delete.md) | Method that deletes the projected cut edges. |
| [GetReferenceKey](../ProjectedCutProxy/ProjectedCutProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProjectedCutProxy/ProjectedCutProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProjectedCutProxy/ProjectedCutProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ProjectedCutProxy/ProjectedCutProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Name](../ProjectedCutProxy/ProjectedCutProxy_Name.md) | Gets and sets name of the projected cut edges. |
| [NativeObject](../ProjectedCutProxy/ProjectedCutProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../ProjectedCutProxy/ProjectedCutProxy_Parent.md) | Property that returns the parent sketch of the projected cut edges. |
| [SketchEntities](../ProjectedCutProxy/ProjectedCutProxy_SketchEntities.md) | Property that returns a collection of sketch entities that belong to the projected cut edges. The sketch entities returned by this property cannot be edited or deleted because they are associated with the projected edges in the model. |
| [Type](../ProjectedCutProxy/ProjectedCutProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2010
