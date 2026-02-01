# ToolbarPanels.item Method

Parent Object: [ToolbarPanels](ToolbarPanels.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanels.h>

## Description

Returns the specified toolbar panel using an index into the collection. When iterating by index, the panels are returned in the same order as they are shown in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanels\_var" is a variable referencing a [ToolbarPanels](ToolbarPanels.htm) object.```` ``` returnValue = toolbarPanels_var.item(index) ``` ```` |

"toolbarPanels\_var" is a variable referencing a [ToolbarPanels](ToolbarPanels.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarPanel](ToolbarPanel.htm) | Returns the specified item or null if an invalid index was specified. |

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

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |