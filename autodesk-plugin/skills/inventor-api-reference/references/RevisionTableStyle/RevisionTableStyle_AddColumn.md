# RevisionTableStyle.AddColumn Method

Parent Object: [RevisionTableStyle](../RevisionTableStyle/RevisionTableStyle.md)

## Description

Method that adds a column to the list of default columns in the style.

## Syntax

RevisionTableStyle.**AddColumn**( ***PropertyType*** As [RevisionTablePropertyEnum](../RevisionTablePropertyEnum.md), [***PropertySetId***] As String, [***PropertyIdentifier***] As Variant, [***Title***] As String, [***Width***] As Double, [***TitleHorizontalJustification***] As [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md), [***ValueHorizontalJustification***] As [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertyType | [RevisionTablePropertyEnum](../RevisionTablePropertyEnum.md) | Input RevisionTablePropertyEnum that specifies the property type to associate with the column. Valid values are\:  kRevisionTableFileProperty, kRevisionTableCustomProperty, kRevisionTableDateProperty, kRevisionTableSheetProperty, kRevisionTableZoneProperty, kRevisionTableZoneSheetProperty and kRevisionTableLtrProperty.  If kRevisionTableFileProperty is specified, the PropertySetId and PropertyIdentifier \arguments are required. If kRevisionTableCustomProperty is specified, the PropertyIdentifier argument is required. |
| PropertySetId | String | Optional input String that specifies the internal name of the property set that contains the property. This is the FMTID associated with the property set. This argument is ignored if the input PropertyType is not kRevisionTableFileProperty. |
| PropertyIdentifier | Variant | Optional input Variant that identifies a property. This could either be a Long value that specifies the PropId of a property within the specified property set or the name of a property. Typically, a PropId should be specified when the \input PropertyType is kRevisionTableFileProperty and a name should be specified when the input PropertyType is kRevisionTableCustomProperty.   This is an optional argument whose default value is null. |
| Title | String | Optional input String that specifies the column title. If not specified, the property name is used.   This is an optional argument whose default value is "". |
| Width | Double | Optional input Double that specifies the width of the column. If not specified, the default width value is used. A value of 0 indicates the default width value.   This is an optional argument whose default value is 0.0. |
| TitleHorizontalJustification | [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) | Optional input HorizontalTextAlignmentEnum that specifies the text justification for the column title.   This is an optional argument whose default value is 19969. |
| ValueHorizontalJustification | [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) | Optional input HorizontalTextAlignmentEnum that specifies the text justification for the column values.   This is an optional argument whose default value is 19969. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |