# ToolLibraries.updateToolLibrary Method

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

Update ToolLibrary in ToolLibraries. Overrides the URL by given ToolLibrary. Throws an error if the URL does not already point to an existing ToolLibrary.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object.```` ``` returnValue = toolLibraries_var.updateToolLibrary(url, toolLibrary) ``` ```` |

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if asset was updated successfully, false otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the existing asset in the ToolLibraries that should be updated. |
| toolLibrary | [ToolLibrary](ToolLibrary.htm) | The ToolLibrary that should be persisted. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |