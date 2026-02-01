# View.GetWindowExtents Method

Parent Object: [View](../View/View.md)

## Description

Method that returns the current size and position of the view's window.

## Syntax

View.**GetWindowExtents**( ***Top*** As Long, ***Left*** As Long, ***Height*** As Long, ***Width*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Top | Long | Output Long that contains the position of the top edge of the window (including the entire frame of the window). The value returned is in pixels relative to screen space. |
| Left | Long | Output Long that contains the position of the left edge of the window (including the entire frame of the window). The value returned is in pixels relative to screen space. |
| Height | Long | Output Long that contains the height of the window (including the entire frame of the window). The value returned is in pixels. |
| Width | Long | Output Long that contains the width of the window (including the entire frame of the window). The value returned is in pixels. |

## Version

Introduced in version 4
