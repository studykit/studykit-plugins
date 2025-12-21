# DerivedParameterTables Object

## Description

Creates and provides access to the parameters that reference parameters in another Inventor document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DerivedParameterTables/DerivedParameterTables_Add.md) | Method that creates a new DerivedParameterTable object, given an existing Inventor part or assembly document as input. Returns the resulting DerivedParameterTable object. The creation fails if the input document does not have any exported parameters. |
| [Add2](../DerivedParameterTables/DerivedParameterTables_Add2.md) | Method that creates a new DerivedParameterTable object, given an existing Inventor part or assembly document as input. Returns the resulting DerivedParameterTable object. This method fails if the input document has already been linked. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../DerivedParameterTables/DerivedParameterTables_Count.md) | Property that specifies the number of items in the collection. |
| [Item](../DerivedParameterTables/DerivedParameterTables_Item.md) | Method that returns the specified DerivedParameterTable object from the collection. This is the default method of the DerivedParameterTables collection object. |
| [Type](../DerivedParameterTables/DerivedParameterTables_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Parameters.DerivedParameterTables](../Parameters/Parameters_DerivedParameterTables.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |