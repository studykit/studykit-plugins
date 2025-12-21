# DerivedParameterTables.Add Method

Parent Object: [DerivedParameterTables](../DerivedParameterTables/DerivedParameterTables.md)

## Description

Method that creates a new DerivedParameterTable object, given an existing Inventor part or assembly document as input. Returns the resulting DerivedParameterTable object. The creation fails if the input document does not have any exported parameters.

## Syntax

DerivedParameterTables.**Add**( ***FullFileName*** As String ) As [DerivedParameterTable](../DerivedParameterTable/DerivedParameterTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | String value that contains the full path to the part or assembly document. |

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