# BOMView.Renumber Method

Parent Object: [BOMView](../BOMView/BOMView.md)

## Description

Method that renumbers all rows in the BOM view. If the BOMRowsToRenumber argument is provided, only those rows are renumbered. Applies only to structured and parts only views. This method returns a failure for the model data BOM view.

## Syntax

BOMView.**Renumber**( [***StartValue***] As Long, [***Increment***] As Long, [***BOMRowsToRenumber***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartValue | Long | Optional input long that specifies the start value for renumbering. If not specified, this value defaults to 1. |
| Increment | Long | Optional input long that specifies the increment to use for renumbering. If not specified, this value defaults to 1.   This is an optional argument whose default value is 1. |
| BOMRowsToRenumber | Variant | Optional input ObjectCollection of BOMRow objects. If not supplied, all rows in the BOMView are renumbered. If provided, only the input rows are renumbered.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2011
