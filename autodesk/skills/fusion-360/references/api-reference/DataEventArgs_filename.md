# DataEventArgs.filename Property

Parent Object: [DataEventArgs](DataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventArgs.h>

## Description

Gets the filename associated with the operation. If there isn't an associated filename, an empty string is returned. For a download operation, this will be the full filename of the downloaded file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. |

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. ```` ``` #include <Core/Dashboard/DataEventArgs.h>  // Get the value of the property. string propertyValue = dataEventArgs_var->filename(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |