# Documents Object

Derived from: [DocumentsEnumerator](../DocumentsEnumerator/DocumentsEnumerator.md) Object

## Description

The Document collection object contains all in-memory Inventor documents.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../Documents/Documents_Add.md) | Creates a new of the specified type. Optionally, a template file can be specified instead. |
| [CloseAll](../Documents/Documents_CloseAll.md) | Method that closes all the documents in the current Inventor session. Changes are not saved to any of the documents. In other words, if there are dirty documents in the collection, changes made to them will be lost. |
| [Open](../Documents/Documents_Open.md) | Method that opens the specified Inventor document. |
| [OpenWithOptions](../Documents/Documents_OpenWithOptions.md) | Method that opens the specified Inventor document. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../Documents/Documents_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Documents/Documents_Item.md) | Returns the specified object from the collection. This is the default property of the DocumentsEnumerator object. |
| [ItemByName](../Documents/Documents_ItemByName.md) | Returns the specified Document object from the collection. |
| [LoadedCount](../Documents/Documents_LoadedCount.md) | Query Loaded documents. |
| [Type](../Documents/Documents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VisibleDocuments](../Documents/Documents_VisibleDocuments.md) | Gets the collection of visible documents. |

## Accessed From

[Application.Documents](../Application/Application_Documents.md), [InventorServer.Documents](InventorServer_Documents.md), [InventorServerObject.Documents](InventorServerObject_Documents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |

## Version

Introduced in version 4
