# RevisionTableColumn.GetFilePropertyId Method

Parent Object: [RevisionTableColumn](../RevisionTableColumn/RevisionTableColumn.md)

## Description

Method that returns the id of the property associated with the column.

## Syntax

RevisionTableColumn.**GetFilePropertyId**( ***PropertySetId*** As String, ***PropId*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertySetId | String | Output String that specifies the internal name of the property set that contains the property. This is the FMTID associated with the property set. |
| PropId | Long | Output Long that specifies the property id. This value is unique within the specified property set. |

## Version

Introduced in version 2012
