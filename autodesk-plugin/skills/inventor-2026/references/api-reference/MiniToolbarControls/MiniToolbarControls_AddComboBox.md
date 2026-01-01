# MiniToolbarControls.AddComboBox Method

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Method that creates a new combobox control within the MiniToolbar.

## Syntax

MiniToolbarControls.**AddComboBox**( ***InternalName*** As String, [***ShowIcon***] As Boolean, [***ShowText***] As Boolean, [***Width***] As Long ) As [MiniToolbarComboBox](../MiniToolbarComboBox/MiniToolbarComboBox.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. |
| ShowIcon | Boolean | Optional input Boolean that specifies whether the icon associated with the currently selected item should be displayed on the face of the control. |
| ShowText | Boolean | Optional input Boolean that specifies whether the text associated with the currently selected item should be displayed on the face of the control.   This is an optional argument whose default value is True. |
| Width | Long | Optional input Boolean that specifies whether the text associated with the currently selected item should be displayed on the face of the control.  **Note:** The width and height of the dropdown area of the control are automatically calculated based on the contents.    This is an optional argument whose default value is 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Change color of part, features or faces](../../sample-programs/ChangeAppearanceUsingMiniToolbar_Sample.md) | This sample demonstrates how to use MiniToolBar to change appearance color of part or features or faces. |

## Version

Introduced in version 2012
