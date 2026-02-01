# ChangeManager.GetObjectFromScriptKey Method

Parent Object: [ChangeManager](../ChangeManager/ChangeManager.md)

## Description

Method that retrieves the object with the specified string. The script key should have been generated using the GetScriptKeyFromObject method and the document should be in the same or similar state as when the script key was generated.

## Remarks

This script key mechanism is not a substitute for the ReferenceKey functionality. This API is specifically intended to enable third party developers to generate reliable transcript keys during transcript creation, and also to bind back to these keys during transcript replay. As a general rule, do not use script key functionality outside the scope of ChangeProcessor.OnWriteToScript and ChangeProcessor.OnReadFromScript.

## Syntax

ChangeManager.**GetObjectFromScriptKey**( ***ScriptKey*** As String ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ScriptKey | String | Script key string of object to retrieve. |

## Version

Introduced in version 11
