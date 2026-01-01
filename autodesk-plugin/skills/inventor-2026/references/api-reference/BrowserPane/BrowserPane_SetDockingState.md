# BrowserPane.SetDockingState Method

Parent Object: [BrowserPane](../BrowserPane/BrowserPane.md)

## Description

Method that sets the docking state of the browser pane.

## Syntax

BrowserPane.**SetDockingState**( ***DockingState*** As [DockingStateEnum](../DockingStateEnum.md), [***DockToObject***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DockingState | [DockingStateEnum](../DockingStateEnum.md) | Input DockingStateEnum value that specifies the docking state. |
| DockToObject | Variant | Optional input object to specify where the browser pane docks to. If the DockingState is specified as kFloat then this argument is ignored. Valid object includes: ViewFrame, DockableWindow, BrowserPane. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dock browser pane to a custom ViewFrame](../../sample-programs/DockBrowserPaneSample_Sample.md) | This sample demonstrates how to dock the browser pane to a custom ViewFrame. |

## Version

Introduced in version 2022
