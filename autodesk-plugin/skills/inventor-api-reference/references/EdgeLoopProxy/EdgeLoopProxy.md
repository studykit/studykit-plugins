# EdgeLoopProxy Object

Derived from: [EdgeLoop](../EdgeLoop/EdgeLoop.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../EdgeLoopProxy/EdgeLoopProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeLoopProxy/EdgeLoopProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EdgeLoopProxy/EdgeLoopProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../EdgeLoopProxy/EdgeLoopProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Edges](../EdgeLoopProxy/EdgeLoopProxy_Edges.md) | Gets the referenced by this EdgeLoop. |
| [EdgeUses](../EdgeLoopProxy/EdgeLoopProxy_EdgeUses.md) | Gets the referenced by this EdgeLoop. |
| [Face](../EdgeLoopProxy/EdgeLoopProxy_Face.md) | Gets the containing this EdgeLoop. |
| [IsOuterEdgeLoop](../EdgeLoopProxy/EdgeLoopProxy_IsOuterEdgeLoop.md) | Gets whether this EdgeLoop is an external loop, or a loop that encloses material as opposed to a void. |
| [NativeObject](../EdgeLoopProxy/EdgeLoopProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../EdgeLoopProxy/EdgeLoopProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../EdgeLoopProxy/EdgeLoopProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [TransientKey](../EdgeLoopProxy/EdgeLoopProxy_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../EdgeLoopProxy/EdgeLoopProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 4
