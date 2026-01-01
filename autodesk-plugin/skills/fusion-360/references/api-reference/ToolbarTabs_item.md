# ToolbarTabs.item Method

Parent Object: [ToolbarTabs](ToolbarTabs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabs.h>

## Description

Returns the specified toolbar tab using an index into the collection. When iterating by index, the tabs are returned in the same order as they are shown in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabs\_var" is a variable referencing a [ToolbarTabs](ToolbarTabs.htm) object.```` ``` returnValue = toolbarTabs_var.item(index) ``` ```` |

"toolbarTabs\_var" is a variable referencing a [ToolbarTabs](ToolbarTabs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarTab](ToolbarTab.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |