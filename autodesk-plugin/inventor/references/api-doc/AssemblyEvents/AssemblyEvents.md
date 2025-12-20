# AssemblyEvents Object

## Description

The AssemblyEvents object provides notification of assembly events including change, delete and constraint.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssemblyEvents/AssemblyEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../AssemblyEvents/AssemblyEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../AssemblyEvents/AssemblyEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnAssemblyChange](../AssemblyEvents/AssemblyEvents_OnAssemblyChange.md) | Event that is fired after any change occurs that impacts the assembly structure. |
| [OnDelete](../AssemblyEvents/AssemblyEvents_OnDelete.md) | Event that is fired whenever an object within this events set is deleted in a document. |
| [OnLoadStateChange](../AssemblyEvents/AssemblyEvents_OnLoadStateChange.md) | Fires when an assembly document goes from lite to full or full to lite loading. |
| [OnNewOccurrence](../AssemblyEvents/AssemblyEvents_OnNewOccurrence.md) | Event that is fired whenever an occurrence is created. |
| [OnNewRelationship](../AssemblyEvents/AssemblyEvents_OnNewRelationship.md) | The OnNewRelationship event notifies a client when a new constraint or connection is added to an assembly. |
| [OnOccurrenceChange](../AssemblyEvents/AssemblyEvents_OnOccurrenceChange.md) | Event that is fired whenever an occurrence changes. |

## Accessed From

[Application.AssemblyEvents](../Application/Application_AssemblyEvents.md), [AssemblyComponentDefinition.AssemblyEvents](../AssemblyComponentDefinition/AssemblyComponentDefinition_AssemblyEvents.md), [InventorServer.AssemblyEvents](InventorServer_AssemblyEvents.md), [InventorServerObject.AssemblyEvents](InventorServerObject_AssemblyEvents.md), [WeldmentComponentDefinition.AssemblyEvents](../WeldmentComponentDefinition/WeldmentComponentDefinition_AssemblyEvents.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |