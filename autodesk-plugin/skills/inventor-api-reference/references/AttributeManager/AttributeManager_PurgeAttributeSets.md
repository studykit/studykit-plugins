# AttributeManager.PurgeAttributeSets Method

Parent Object: [AttributeManager](../AttributeManager/AttributeManager.md)

## Description

Method that finds and deletes the AttributeSets of the specified names whose parent cannot be resolved. If preview flag is true, then instead of deleting these AttributeSets, it returns their collection.

## Syntax

AttributeManager.**PurgeAttributeSets**( [***AttributeSetName***] As String, [***Preview***] As Boolean, [***PreviewResult***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeSetName | String | Optional input String value that specifies the name of the attribute set. An asterisk can be used as a wild card in the string to match partial strings. If this value is not input it will default to "\*" which will match all attribute sets. The search is not case sensitive. |
| Preview | Boolean | Optional input Boolean that specifies whether to return the collection of to preview prior to deleting them. A value of False (the default) means that the preview collection is not returned.   This is an optional argument whose default value is False. |
| PreviewResult | Variant | Optional output Variant that contains the collection of to preview if Preview is set to True.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5
