# AttributeSets.Add Method

Parent Object: [AttributeSets](../AttributeSets/AttributeSets.md)

## Description

Method that creates a new for the object the AttributeSets collection was obtained from. The created AttributeSet object is returned.

## Syntax

AttributeSets.**Add**( ***AttributeSetName*** As String, [***CopyWithOwner***] As Boolean ) As [AttributeSet](../AttributeSet/AttributeSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeSetName | String | Input String value that specifies the name of the attribute set. The name must be unique with respect to the other attribute sets attached to this object. If it is not unique, an error will occur. |
| CopyWithOwner | Boolean | Property that specifies whether the attribute set should be copied with its owner when the object it is associated with is copied or split. If True, the attribute set is copied. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |