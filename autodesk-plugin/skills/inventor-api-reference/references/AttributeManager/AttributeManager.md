# AttributeManager Object

## Description

Dynamic attributes provide the ability for a programmer to add any arbitrary data to any persistent object within Autodesk Inventor.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [FindAttributes](../AttributeManager/AttributeManager_FindAttributes.md) | Method that returns the Attribute objects that match the search criteria. |
| [FindAttributeSets](../AttributeManager/AttributeManager_FindAttributeSets.md) | Method that returns attribute sets that have the specified names and values. |
| [FindObjects](../AttributeManager/AttributeManager_FindObjects.md) | Method that returns the objects that have the specified attributes. |
| [FindObjectsByPattern](../AttributeManager/AttributeManager_FindObjectsByPattern.md) | Method that returns the objects whose AttributeSets, if converted to XML, satisfy the specified XSL pattern. |
| [OpenAttributeSets](../AttributeManager/AttributeManager_OpenAttributeSets.md) | Finds the AttributeSet of the given name for each object in the object collection. If it does not find one, it creates a new AttributeSet. returns the in the same order as the object collection. Using this method is several times faster than accessing AttributeSets for each object individually. OpenAttributeSets works correctly even if the given collection has degenerate objects such as an edge for the apex of a cone. In such a case, OpenAttributeSets succeeds for all the valid objects, and returns NULL objects for the degenerate objects. |
| [PurgeAttributeSets](../AttributeManager/AttributeManager_PurgeAttributeSets.md) | Method that finds and deletes the AttributeSets of the specified names whose parent cannot be resolved. If preview flag is true, then instead of deleting these AttributeSets, it returns their collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Parent](../AttributeManager/AttributeManager_Parent.md) | Property that returns either the Autodesk Inventor document or the ApprenticeServerDocument. |
| [RevisionId](../AttributeManager/AttributeManager_RevisionId.md) | Gets the GUID that represents the last saved revision of this file. Works as a stamp of the contents of this file. |
| [Type](../AttributeManager/AttributeManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.AttributeManager](../ApprenticeServerDocument/ApprenticeServerDocument_AttributeManager.md), [ApprenticeServerDrawingDocument.AttributeManager](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_AttributeManager.md), [AssemblyDocument.AttributeManager](../AssemblyDocument/AssemblyDocument_AttributeManager.md), [Document.AttributeManager](../Document/Document_AttributeManager.md), [DrawingDocument.AttributeManager](../DrawingDocument/DrawingDocument_AttributeManager.md), [PartDocument.AttributeManager](../PartDocument/PartDocument_AttributeManager.md), [PresentationDocument.AttributeManager](../PresentationDocument/PresentationDocument_AttributeManager.md)

## Version

Introduced in version 5
