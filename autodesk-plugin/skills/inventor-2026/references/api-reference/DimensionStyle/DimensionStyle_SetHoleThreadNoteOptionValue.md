# DimensionStyle.SetHoleThreadNoteOptionValue Method

Parent Object: [DimensionStyle](../DimensionStyle/DimensionStyle.md)

## Description

Sets the option value for hole thread notes.

## Syntax

DimensionStyle.**SetHoleThreadNoteOptionValue**( ***HoleThreadType*** As String, ***OptionName*** As String, ***OptionValue*** As Variant, [***ApplyToAll***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HoleThreadType | String | Input String value that specifies a hole or thread type. The HoleThreadTypeList can return the hole and thread type list for this argument to use. The English-based hole or thread type can always be used as valid input for this argument(like “Thru” or “Thru Counterbore” etc.). |
| OptionName | String | Input String value that specifies an option name. Below are valid option names and value types: |
| OptionValue | Variant | Input value that specifies an option value. Refer to OptionName to find the value type to set for an option. |
| ApplyToAll | Variant | Optional input Boolean that specifies whether the value change should be applied to all the hole and thread types. If not provided this default to False.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025
