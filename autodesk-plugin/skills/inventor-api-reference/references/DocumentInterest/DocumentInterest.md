# DocumentInterest Object

## Description

Provides a means for an application to register an interest in a document. In order words, to flag the document as containing application-specific data, and to set the data version (for example, so Inventor can determine whether data migration is required and so fire the appropriate event).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DocumentInterest/DocumentInterest_Delete.md) | Method that deletes the DocumentInterest object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DocumentInterest/DocumentInterest_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientData](../DocumentInterest/DocumentInterest_ClientData.md) | Gets/Sets additional data that the client would like to store with the interest. This string is not interpreted by Inventor. |
| [ClientId](../DocumentInterest/DocumentInterest_ClientId.md) | Property that returns the ClientId associated with the DocumentInterest indicating the owner of this object. |
| [DataVersion](../DocumentInterest/DocumentInterest_DataVersion.md) | Gets/Sets the current data version of the document. If the property returns -1 or is set to -1, this is assumed to be a 'non-migrating' type of interest. |
| [InterestType](../DocumentInterest/DocumentInterest_InterestType.md) | Gets/Sets the type of interest that the client has in this document. |
| [Name](../DocumentInterest/DocumentInterest_Name.md) | Property that returns the non-localized name associated with this interest. |
| [Parent](../DocumentInterest/DocumentInterest_Parent.md) | Property that returns the parent document object. |
| [Type](../DocumentInterest/DocumentInterest_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DocumentInterests.Add](../DocumentInterests/DocumentInterests_Add.md), [DocumentInterests.Item](../DocumentInterests/DocumentInterests_Item.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |