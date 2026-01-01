# ViewTab Object

## Description

ViewTab Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ViewTab/ViewTab_Close.md) | Method that closes this ViewTab. |
| [MoveToGroup](../ViewTab/ViewTab_MoveToGroup.md) | Method that moves the current view tab to a ViewTabGroup. The ViewTabGroup the current ViewTab moves into will be returned. |
| [MoveToNewViewFrame](../ViewTab/ViewTab_MoveToNewViewFrame.md) | Method that moves current ViewTab to a new ViewFrame. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ViewTab/ViewTab_Application.md) | Read-only property that returns the root Application object. |
| [Type](../ViewTab/ViewTab_Type.md) | Gets the constant that indicates the type of this object. |
| [View](../ViewTab/ViewTab_View.md) | Read-only property that returns the View or WebView this view tab is associated with. |
| [ViewFrame](../ViewTab/ViewTab_ViewFrame.md) | Read-only property that returns the ViewFrame this view tab is located in. |
| [ViewTabGroup](../ViewTab/ViewTab_ViewTabGroup.md) | Read-only property that returns the ViewTabGroup this view tab is located in. This returns Nothing if the ViewTab is not grouped. |

## Accessed From

[View.ViewTab](../View/View_ViewTab.md), [ViewTabGroup.Item](../ViewTabGroup/ViewTabGroup_Item.md), [ViewTabsEnumerator.Item](../ViewTabsEnumerator/ViewTabsEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dock browser pane to a custom ViewFrame](../../sample-programs/DockBrowserPaneSample_Sample.md) | This sample demonstrates how to dock the browser pane to a custom ViewFrame. |
| [Move view tab between different view frames](../../sample-programs/ViewTabMoveSample_Sample.md) | This sample demonstrates how to move views using ViewTab between different view frames. |

## Version

Introduced in version 2022
