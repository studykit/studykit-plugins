# ReferenceKeyManager Object

## Description

Reference key manager object. This object provides methods to create and save reference key contexts as well as bind reference keys to their targets.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BindKeyToObject](../ReferenceKeyManager/ReferenceKeyManager_BindKeyToObject.md) | Method to bind a reference key to the persistent object within the document. Returns a specific object, if there is a unique solution. |
| [CanBindKeyToObject](../ReferenceKeyManager/ReferenceKeyManager_CanBindKeyToObject.md) | Method that returns whether the key can be bound to an entity or not. |
| [CreateKeyContext](../ReferenceKeyManager/ReferenceKeyManager_CreateKeyContext.md) | Method to create a key context to use in the creation of reference keys. |
| [KeyToString](../ReferenceKeyManager/ReferenceKeyManager_KeyToString.md) | Converts a ReferenceKey byte array to a Base64 encoded string. |
| [LoadContextFromArray](../ReferenceKeyManager/ReferenceKeyManager_LoadContextFromArray.md) | Method to load a previously saved key context from an array of data. |
| [ReleaseKeyContext](../ReferenceKeyManager/ReferenceKeyManager_ReleaseKeyContext.md) | Specifies a key context to release. |
| [SaveContextToArray](../ReferenceKeyManager/ReferenceKeyManager_SaveContextToArray.md) | Method to save a key context out as an array of data. |
| [StringToKey](../ReferenceKeyManager/ReferenceKeyManager_StringToKey.md) | Converts a string to a reference key byte array. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ReferenceKeyManager/ReferenceKeyManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../ReferenceKeyManager/ReferenceKeyManager_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../ReferenceKeyManager/ReferenceKeyManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.ReferenceKeyManager](../ApprenticeServerDocument/ApprenticeServerDocument_ReferenceKeyManager.md), [ApprenticeServerDrawingDocument.ReferenceKeyManager](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferenceKeyManager.md), [AssemblyDocument.ReferenceKeyManager](../AssemblyDocument/AssemblyDocument_ReferenceKeyManager.md), [Document.ReferenceKeyManager](../Document/Document_ReferenceKeyManager.md), [DrawingDocument.ReferenceKeyManager](../DrawingDocument/DrawingDocument_ReferenceKeyManager.md), [PartDocument.ReferenceKeyManager](../PartDocument/PartDocument_ReferenceKeyManager.md), [PresentationDocument.ReferenceKeyManager](../PresentationDocument/PresentationDocument_ReferenceKeyManager.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |