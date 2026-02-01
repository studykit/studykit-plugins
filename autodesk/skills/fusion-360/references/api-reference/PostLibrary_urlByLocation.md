# PostLibrary.urlByLocation Method

Parent Object: [PostLibrary](PostLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostLibrary.h>

## Description

Get the URL for a given LibraryLocations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postLibrary\_var" is a variable referencing a [PostLibrary](PostLibrary.htm) object.```` ``` returnValue = postLibrary_var.urlByLocation(location) ``` ```` |

"postLibrary\_var" is a variable referencing a [PostLibrary](PostLibrary.htm) object. |

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