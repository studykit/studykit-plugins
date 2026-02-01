# DrawingBOMColumn.GetFilePropertyId Method

Parent Object: [DrawingBOMColumn](../DrawingBOMColumn/DrawingBOMColumn.md)

## Description

Method that returns the id of the property associated with the column. This method will return an error if the PropertyType property does not return a value of kFilePropertyType.

## Syntax

DrawingBOMColumn.**GetFilePropertyId**( ***PropSetId*** As String, ***PropId*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropSetId | String | Returned String that specifies the internal name of the property set that contains the property. This is the FMTID associated with the property set. |
| PropId | Long | Returned Long that specifies the property id. This value is unique within the specified property set. |

## Version

Introduced in version 2009
