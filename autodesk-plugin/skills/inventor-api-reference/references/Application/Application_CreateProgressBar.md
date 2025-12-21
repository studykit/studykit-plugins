# Application.CreateProgressBar Method

Parent Object: [Application](../Application/Application.md)

## Description

Method that creates a new ProgressBar object. The progress bar is not immediately displayed. Calling the UpdateProgress method for the first time causes the bar to display.

## Syntax

Application.**CreateProgressBar**( ***DisplayInStatusBar*** As Boolean, ***NumberOfSteps*** As Long, ***Title*** As String, [***AllowCancel***] As Boolean, [***HWND***] As Long ) As [ProgressBar](../ProgressBar/ProgressBar.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayInStatusBar | Boolean | Input Boolean that specifies whether the progress bar should be displayed in the status bar or as a dialog. |
| NumberOfSteps | Long | Input long that specifies the number of steps for the progress bar. The ProgressBar.UpdateProgress method should be called as many times as this value. |
| Title | String | Input String that specifies the title for the progress bar. |
| AllowCancel | Boolean | Optional input Boolean that specifies whether the progress bar should display a cancel button for the user to cancel the operation. If specified to be True, the ProgressBar.OnCancel event is fired when the user chooses to cancel the operation. The client should abort their operation and close the progress bar when this event is fired. |
| HWND | Long | Optional input Long that specifies the hwnd of the parent dialog that is launching the progress bar. If not specified, the active Inventor application's hwnd is used. This argument is not applicable if the DisplayInStatusBar argument is set to True.   This is an optional argument whose default value is 0. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |