# MaterialLibraries.load Method

Parent Object: [MaterialLibraries](MaterialLibraries.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibraries.h>

## Description

Loads the specified existing local material library. Fusion remembers which libraries have been loaded from one session to the next so you should check to see if the local library is already loaded or not before loading it again.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibraries\_var" is a variable referencing a [MaterialLibraries](MaterialLibraries.htm) object.```` ``` returnValue = materialLibraries_var.load(filename) ``` ```` |

"materialLibraries\_var" is a variable referencing a [MaterialLibraries](MaterialLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MaterialLibrary](MaterialLibrary.htm) | Returns the MaterialLibrary object representing the opened library or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename of the .adsklib material file. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |