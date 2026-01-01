# CAMLibrary.urlByLocation Method

Parent Object: [CAMLibrary](CAMLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibrary.h>

## Description

Get the URL for a given LibraryLocations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibrary\_var" is a variable referencing a [CAMLibrary](CAMLibrary.htm) object.```` ``` returnValue = cAMLibrary_var.urlByLocation(location) ``` ```` |

"cAMLibrary\_var" is a variable referencing a [CAMLibrary](CAMLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL for given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| location | [LibraryLocations](LibraryLocations.htm) | The LibraryLocations to be converted into an URL. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |