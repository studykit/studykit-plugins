# HoleTableStyle.AddColumn Method

Parent Object: [HoleTableStyle](../HoleTableStyle/HoleTableStyle.md)

## Description

Method that adds a column to the list of default columns in the style.

## Syntax

HoleTableStyle.**AddColumn**( ***PropertyType*** As [HolePropertyEnum](../HolePropertyEnum.md), [***CustomPropertyName***] As String, [***Title***] As String, [***Width***] As Double, [***TitleHorizontalJustification***] As [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md), [***ValueHorizontalJustification***] As [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertyType | [HolePropertyEnum](../HolePropertyEnum.md) | Input HolePropertyEnum that specifies the property type to associate with the column. If kCustomHoleProperty is specified, the CustomPropertyName argument is required. |
| CustomPropertyName | String | Optional input String that specifies the name of the custom property to associate with the column. This argument must be specified if the PropertyType is specified to be kCustomHoleProperty, else the method returns an error. |
| Title | String | Optional input String that specifies the column title. If not specified, the property name is used.   This is an optional argument whose default value is "". |
| Width | Double | Optional input Double that specifies the width of the column. If not specified, the default width value is used. A value of 0 indicates the default width value.   This is an optional argument whose default value is 0.0. |
| TitleHorizontalJustification | [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) | Optional input HorizontalTextAlignmentEnum that specifies the text justification for the column title.   This is an optional argument whose default value is 19969. |
| ValueHorizontalJustification | [HorizontalTextAlignmentEnum](../HorizontalTextAlignmentEnum.md) | Optional input HorizontalTextAlignmentEnum that specifies the text justification for the column values.   This is an optional argument whose default value is 19969. |

## Version

Introduced in version 2011
