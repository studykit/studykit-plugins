# HoleTables Object

## Description

The HoleTables collection object represents all the hole tables on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../HoleTables/HoleTables_Add.md) | Method that creates a new hole table by including all holes in the input drawing view. Only those feature types specified in the input (or the default) hole table style will be included. The newly created HoleTable is returned. |
| [AddByFeatureType](../HoleTables/HoleTables_AddByFeatureType.md) | Method that creates a new hole table by including only the holes that are of the specified type in the input drawing view. The newly created HoleTable is returned. |
| [AddSelected](../HoleTables/HoleTables_AddSelected.md) | Method that creates a new hole table by including only the specified holes. The newly created HoleTable is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HoleTables/HoleTables_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../HoleTables/HoleTables_Count.md) | Property that returns the number of items in the collection. |
| [Item](../HoleTables/HoleTables_Item.md) | Returns the specified HoleTable object from the collection. |
| [Type](../HoleTables/HoleTables_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.HoleTables](../Sheet/Sheet_HoleTables.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |