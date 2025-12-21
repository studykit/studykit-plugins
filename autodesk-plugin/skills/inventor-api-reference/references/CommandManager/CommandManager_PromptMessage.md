# CommandManager.PromptMessage Method

Parent Object: [CommandManager](../CommandManager/CommandManager.md)

## Description

This method allows the developer to put up prompt messages (unless the user has suppressed this prompt) much like the Visual Basic MsgBox functionality.

## Remarks

If you pick one of the radio buttons in the "Prompts" section of the dialog, the prompt and your choice will be saved to the registry, and your selection will work for future uses of the prompt (i.e. when the client calls the prompt, if the user has selected one of the "Controls when you will see this prompt" options, the dialog is suppressed, and the answer specified earlier by the user is returned).

## Syntax

CommandManager.**PromptMessage**( ***Prompt*** As String, ***Buttons*** As Long, [***Title***] As Variant, [***DefaultAnswer***] As Variant, [***Restrictions***] As Variant, [***PromptStrings***] As Variant ) As Long

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Prompt | String | The string that will appear in the dialog. The string can include "%s" to indicate a string placeholder, while you can specify the string value using the PromptStrings argument. The string can also specify the hyperlink with XML tags. |
| Buttons | Long | Describes which buttons will be used, and which is the default answer. For example "vbOKCancel + vbDefaultButton1", or "vbYesNo". |
| Title | Variant | Each time you call the function, you can give it a new dialog title/caption. If not supplied, the title will default to "Inventor x", where x is the release number. |
| DefaultAnswer | Variant | The default response for the dialog. (vbOK, vbYes, etc.)   This is an optional argument whose default value is null. |
| Restrictions | Variant | The client can specify which of the "Controls when you will see this prompt" options to allow (these options are grayed on the dialog). Also, in Inventor there is an option for which window should get focus when you exit the dialog (default is the mainframe window of Inventor). Zero or more of the following, in combination (can be added together with +): General options  * \* kNoRestrictions (Allow all of the radio button options in the dialog "Do not show this message again ever", "Do not show this message again this session", for all buttons) * \* kDontAllowNeverAgain (Disable the "Do not show this message again ever" option) * \* kDontAllowNoMoreThisSession (Disable the "Do not show this message again this session" option)   Button 1 options (i.e. what is allowed/not allowed if button 1 is picked) * \* kDontAllowButton1NeverAgain (Disable the "Do not show this message again ever" option if button 1 is selected) * \* kDontAllowButton1NoMoreThisSession (Disable the "Do not show this message again this session")   Button 2 options (i.e. what is allowed/not allowed if button 2 is picked) * \* kDontAllowButton2NeverAgain (Disable the "Do not show this message again ever" option if button 1 is selected) * \* kDontAllowButton2NoMoreThisSession (Disable the "Do not show this message again this session")   Button 3 options (i.e. what is allowed/not allowed if button 3 is picked) * \* kDontAllowButton3NeverAgain (Disable the "Do not show this message again ever" option if button 1 is selected) * \* kDontAllowButton3NoMoreThisSession (Disable the "Do not show this message again this session")     This is an optional argument whose default value is null. |
| PromptStrings | Variant | Optional input String or String array or Long value. If this input is Long it can indicate the parent window handler(HWND) for this prompt. If this argument is String or String array, and the input Prompt value includes "%s" then the "%s" will be replaced by this String value or String array sequentially.   This is an optional argument whose default value is null. |

## Version

Introduced in version 10
