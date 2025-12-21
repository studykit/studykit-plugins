# ViewTab.MoveToNewViewFrame Method

Parent Object: [ViewTab](../ViewTab/ViewTab.md)

## Description

Method that moves current ViewTab to a new ViewFrame.

## Syntax

ViewTab.**MoveToNewViewFrame**( [***ViewFrameWidth***] As Variant, [***ViewFrameHeight***] As Variant, [***ViewFrameLeft***] As Variant, [***ViewFrameTop***] As Variant, [***AdditionalViewTabs***] As Variant ) As [ViewFrame](../ViewFrame/ViewFrame.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewFrameWidth | Variant | Optioanl input Long value that specifies the width of the new ViewFrame. |
| ViewFrameHeight | Variant | Optioanl input Long value that specifies the height of the new ViewFrame.   This is an optional argument whose default value is null. |
| ViewFrameLeft | Variant | Optioanl input Long value that specifies the left of the new ViewFrame.   This is an optional argument whose default value is null. |
| ViewFrameTop | Variant | Optioanl input Long value that specifies the top of the new ViewFrame.   This is an optional argument whose default value is null. |
| AdditionalViewTabs | Variant | Optional input ObjectCollection object containing ViewTab objects as additional view tabs to move to the ViewFrame with current ViewTab.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dock browser pane to a custom ViewFrame](../../sample-programs/DockBrowserPaneSample_Sample.md) | This sample demonstrates how to dock the browser pane to a custom ViewFrame. |
| [Move view tab between different view frames](../../sample-programs/ViewTabMoveSample_Sample.md) | This sample demonstrates how to move views using ViewTab between different view frames. |

## Version

Introduced in version 2022
