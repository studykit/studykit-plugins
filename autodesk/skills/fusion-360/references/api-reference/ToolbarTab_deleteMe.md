# ToolbarTab.deleteMe Method

Parent Object: [ToolbarTab](ToolbarTab.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTab.h>

## Description

Deletes this tab. Fusion native tabs cannot be deleted. Use the isNative property to determine if this is a native or API created tab.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTab\_var" is a variable referencing a [ToolbarTab](ToolbarTab.htm) object.```` ``` returnValue = toolbarTab_var.deleteMe() ``` ```` |

"toolbarTab\_var" is a variable referencing a [ToolbarTab](ToolbarTab.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |

## Version

Introduced in version October 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |