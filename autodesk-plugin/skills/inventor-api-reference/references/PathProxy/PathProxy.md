# PathProxy Object

Derived from: [Path](../Path/Path.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../PathProxy/PathProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PathProxy/PathProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PathProxy/PathProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../PathProxy/PathProxy_Closed.md) | Property that returns a Boolean indicating if the path is closed or not. Returns True in the case of a closed path. |
| [ContainingOccurrence](../PathProxy/PathProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Count](../PathProxy/PathProxy_Count.md) | Property that returns the number of items in this collection. |
| [Item](../PathProxy/PathProxy_Item.md) | Returns the specified PathEntity object from the collection. |
| [NativeObject](../PathProxy/PathProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Type](../PathProxy/PathProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wires](../PathProxy/PathProxy_Wires.md) | Property returning the Wires collection object associated with this Path. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |