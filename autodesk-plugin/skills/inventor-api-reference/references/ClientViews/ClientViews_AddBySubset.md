# ClientViews.AddBySubset Method

Parent Object: [ClientViews](../ClientViews/ClientViews.md)

## Description

Add a new within a rectangular region of a window, identified by its hWnd. This allows multiple views in a single hWnd.

## Syntax

ClientViews.**AddBySubset**( ***HWND*** As Long, ***Left*** As Long, ***Top*** As Long, ***Width*** As Long, ***Height*** As Long ) As [ClientView](../ClientView/ClientView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HWND | Long | Input Long that defines the hWnd for the window to add. |
| Left | Long | Input Long that specifies the position of the left edge of the view. |
| Top | Long | Input Long that specifies the position of the top edge of the view. |
| Width | Long | Input Long that specifies the width of the view. |
| Height | Long | Input Long that specifies the height of the view. |

## Version

Introduced in version 6
