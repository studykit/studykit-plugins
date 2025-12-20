# DesignProjectManager.AddOptionsButton Method

Parent Object: [DesignProjectManager](../DesignProjectManager/DesignProjectManager.md)

## Description

Method that adds an options button to the Projects dialog. The returned button object can be used to receive an OnClick event fired when the user clicks the option button.

## Syntax

DesignProjectManager.**AddOptionsButton**( ***ClientId*** As String, ***DisplayName*** As String, ***ToolTipText*** As String, [***StandardIcon***] As Variant ) As [ProjectOptionsButton](../ProjectOptionsButton/ProjectOptionsButton.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input string that uniquely identifies the client. |
| DisplayName | String | Input string that specifies the dispaly name of the control. |
| ToolTipText | String | Input string that specifies the tooltip text. |
| StandardIcon | Variant | Optional input Picture (IPictureDisp) object that specifies the icon to use for the control. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |