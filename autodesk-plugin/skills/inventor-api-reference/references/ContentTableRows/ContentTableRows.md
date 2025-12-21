# ContentTableRows Object

## Description

The ContentTableRows object is a collection that provides access to the rows of the table associated with a particular content center family.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ContentTableRows/ContentTableRows_Add.md) | Method that creates a new row. Any changes to the table are not actually applied until the ContentFamily.Save method is called. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentTableRows/ContentTableRows_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ContentTableRows/ContentTableRows_Count.md) | Property that returns the number of ContentTableRow objects in the collection. |
| [Item](../ContentTableRows/ContentTableRows_Item.md) | Returns the specified ContentTableRow object from the collection. |
| [Type](../ContentTableRows/ContentTableRows_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ContentFamily.TableRows](../ContentFamily/ContentFamily_TableRows.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |