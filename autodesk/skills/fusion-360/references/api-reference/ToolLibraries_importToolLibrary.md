# ToolLibraries.importToolLibrary Method

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

Import a given ToolLibrary from a specific location. The imported ToolLibrary can be accessed through this ToolLibraries object. Throws an error, if the given URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object.```` ``` returnValue = toolLibraries_var.importToolLibrary(toolLibrary, destinationUrl, libraryName) ``` ```` |

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL of the newly imported tool library, or null if the import failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| toolLibrary | [ToolLibrary](ToolLibrary.htm) | The ToolLibrary that should be imported. |
| destinationUrl | [URL](URL.htm) | The URL to the parent folder where the imported tool library will be saved. |
| libraryName | string | The name of the library that should be created due to the import. If the specified name already exists, a number will be added to the name to ensure it is unique. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |