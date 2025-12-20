# SearchBox Object

## Description

Represents a search box in the browser.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Search](../SearchBox/SearchBox_Search.md) | Method that start to search text. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SearchBox/SearchBox_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Enabled](../SearchBox/SearchBox_Enabled.md) | Read-write property that gets and sets whether the search box is enabled or not. |
| [Parent](../SearchBox/SearchBox_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SearchBoxEvents](../SearchBox/SearchBox_SearchBoxEvents.md) | Read-only property that returns a SearchBoxEvents object. |
| [SearchFilter](../SearchBox/SearchBox_SearchFilter.md) | Read-only property that returns the search box filter. This could be a bit-mask defining various of filters. Set this to 0 will clear the search filter. |
| [SearchText](../SearchBox/SearchBox_SearchText.md) | Read-only property that returns the search text. |
| [Type](../SearchBox/SearchBox_Type.md) | Gets the constant that indicates the type of this object. |
| [Visible](../SearchBox/SearchBox_Visible.md) | Read-write property that gets and sets whether the search box is displayed or hidden. |

## Accessed From

[BrowserPane.SearchBox](../BrowserPane/BrowserPane_SearchBox.md), [SearchBoxEvents.Parent](../SearchBoxEvents/SearchBoxEvents_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Browser Search Box Sample](../../sample-programs/SearchBoxSample_Sample.md) | This sample demonstrates how to use the search box in a document's browser pane. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |