# TableStyle.AddColumn Method

Parent Object: [TableStyle](../TableStyle/TableStyle.md)

## Description

Method that adds a column to the list of default columns in the style.

## Syntax

TableStyle.**AddColumn**( [***Title***] As String, [***Width***] As Double, [***TitleHorizontalJustification***] As [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md), [***ValueHorizontalJustification***] As [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Title | String | Optional input String that specifies the column title. If not specified, a default name is used. |
| Width | Double | Optional input Double that specifies the width of the column. If not specified, the default width value is used. A value of 0 indicates the default width value.   This is an optional argument whose default value is 0.0. |
| TitleHorizontalJustification | [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) | Optional input HorizontalTextAlignmentEnum that specifies the text justification for the column title.   This is an optional argument whose default value is 19969. |
| ValueHorizontalJustification | [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) | Optional input HorizontalTextAlignmentEnum that specifies the text justification for the column values.   This is an optional argument whose default value is 19969. |

## Version

Introduced in version 2011
