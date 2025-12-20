# RevisionTableColumns.Add Method

Parent Object: [RevisionTableColumns](../RevisionTableColumns/RevisionTableColumns.md)

## Description

Method that creates a new revision table column based on a property.

## Syntax

RevisionTableColumns.**Add**( ***PropertyType*** As [RevisionTablePropertyEnum](../RevisionTablePropertyEnum.md), [***PropertySetId***] As String, [***PropertyIdentifier***] As Variant, [***TargetIndex***] As Long, [***InsertBefore***] As Boolean ) As [RevisionTableColumn](../RevisionTableColumn/RevisionTableColumn.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertyType | [RevisionTablePropertyEnum](../RevisionTablePropertyEnum.md) | Input RevisionTablePropertyEnum that specifies the property type to associate with the column. Valid values are kRevisionTableFileProperty, kRevisionTableCustomProperty, kRevisionTableDateProperty, kRevisionTableSheetProperty, kRevisionTableZoneProperty, kRevisionTableZoneSheetPropertyand kRevisionTableLtrProperty. If kRevisionTableFileProperty is specified, the PropertySetId and PropertyIdentifier arguments are required. If kRevisionTableCustomProperty is specified, the PropertyIdentifier argument is required. |
| PropertySetId | String | Optional input String that specifies the internal name of the property set that contains the property. This is the FMTID associated with the property set. This argument is ignored if the input PropertyType is not kRevisionTableFileProperty. |
| PropertyIdentifier | Variant | Optional input Variant that identifies a property. This could either be a Long value that specifies the PropId of a property within the specified property set or the name of a property. Typically, a PropId should be specified when the input PropertyType is kRevisionTableFileProperty and a name should be specified when the input PropertyType is kRevisionTableCustomProperty.   This is an optional argument whose default value is null. |
| TargetIndex | Long | Optional input Long that specifies the existing column next to which the new column will be inserted. The valid range of values is 0 to the number of existing columns in the table. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the column will be added at the end.   This is an optional argument whose default value is 0. |
| InsertBefore | Boolean | Optional input Boolean indicating if the column should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |