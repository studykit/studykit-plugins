# ChangeManager.GetScriptKeyFromObject Method

Parent Object: [ChangeManager](../ChangeManager/ChangeManager.md)

## Description

Method that generates a key (identifier) for the input object. This key is suitable to use in constructing the Inputs argument of the OnWriteToScript event on the ChangeProcessor object. This key is only intended to be able to identify the specified object in the current state of the document (this is not a robust persistent reference key).

## Remarks

This script key mechanism is not a substitute for the ReferenceKey functionality. This API is specifically intended to enable third party developers to generate reliable transcript keys during transcript creation, and also to bind back to these keys during transcript replay. As a general rule, do not use script key functionality outside the scope of ChangeProcessor.OnWriteToScript and ChangeProcessor.OnReadFromScript.

## Syntax

ChangeManager.**GetScriptKeyFromObject**( ***Object*** As Object ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Object | Object | Object from which to generate key. |

## Version

Introduced in version 11
