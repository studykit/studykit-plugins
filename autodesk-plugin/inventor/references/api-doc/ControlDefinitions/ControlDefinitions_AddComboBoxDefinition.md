# ControlDefinitions.AddComboBoxDefinition Method

Parent Object: [ControlDefinitions](../ControlDefinitions/ControlDefinitions.md)

## Description

Method that creates a new ComboBoxDefinition object.

## Syntax

ControlDefinitions.**AddComboBoxDefinition**( ***DisplayName*** As String, ***InternalName*** As String, ***Classification*** As [CommandTypesEnum](../CommandTypesEnum.md), ***DropDownWidth*** As Long, [***ClientId***] As Variant, [***DescriptionText***] As String, [***ToolTipText***] As String, [***StandardIcon***] As Variant, [***LargeIcon***] As Variant, [***ButtonDisplay***] As [ButtonDisplayEnum](../ButtonDisplayEnum.md) ) As [ComboBoxDefinition](../ComboBoxDefinition/ComboBoxDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayName | String | Input String that specifies the display name associated with this definition. The display name is the text that is displayed to the user. Because this string is displayed to the user, you should consider localizing it for different languages. |
| InternalName | String | Input String value that defines the unique name of the definition. This name is never displayed to the user. The name must be unique with respect to all other control definitions and command bars in Inventor. Because of the uniqueness requirement, it is recommended that you add your application name to the name to help eliminate naming conflicts. For example instead of the name 'Analyze' it might be 'ACMEAnalyze'. |
| Classification | [CommandTypesEnum](../CommandTypesEnum.md) | Input that sets the classification for this ControlDefinition. These classifications are bits and can be combined to designate that a command falls within more than one classification. |
| DropDownWidth | Long | Input Long that specifies the width (in pixels) of the drop-down portion of a combo box. |
| ClientId | Variant | Optional input string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". When set shortcut to a ComboBoxDefinition this is required to make the shortcut to work because Inventor requires this to determine if the addin is loaded or not. |
| DescriptionText | String | Optional input String that specifies the description text for this definition. The description text is displayed in the status bar when the mouse is moved over a control associated with the definition. If not supplied the display name will be used for the description text.   This is an optional argument whose default value is "". |
| ToolTipText | String | Optional input String that specifies the tool tip text for this definition. If not supplied the display name will be used for the tool tip text.   This is an optional argument whose default value is "". |
| StandardIcon | Variant | Optional input Picture (IPictureDisp) object that specifies the standard size icon to use for the controls using this definition. A standard size icon is 16 pixels wide and 16 pixels high. All icons use 16 colors. If not supplied the button will be created as a text only button and the LargeIcon argument is ignored.   This is an optional argument whose default value is null. |
| LargeIcon | Variant | Optional input Picture (IPictureDisp) object that specifies the large size icon to use for the controls using this definition. A large size icon is 24 pixels wide and 24 pixels high. All icons use 16 colors. If not supplied and a standard size icon is supplied a large icon will be automatically created by scaling the standard size icon. Because scaling a bitmap does not necessarily create a good image, it is recommended that you create and supply a large bitmap.   This is an optional argument whose default value is null. |
| ButtonDisplay | [ButtonDisplayEnum](../ButtonDisplayEnum.md) | constant indicating whether to display text and icons on a button.   This is an optional argument whose default value is 43011. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |