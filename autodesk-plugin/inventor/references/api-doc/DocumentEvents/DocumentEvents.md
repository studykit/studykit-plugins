# DocumentEvents Object

## Description

The DocumentEvents object provides notification of events that take place at the document level, such as activating, closing and saving particular documents.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DocumentEvents/DocumentEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../DocumentEvents/DocumentEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../DocumentEvents/DocumentEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivate](../DocumentEvents/DocumentEvents_OnActivate.md) | The OnActivate event notifies a client when the document is activated. |
| [OnChange](../DocumentEvents/DocumentEvents_OnChange.md) | Fires when this document changes, supplying the reasons for change and the context in which this action is being taken. |
| [OnChangeSelectSet](../DocumentEvents/DocumentEvents_OnChangeSelectSet.md) | The OnChangeSelectSet event notifies a client when the contents of the select set have changed. |
| [OnClose](../DocumentEvents/DocumentEvents_OnClose.md) | The Onclose event notifies a client when the document is closed. |
| [OnDeactivate](../DocumentEvents/DocumentEvents_OnDeactivate.md) | The OnDeactivate event notifies a client when the document is being deactivated. |
| [OnDelete](../DocumentEvents/DocumentEvents_OnDelete.md) | The OnDelete event notifies a client when an entity is deleted. |
| [OnSave](../DocumentEvents/DocumentEvents_OnSave.md) | The OnSave event notifies a client whenever the document is saved. |

## Accessed From

[AssemblyDocument.DocumentEvents](../AssemblyDocument/AssemblyDocument_DocumentEvents.md), [Document.DocumentEvents](../Document/Document_DocumentEvents.md), [DrawingDocument.DocumentEvents](../DrawingDocument/DrawingDocument_DocumentEvents.md), [PartDocument.DocumentEvents](../PartDocument/PartDocument_DocumentEvents.md), [PresentationDocument.DocumentEvents](../PresentationDocument/PresentationDocument_DocumentEvents.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |