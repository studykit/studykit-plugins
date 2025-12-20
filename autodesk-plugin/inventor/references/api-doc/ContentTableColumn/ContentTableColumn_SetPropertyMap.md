# ContentTableColumn.SetPropertyMap Method

Parent Object: [ContentTableColumn](../ContentTableColumn/ContentTableColumn.md)

## Description

Method that sets the information associated with a custom expression.

## Remarks

This method is only valid when the HasCustomExpression property returns True. Any changes to the table are not actually applied until the ContentFamily.Save method is called.

## Syntax

ContentTableColumn.**SetPropertyMap**( ***PropertySetId*** As String, ***PropertyIdentifier*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertySetId | String | Input String that specifies the name of the property set that contains the property. This is the InternalName or Name associated with the property set. |
| PropertyIdentifier | Variant | Input Variant that identifies a property. This can be a Long value that specifies the PropId of a property within the specified property set or the name of a property. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |