# ClientView.Update Method

Parent Object: [ClientView](../ClientView/ClientView.md)

## Description

Method that redraws the view.

## Syntax

ClientView.**Update**( ***Interactive*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Interactive | Boolean | Input Boolean that specifies the type of update to perform. Interactive update should be used when the user is dynamically modifying the view. During interactive update Autodesk Inventor takes steps to optimize the display in an attempt to achieve a higher frame rate. For example it will create simplified displays of parts and eliminate the display of small parts in assemblies. Setting the Interactive argument to True allows Autodesk Inventor to perform these optimizations. Setting this argument to False causes Autodesk Inventor to perform a complete rendering without any optimizations. Typically you will set the Interactive argument to True while the user is dynamically modifying the view (while the mouse button is down). A final update (When the mouse button is released) is performed with the Interactive argument set to False to get an accurate rendering. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |