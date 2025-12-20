# PromptMessages.Add Method

Parent Object: [PromptMessages](../PromptMessages/PromptMessages.md)

## Description

Method that creates a new custom PromptMessage.

## Syntax

PromptMessages.**Add**( ***Id*** As String, ***PromptText*** As String, ***Buttons*** As Long, ***Icon*** As Long, [***Title***] As Variant, [***DisplayedPromptText***] As Variant, [***DefaultAnswer***] As Variant, [***Restrictions***] As Variant, [***PromptSettings***] As Variant ) As [PromptMessage](../PromptMessage/PromptMessage.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Id | String | Input the String value to specify the Id of PromptMessage. The Id should be unique in the collection of the PromptMessage objects. |
| PromptText | String | Input the String value to specify the formatted prompt text of PromptMessage. The string can include “%s” to indicate a string placeholder that you can specify the string value for the placeholder using the PromptStrings argument in PromprMessage.Display method. Currently you can specify up to three placeholders. The string can also specify the hyperlink with XML tags. |
| Buttons | Long | Input the Long value to specify the buttons to use for PromptMessage. Valid values are:  1. vbOKOnly or 0. 2. vbOKCancel or 1. 3. vbAbortRetryIgnore or 2. 4. vbYesNoCancel or 3. 5. vbYesNo or 4. 6. vbRetryCancel or 5. |
| Icon | Long | Input Long that specifies the icon type. This can be vbCritical (16), vbExclamation (48), vbInformation(64) or vbQuestion (32). |
| Title | Variant | Optional input String value to specify the title for PromptMessage. If not supplied, the title will default to "Inventor x", where x is the release number. |
| DisplayedPromptText | Variant | Optional input String value to specify the displayed prompt text of PromptMessage. If not specified the PromptText will be used as DisplayedPromptText and displayed on Prompt Text column onto Prompts option, otherwise this DisplayedPromptText will be displayed instead. This can be set when the PromptText contains special chars that is not suitable to display in UI.   This is an optional argument whose default value is null. |
| DefaultAnswer | Variant | Optional input Long value to specify the default response for the PromptMessage dialog. Valid values are:  1. vbDefaultButton1 (or 0) indicating the first button is set as default response button. This is also default value if not specified. 2. vbDefaultButton2 (or 256) indicating the second button is set as default response button. 3. vbDefaultButton3 (or 512) indicating the third button is set as default response button.  If not supplied the first button will be set as default answer.   This is an optional argument whose default value is null. |
| Restrictions | Variant | Optional input Long(PromptMessageRestrictionsEnum) value to specify the “Controls when you will see this prompt” option for PromptMessage(grey out the options). Zero or more of the following, in combination (can be added together with +):  * kNoRestrictions (Allow all of the radio button options in the dialog "Do not show this message again ever", "Do not show this message again this session", "Prompt only once per operation", "Always show this message ", for all buttons) * kDontAllowNeverAgain (Disable the "Do not show this message again ever" option) * kDontAllowNoMoreThisSession (Disable the "Do not show this message again this session" option)  Button 1 options (i.e. what is allowed/not allowed if button 1 is picked) :  * kDontAllowButton1NeverAgain (Disable the "Do not show this message again ever" option if button 1 is selected) * kDontAllowButton1NoMoreThisSession (Disable the "Do not show this message again this session" option if button 1 is selected)  Button 2 options (i.e. what is allowed/not allowed if button 2 is picked) :  * kDontAllowButton1NeverAgain (Disable the "Do not show this message again ever" option if button 2 is selected) * kDontAllowButton1NoMoreThisSession (Disable the "Do not show this message again this session" option if button 2 is selected)  Button 3 options (i.e. what is allowed/not allowed if button 3 is picked) :  * kDontAllowButton1NeverAgain (Disable the "Do not show this message again ever" option if button 3 is selected) * kDontAllowButton1NoMoreThisSession (Disable the "Do not show this message again this session" option if button 3 is selected)     This is an optional argument whose default value is null. |
| PromptSettings | Variant | Optional input NameValueMap object that specifies more prompt settings. This is reserved for future use.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Prompt message creation sample](../../sample-programs/PromptMessageCreationSample_Sample.md) | This sample demonstrates how to creat a custom prompt message. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |